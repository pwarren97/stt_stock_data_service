from abc import ABC

class Source(ABC):
    @staticmethod
    def get_historical_data(ticker_symbols, start, end=None, close_only=False):
        """
        Returns historical stock data from the start date (start parameter)
        to the end date (end parameter). If end is not specified, it will only
        return data corresponding to the single date.
        The ticker_symbols must be passed in the form of a list of strings,
        and the close_only parameter specifies whether or not to return all
        price data for a day or just the close price.

        Data returned should be as follows, a dictionary with the ticker symbols
        as the keys, and pandas objects as the values as with columns follows:

        date        | open | high | low | close | volume

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

        @staticmethod
        def get_symbols():
            """
            Returns all ticker_symbols, company names, associated exchange(s), etc.
            """
            pass
