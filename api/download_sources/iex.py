from .template import Source
from iexfinance.stocks import get_historical_data
from .settings import IEX_TOKEN
import pandas as pd

class Iex(Source):
    """
    Class representing the connection to the IEXCloud platform.
    It inherits from the Source class in template.py,
    <stt_stock_data_service.download_sources.template.Source>.

    functions:
    get_historical_data(ticker_symbol, start, end=None, close_only=False)
    get_ticker_symbols()
    """

    self.available_functions = ['get_historical_data']

    @staticmethod
    def get_historical_data(ticker_symbols, start, end=None, close_only=False):
        """
        Downloads historical stock

        get_historical_data(ticker_symbols, start, end=None, close_only=False)
        """
        # Run error checking from Source class
        Source.get_historical_data(ticker_symbols, start, end, close_only)

        stock_data = get_historical_data(ticker_symbols, start, end, close_only=close_only)
        return stock_data

    @staticmethod
    def get_ticker_symbols():
        # no need to call superclass function

        raise NotImplementedError()

    @staticemethod
    def get_current_price(ticker_symbols):

        raise NotImplementedError
