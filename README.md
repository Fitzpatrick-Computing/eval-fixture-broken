# ledger

Small invoicing math helpers: `ledger.line_total` prices one line and
`ledger.invoice_total` sums an invoice (price, qty, discount_percent triples)
with each line's discount applied.

## Layout

- `ledger/` — the package
- `tests/` — the test suite (these tests define the contract)

## Running the tests

From the repository root:

```
python3 -m pytest -q
```

Python >= 3.9, no third-party runtime dependencies (pytest is only needed
to run the tests).
