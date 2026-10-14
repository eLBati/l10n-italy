# Copyright 2025 Simone Rubino
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from lxml import etree

from odoo import api, models

_logger = logging.getLogger(__name__)


class AccountJournal(models.Model):
    _inherit = "account.journal"

    @api.model
    def _l10n_it_edi_extension_split_content(self, attachment):
        """
        Break down the content of `attachment`
        if contains multiple FatturaElettronicaBody.

        If `attachment` is an e-invoice that contains N FatturaElettronicaBody:

        <FatturaElettronica>
            <FatturaElettronicaHeader/>
            <FatturaElettronicaBody>
                // Content of 1st invoice
            </FatturaElettronicaBody>
            // ...
            <FatturaElettronicaBody>
                // Content of N-th invoice
            </FatturaElettronicaBody>
        </FatturaElettronica>

        return a list of N strings (bytes) with the same FatturaElettronicaHeader:

        <FatturaElettronica>
            <FatturaElettronicaHeader/>
            <FatturaElettronicaBody>
                // Content of N-th invoice
            </FatturaElettronicaBody>
        </FatturaElettronica>
        """
        attachment.ensure_one()

        if (
            xml_tree := attachment._parse_xml_with_recovery(
                attachment.raw, name=attachment.name
            )
        ) is not None:
            bodies = xml_tree.xpath("//FatturaElettronicaBody")
            if len(bodies) <= 1:
                # Nothing to split: return the original bytes untouched. Avoids a
                # needless parse-rebuild-serialize round-trip for the common
                # single-invoice case, and keeps the original signed/namespaced
                # file intact (no lossy re-serialization).
                return [attachment.raw]
            header = xml_tree.xpath("//FatturaElettronicaHeader")[0]
            result = []
            for body in bodies:
                e_invoice_root = etree.Element("FatturaElettronica")
                e_invoice_root.insert(0, header)
                e_invoice_root.insert(1, body)
                result.append(etree.tostring(e_invoice_root))
        else:
            result = [attachment.raw]
        return result

    def _create_document_from_attachment(self, attachment_ids):
        """Return also the invoices created from multi-invoice e-invoices.

        `account.move._extend_with_attachments` creates one invoice for each
        FatturaElettronicaBody after the first one, but core only collects
        the invoice it created itself for each attachment: gather the other
        ones, give them the same treatment and return them too.
        """
        split_move_ids = []
        invoices = super(
            AccountJournal,
            self.with_context(l10n_it_edi_extension_split_move_ids=split_move_ids),
        )._create_document_from_attachment(attachment_ids)
        split_invoices = self.env["account.move"].browse(split_move_ids)
        for invoice in split_invoices:
            invoice.with_context(
                account_predictive_bills_disable_prediction=True,
                no_new_invoice=True,
            ).message_post(attachment_ids=invoice.l10n_it_edi_attachment_id.ids)
            invoice._autopost_bill()
        return invoices | split_invoices
