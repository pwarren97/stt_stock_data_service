from django.http import HttpResponse
from django.views import View

import json

# Import source

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

class Symbols(View):
    def get(self, request):
        response = HttpResponse()
        response.content = 'Hello world'

        # Do work
        return response
