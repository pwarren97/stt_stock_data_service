# This file contains functions to help the view classes
from api.models import Stock, StockName
from datetime import datetime, timedelta

from api.lib.download_sources.template import Source
source = Source.import_source()

# Pulls data from the database, then download source
# Inclusive of second date
def pull_historical_data(ticker_symbols, start_date, end_date=None, close_only=False):
    # Add a final stock data variable
    results = dict()

    if end_date == None:
        end_date = start_date

    for ticker_symbol in ticker_symbols:
        # Pull db data
        if start_date != end_date:
            db_data = Stock.objects.filter(symbol=ticker_symbol, date__range=(start_date, end_date))
        elif start_date <= end_date:
            db_data = Stock.objects.filter(symbol=ticker_symbol, date=start_date)
        else:
            raise ValueError("The start date must come before end date.")

        # Setup for finding missing dates
        temp_date = datetime(start_date.date().year, start_date.date().month, start_date.date().day)
        missing_dates = []
        db_data_idx = 0

        # Find the missing dates in the db_data
        while temp_date != end_date:
            if temp_date != db_data[db_data_idx]:
                missing_dates.append(temp_date)
            else:
                db_data_idx = db_data_idx + 1
            temp_date = temp_date + timedelta(days=1)


        download_data = source.get_historical_data(ticker_symbol, start_date, end_date, close_only)

    return download_data

def parse_date(date_string):
    is_valid = validate_date(date_string)

    if is_valid:
        year = int(date_string[:4])
        month = int(date_string[4:6])
        day = int(date_string[6:])
        return datetime(year, month, day)



def parse_ticker_symbols(ticker_symbols_string):
    return ticker_symbols_string.lower().split(',')
