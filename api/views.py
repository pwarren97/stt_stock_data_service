from django.http import HttpResponse
from django.views import View
from datetime import datetime

import json

from .download_sources.template import Source
source = Source.import_source()

# Create your views here.
class HistoricalDataOneParameter(View):
    def get(self, request, ticker_symbols, year, month, day):
        close_only = True
        validate_ticker_symbols(ticker_symbols)
        validate_date(year, month, day)

        response = HttpResponse()

        date = datetime(year, month, day)

        # Do work
        data = dict()
        # ticker_symbols = request.ticker_symbols.split(',')
        ticker_symbols = parse_ticker_symbols(ticker_symbols)

        data = source.get_historical_data(ticker_symbols, date, close_only=close_only)
        response.content = json.dumps(data)
        return response

class HistoricalDataTwoParameters(View):
    def get(self, request, ticker_symbols, start_year, start_month, start_day, end_year, end_month, end_day):
        close_only = True
        validate_ticker_symbols(ticker_symbols)
        validate_date(start_year, start_month, start_day)
        validate_date(end_year, end_month, end_day)

        response = HttpResponse()

        start_date = datetime(start_year, start_month, start_day)
        end_date = datetime(end_year, end_month, end_day)

        data = dict()
        ticker_symbols = parse_ticker_symbols(ticker_symbols)

        data = source.get_historical_data(ticker_symbols, start_date, end_date, close_only=close_only)
        response.content = json.dumps(data)
        return response

class TickerSymbols(View):
    def get(self, request):
        response = HttpResponse()
        response.content = 'Hello world'

        # Uncomment if get_ticker_symbols is implemented
        try:
            data = source.get_ticker_symbols()
            response.content = json.dumps(data)
        except:
            msg = 'Could not run get_ticker_symbols() using this download source, NotImplementedError'
            print(msg)
            response.content = msg
        return response

def parse_date(date_string):
    is_valid = validate_date(date_string)

    if is_valid:
        year = int(date_string[:4])
        month = int(date_string[4:6])
        day = int(date_string[6:])
        return datetime(year, month, day)

def parse_ticker_symbols(ticker_symbols_string):
    return ticker_symbols_string.split(',')

def validate_ticker_symbols(ticker_symbols):
    pass

def validate_date(year, month, day):
    pass
