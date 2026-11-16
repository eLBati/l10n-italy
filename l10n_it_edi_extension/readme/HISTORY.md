## Unreleased

### Bugfixes

- Switch the external Python dependency to `python-codicefiscale`
  (fabiocaccamo), which is actively maintained and compatible with
  Python 3.12. The previous `codicefiscale` (baxeico) distribution is
  unmaintained since 2017 and, when installed on Odoo 19.0, caused the
  wizard to fail at import with
  `ImportError: cannot import name 'build' from 'codicefiscale'`.
  The wizard and the tests have been updated to the new API
  (`codicefiscale.encode` / `codicefiscale.is_valid`).
