"""Invoicing math.

An invoice is a list of line items, each a ``(price, qty, discount_percent)``
triple. ``line_total`` prices one line; ``invoice_total`` sums the whole
invoice with each line's own discount applied.
"""


def line_total(price, qty):
    """Price for one line: ``price * qty``."""
    return price * qty


def invoice_total(items):
    """Sum an invoice, applying each line's discount to that line.

    ``items`` is an iterable of ``(price, qty, discount_percent)`` triples.
    Returns the total rounded to cents.
    """
    total = 0.0
    for price, qty, discount in items:
        base = line_total(price, qty)
        base -= base * discount / 100
        total += base
    return round(total, 2)
