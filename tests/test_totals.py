"""Invoice total contract: one discount percent per line.

Run from the repository root:  python3 -m pytest -q
"""
from ledger import invoice_total


def test_empty_invoice_is_zero():
    assert invoice_total([]) == 0.0


def test_single_line_no_discount():
    # (price, qty, discount_percent)
    assert invoice_total([(10.0, 2, 0)]) == 20.0


def test_discount_percent_applies_to_line():
    # 2 x 10.00 = 20.00, 10% off -> 18.00
    assert invoice_total([(10.0, 2, 10)]) == 18.0


def test_discount_on_every_line():
    # 10.00 at 10% off -> 9.00; 20.00 at 50% off -> 10.00
    assert invoice_total([(10.0, 1, 10), (20.0, 1, 50)]) == 19.0


def test_discount_rounds_to_cents():
    # 3 x 3.33 = 9.99, 10% off -> 8.991 -> 8.99
    assert invoice_total([(3.33, 3, 10)]) == 8.99


def test_hundred_percent_discount_lines_to_zero():
    assert invoice_total([(5.0, 4, 100), (5.0, 4, 0)]) == 20.0
