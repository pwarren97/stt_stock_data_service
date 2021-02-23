from .template import Source
from iexfinance.stocks import get_historical_data
from .settings import IEX_TOKEN

class Iex(Source):
    """
    Class representing the connection to the IEXCloud platform.
    It inherits from the Source class in template.py,
    <stt_stock_data_service.download_sources.template.Source>.

    functions:
    get_historical_data(ticker_symbol, start, end=None, close_only=False)
    get_ticker_symbols()
    """

    available_functions = ['get_historical_data']

    @staticmethod
    def get_historical_data(ticker_symbols, start, end=None, close_only=False):
        """
        Downloads historical stock

        get_historical_data(ticker_symbols, start, end=None, close_only=False)
        """
        # Run error checking from Source class
        Source.get_historical_data(ticker_symbols, start, end, close_only)

        stock_data = dict()
        if len(ticker_symbols) == 1:
            stock_data[ticker_symbols[0].upper()] = get_historical_data(ticker_symbols, start, end, output_format='json', token=IEX_TOKEN, close_only=close_only)
        else:
            # the iexfinance function already returns a dict in the appropriate format
            stock_data = get_historical_data(ticker_symbols, start, end, output_format='json', token=IEX_TOKEN, close_only=close_only)
        print(stock_data)
        return stock_data

    @staticmethod
    def get_ticker_symbols():
        # no need to call superclass function

        raise NotImplementedError()

    @staticmethod
    def get_current_price(ticker_symbols):

        raise NotImplementedError
