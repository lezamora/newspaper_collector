import datetime
import logging

logger = logging.getLogger(__name__)


def get_date(s_date):
    date_patterns = ['%d-%m-%Y', '%Y%m%d']

    for pattern in date_patterns:
        try:
            return datetime.datetime.strptime(s_date, pattern).date()
        except:
            logger.info('Incorrect format.')
