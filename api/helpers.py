# This file contains functions to help the view classes
from api.models import Stock, StockName

from .download_sources.template import Source
source = Source.import_source()

# Pulls data from download source and database
# Noninclusive of second date
def pull_historical_data(ticker_symbols, start_date, end_date, close_only):
    for ticker_symbol in ticker_symbols:
        stock_name = StockName(symbol=ticker_symbol,)
        stock = Stock.objects.filter(symbol=ticker_symbol)
        data = source.get_historical_data(ticker_symbol, start_date, end_date, close_only)
        return data

def parse_date(date_string):
    is_valid = validate_date(date_string)

    if is_valid:
        year = int(date_string[:4])
        month = int(date_string[4:6])
        day = int(date_string[6:])
        return datetime(year, month, day)



def parse_ticker_symbols(ticker_symbols_string):
    return ticker_symbols_string.lower().split(',')


def validate_ticker_symbols(ticker_symbols):
    for ticker_symbol in ticker_symbols:
        if not len(ticker_symbol) == 4:
            raise ValueError()

def validate_date(year, month, day):
    pass

def validate_close_only(close_only):
    if not (close_only == 'true' or close_only == 'false'):
        raise ValueError()

def validate_common_params(ticker_symbols, close_only):
    err_msg = dict()
    err_msg["Error"] = dict()
    valid = True

    try:
        validate_ticker_symbols(ticker_symbols)
    except:
        err_msg["Error"]["ticker-symbols"] = invalid_ticker_symbols_msg
        valid = False

    try:
        validate_close_only(close_only)
    except ValueError:
        err_msg["Error"]["close-only"] = invalid_close_only_msg
        valid = False

    return valid, err_msg

def validate_hist_data_one_param(ticker_symbols, year, month, day, close_only):
    valid, err_msg = validate_common_params(ticker_symbols, close_only)

    try:
        validate_date(year, month, day)
    except:
        err_msg["Error"]["date"] = invalid_date_msg
        valid = False

    return valid, err_msg

def validate_hist_data_two_params(ticker_symbols, start_year, start_month, start_day, end_year, end_month, end_day, close_only):
    valid, err_msg = validate_common_params(ticker_symbols, close_only)

    try:
        validate_date(start_year, start_month, start_day)
    except:
        err_msg["Error"]["start-date"] = invalid_start_date_msg

    try:
        validate_date(end_year, end_month, end_day)
    except:
        err_msg["Error"]["end-date"] =  invalid_end_date_msg
        valid = False

    return valid, err_msg
