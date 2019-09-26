"""
Jinja filters for printing information.
"""

def wlv_datetime(value):
    """Default format for printing datetimes."""
    return value.strftime("%d/%m/%Y %H:%M:%S") if value else ""

def long_datetime(value):
    """Locale's appropriate date and time representation."""
    return value.strftime("%c") if value else ""
