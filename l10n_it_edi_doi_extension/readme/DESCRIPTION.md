**English**

This module extends the functionality of l10n_it_edi_doi, enabling the
use of the Declaration of Intent (Dichiarazione di Intento) for incoming
vendor bills and purchase orders.

Key features:
 - Support for multiple Declarations of Intent per invoice
 - Dedicated tab in invoice form for managing DOI associations
 - Automatic validation of DOI amounts and available thresholds
 - Smart warnings when invoice amounts don't match DOI coverage
 - Backward compatibility with single-declaration workflow
 - Check that the invoice lines with the DoI tax do not include other taxes

To use the DoI tax together with taxes that are not VAT (e.g. withholding
taxes) in the same invoice line, install the module "ITA - Registri IVA"
(l10n_it_vat_registries) and set those taxes as excluded from the VAT
registries.

**Italiano**

Questo modulo estende la funzionalità di l10n_it_edi_doi, permettendo
l'utilizzo della Dichiarazione di Intento per le fatture di acquisto in
ingresso e gli ordini di acquisto.

Caratteristiche principali:
 - Supporto per dichiarazioni di intento multiple per fattura
 - Tab dedicato nel form fattura per gestire le associazioni DOI
 - Validazione automatica degli importi e soglie disponibili
 - Avvisi intelligenti quando gli importi non corrispondono
 - Retrocompatibilità con il flusso a dichiarazione singola
 - Verifica che le righe con l'imposta per la DI non includano altre imposte

Per usare l'imposta per la DI insieme a imposte che non sono IVA (ad es.
ritenute) nella stessa riga di fattura, installare il modulo "ITA - Registri
IVA" (l10n_it_vat_registries) e impostare tali imposte come escluse dai
registri IVA.
