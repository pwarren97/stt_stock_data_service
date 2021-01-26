from .template import Source
from iexfinance.stocks import get_historical_data
from .settings import IEX_TOKEN

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

        if close_only:
            stock_data = pd.DataFrame(columns=["symbol", "date", "close", "volume"])
        else:
            stock_data = pd.DataFrame(columns=["symbol", "date", "open", "high", "low", "close", "volume"])

        # if no end is specified
        if end == None:
            there_is_only_one_date_listed = True
        else:
            there_is_only_one_date_listed = False

        for ticker_symbol in ticker_symbols:
            ticker_symbol = ticker_symbol.upper()

            stock_data = download_then_add_data(stock_data, ticker_symbol, start, end, output_format='pandas', close_only=close_only)

# Eliminate IEXCloud specific information for putting data in the database
def restructure_df(data_frame, ticker_symbol, close_only):
    data_frame['date'] = data_frame.index
    data_frame.index.name = None
    data_frame.index = range(len(data_frame))
    data_frame['symbol'] = ticker_symbol

    if close_only:
        data_frame = data_frame[["symbol", "date", "close", "volume"]]
    else:
        data_frame = data_frame[["symbol", "date", "open", "high", "low", "close", "volume"]]
    return data_frame

# downloads data from IEX then adds it to the relevant pd.DataFrame
def download_then_add_data(stock_df, ticker_symbol, start, end, close_only):
    temp = get_historical_data(ticker_symbol, start, end, output_format='pandas', token=IEX_TOKEN, close_only=close_only)
    temp = restructure_df(temp, ticker_symbol, close_only)
    return pd.concat([stock_df, temp], ignore_index=True)
