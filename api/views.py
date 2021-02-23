from django.http import HttpResponse
from django.views import View
from datetime import datetime

import json

from .download_sources.template import Source
source = Source.import_source()

# Create your views here.
class HistoricalData(View):
    def get(self, request, ticker_symbols, date):
        response = HttpResponse()

        date = parse_date(date)

        # Do work
        data = dict()
        # ticker_symbols = request.ticker_symbols.split(',')
        ticker_symbols = [ ticker_symbols ]

        close_only = True
        # if end_date:
        #     data = source.get_historical_data(ticker_symbols, date, end_date, close_only=close_only)
        # else:
        data = source.get_historical_data(ticker_symbols, date, close_only=close_only)
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


def validate_ticker_symbols(ticker_symbols):
    pass

def validate_date(date_string):
    return True
