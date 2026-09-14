**Italiano**

Con questo modulo installato i prelievi non sono più DDT per la fatturazione
elettronica, quindi i test di `l10n_it_stock_ddt` che se lo aspettano
(ad esempio `TestItEdiDDT.test_deferred_invoice` e i controlli su
`l10n_it_ddt_ids` in `TestDDT`) falliscono.

**English**

With this module installed the pickings are no longer DDT for electronic
invoicing, so the tests of `l10n_it_stock_ddt` expecting it
(e.g. `TestItEdiDDT.test_deferred_invoice` and the checks on
`l10n_it_ddt_ids` in `TestDDT`) fail.
