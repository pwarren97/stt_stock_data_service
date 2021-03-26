from django.http import HttpResponse
from django.views import View
from .models import Stock, StockName
from datetime import datetime, timedelta

import json

from .download_sources.template import Source
source = Source.import_source()

# Error messages to be passed through through to the response
invalid_ticker_symbols_msg = "The ticker-symbol variable must be in a comma separated list."
_invalid_date_msg = " must be in the form year/month/day."
invalid_start_date_msg = "The start date" + _invalid_date_msg
invalid_end_date_msg = "The end date" + _invalid_date_msg
invalid_close_only_msg = "The close-only variable was not set correctly. It must be true or false."

# Create your views here.
class HistoricalDataOneParameter(View):
    def get(self, request, ticker_symbols, year, month, day, close_only):
        response = HttpResponse()
        ticker_symbols = parse_ticker_symbols(ticker_symbols)
        close_only = close_only.lower()

        valid, err_msg = validate_hist_data_one_param(ticker_symbols, year, month, day, close_only)
        if not valid:
            response.content = json.dumps(err_msg)
            return response

        # have to validate close_only before you to make into a boolean
        close_only = close_only == "true"

        date = datetime(year, month, day)

        # get the data
        data = dict()
        data = pull_historical_data(ticker_symbols, date, date, close_only)

        response.content = json.dumps(data)
        return response

class HistoricalDataTwoParameters(View):
    def get(self, request, ticker_symbols, start_year, start_month, start_day, end_year, end_month, end_day, close_only):
        response = HttpResponse()
        ticker_symbols = parse_ticker_symbols(ticker_symbols)
        close_only = close_only.lower()

        valid, err_msg = validate_hist_data_two_params(ticker_symbols, start_year, start_month, start_day, end_year, end_month, end_day, close_only)
        if not valid:
            response.content = json.dumps(err_msg)
            return response

        # have to validate close_only before you to make into a boolean
        close_only = close_only == "true"

        start_date = datetime(start_year, start_month, start_day)
        end_date = datetime(end_year, end_month, end_day)

        # get the data
        data = dict()
        data = pull_historical_data(ticker_symbols, start_date, end_date, close_only)

        response.content = json.dumps(data)
        return response

class CurrentPrice(View):
    def get(self, ticker_symbols):
        pass

class TickerSymbols(View):
    def get(self, request):
        response = HttpResponse()

        try:
            data = source.get_ticker_symbols()
            response.content = json.dumps(data)
        except:
            msg = 'Could not run get ticker symbols using this download source.'
            print(msg)
            response.content = msg
        return response

class NewsArticles(View):
    def get(self, ticker_symbols, start_date, end_date):
        pass


def parse_date(date_string):
    is_valid = validate_date(date_string)

    if is_valid:
        year = int(date_string[:4])
        month = int(date_string[4:6])
        day = int(date_string[6:])
        return datetime(year, month, day)

# Pulls data from download source and database
# Noninclusive of second date
def pull_historical_data(ticker_symbols, start_date, end_date, close_only):
    for ticker_symbol in ticker_symbols:
        stock = Stock.objects.filter(ticker_symbol)
    data = source.get_historical_data(ticker_symbols, start_date, end_date, close_only)
    return data


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
