import datetime
import pytz
from flask import current_app


def tzware_datetime():
    """
    Return a timezone aware datetime.

    :return: Datetime
    """
    return datetime.datetime.now(tz=pytz.timezone(current_app.config['TIMEZONE']))


def timedelta_months(months, compare_date=None):
    """
    Return a new datetime with a month offset applied.

    :param months: Amount of months to offset
    :type months: int
    :param compare_date: Date to compare at
    :type compare_date: date
    :return: datetime
    """
    if compare_date is None:
        compare_date = datetime.date.today()

    delta = months * 365 / 12
    compare_date_with_delta = compare_date + datetime.timedelta(delta)

    return compare_date_with_delta
