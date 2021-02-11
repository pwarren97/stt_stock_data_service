from abc import ABC
from datetime import datetime

class Source(ABC):
    available_functions = ['get_historical_data', 'get_ticker_symbols', 'get_current_price']

    @staticmethod
    def get_historical_data(ticker_symbols, start, end=None, close_only=False):
        """
        Returns historical stock data from the start date (start parameter)
        to the end date (end parameter). If end is not specified, it will only
        return data corresponding to the single date.
        The ticker_symbols must be passed in the form of a list of strings,
        and the close_only parameter specifies whether or not to return all
        price data for a day or just the close price.

        Data returned should be as follows, a dictionary to be turned into a JSON
        object. Details listed in docs/interface.md

        """
        # Force all the types to be appropriate
        if not isinstance(ticker_symbols, list):
            raise TypeError("ticker_symbol must be a list.")
        elif not isinstance(start, datetime):
            raise TypeError("start must be a datetime.date object.")
        elif not isinstance(end, datetime) and not end == None:
            raise TypeError("end must be a datetime.date object.")

        for item in ticker_symbols:
            if not isinstance(item, str):
                raise TypeError("An item in ticker_symbol is not a string.")

        if not end == None and not start < end:
            raise ValueError("The start needs to come before the end.")

        return None

    @staticmethod
    def get_ticker_symbols():
        """
        Returns all ticker symbols, company names, associated exchange(s), etc.
        """
        pass

    @staticmethod
    def get_current_price():
        """
        Returns current price
        """
        pass

    @staticmethod
    def import_source():
        from . import settings

        if settings.DOWNLOAD_SOURCE == 'iex':
            from .iex import Iex as source
        else:
            raise ValueError('Need a proper download source. Set it in stt_stock_data_service.stt_stock_data_service.settings.py.')
