from .template import Source
from iexfinance.stocks import get_historical_data

class Iex(Source):
    """
    Class representing the connection to the IEXCloud platform.
    It inherits from the Source class in template.py,
    <stt_stock_data_service.download_sources.template.Source>.

    functions:
    get_stocks_data(ticker_symbol, start, end=None, close_only=False)
    get_symbols()
    """
    @staticmethod
    def get_historical_data(ticker_symbols, start, end=None, close_only=False):
        """
        Downloads historical stock

        get_historical_data(ticker_symbol, start, end=None, close_only=False)
        """
        # Run error checking from Source class
        Source.get_historical_data(ticker_symbols, start, end, close_only)

        # if no end is specified
        if end == None:
            there_is_only_one_date_listed = True
        else:
            there_is_only_one_date_listed = False

        for ticker_symbols in ticker_symbols:
            pass
