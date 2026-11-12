"""Line pricing contract."""
from ledger import line_total


def test_line_total_basic():
    assert line_total(4.5, 3) == 13.5


def test_line_total_zero_qty():
    assert line_total(99.0, 0) == 0.0


def test_line_total_fractional_price():
    assert line_total(1.25, 4) == 5.0
