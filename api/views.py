from django.http import HttpResponse
from django.views import View

import json

from .download_sources.template import Source
source = Source.import_source()

# Create your views here.
class HistoricalData(View):
    def get(self, request):
        response = HttpResponse()

        # Do work
        data = dict()
        ticker_symbols = request.ticker_symbols.split(',')
        for ticker_symbol in ticker_symbols:
            info = source.get_historical_data()
            data[ticker_symbol] = info

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
