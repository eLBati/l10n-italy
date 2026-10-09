**Italiano**

Questo modulo sostituisce `l10n_it_intrastat_statement`, rinominato per
coerenza con `l10n_it_intrastat_oca`.

Nei database migrati con OpenUpgrade la rinomina è automatica.

Nei database migrati con il servizio di Odoo SA (upgrade.odoo.com),
installare questo modulo: durante l'installazione assorbe i dati del
vecchio modulo `l10n_it_intrastat_statement`.

I moduli che dipendono da `l10n_it_intrastat_statement` devono usare il
nuovo nome nelle dipendenze e negli XMLID.
