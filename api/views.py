from django.http import HttpResponse
from django.views import View
from datetime import datetime, timedelta
from api.lib.utils import helpers
from api.lib.utils.input_validation import UrlInputValids

import json

# Create your views here.
class HistoricalDataOneParameter(View):
    def get(self, request, ticker_symbols, year, month, day, close_only):
        response = HttpResponse()
        ticker_symbols = helpers.parse_ticker_symbols(ticker_symbols)
        close_only = close_only.lower()

        valid, err_msg = UrlInputValids.validate_hist_data_one_param(ticker_symbols, year, month, day, close_only)
        if not valid:
            response.content = json.dumps(err_msg)
            return response

        # have to validate close_only before you to make into a boolean
        close_only = close_only == "true"

        date = datetime(year, month, day)

        # get the data
        data = dict()
        data = helpers.pull_historical_data(ticker_symbols, date, date, close_only)

        response.content = json.dumps(data)
        return response

class HistoricalDataTwoParameters(View):
    def get(self, request, ticker_symbols, start_year, start_month, start_day, end_year, end_month, end_day, close_only):
        response = HttpResponse()
        ticker_symbols = helpers.parse_ticker_symbols(ticker_symbols)
        close_only = close_only.lower()

        valid, err_msg = UrlInputValids.validate_hist_data_two_params(ticker_symbols, start_year, start_month, start_day, end_year, end_month, end_day, close_only)
        if not valid:
            response.content = json.dumps(err_msg)
            return response

        # have to validate close_only before you to make into a boolean
        close_only = close_only == "true"

        start_date = datetime(start_year, start_month, start_day)
        end_date = datetime(end_year, end_month, end_day)

        # get the data
        data = dict()
        data = helpers.pull_historical_data(ticker_symbols, start_date, end_date, close_only)

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
