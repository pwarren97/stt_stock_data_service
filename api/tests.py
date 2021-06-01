from django.test import TestCase
from datetime import datetime, timedelta
from . import test_data
from api.models import Stock, StockName
from api.lib.download_sources.template import Source
from api.lib.utils import helpers

from unittest.mock import patch

source = Source.import_source()

class DownloadSourceTestCase(TestCase):
    """
    All Tests assume internet connection is sound, that the token for the
    download source is valid, and that
    """

    def test_get_historical_data(self):

        # THIS GROUPING OF TESTS MAKES SURE THAT THE FUNCTION RETURNS THE CORRECT RESULT
        ticker_symbols = [ test_data.stock1, test_data.stock2 ]
        start_date = test_data.start_date
        end_date = test_data.end_date
        close_only_options = [ False, True ]

        tests = []
        for num_of_tickers in [1, 2]:
            for num_of_dates in [1, 2]:
                for close in close_only_options:
                    if num_of_tickers == 1:
                        if num_of_dates == 1:
                            tests.append(source.get_historical_data( [ ticker_symbols[0] ], start_date, close_only=close))
                        else:
                            tests.append(source.get_historical_data( [ ticker_symbols[0] ], start_date, end_date, close_only=close))
                    else:
                        if num_of_dates == 1:
                            tests.append(source.get_historical_data( [ ticker_symbols[0], ticker_symbols[1] ], start_date, close_only=close))
                        else:
                            tests.append(source.get_historical_data( [ ticker_symbols[0], ticker_symbols[1] ], start_date, end_date, close_only=close))
        #
        # Run above tests
        for idx in range(len(tests)):
            self.assertEqual(tests[idx], test_data.correct_tests[idx])
        #
        #
        # Allow stock to be passed through as a string
        test_string = source.get_historical_data(ticker_symbols[0], start_date)
        self.assertEqual(test_string, test_data.correct_test1)

        # Test to make sure that having the same date for the start date and the end date still pulls data
        test_same_dates = source.get_historical_data([ ticker_symbols[0] ], start_date, start_date)
        self.assertEqual(tests[0], test_same_dates)

        # Test to make sure the default for close_only = False
        test_default_False = source.get_historical_data([ ticker_symbols[0] ], start_date)
        self.assertEqual(test_default_False, tests[0])


        # THIS GROUPING OF TESTS MAKES SURE THAT THE APPROPRIATE ERROR CHECK AS PROVDED BY THE Source CLASS IS BEING USED
        # ticker_symbols has to be a string when it is not a list of strings
        with self.assertRaises(TypeError):
            temp = source.get_historical_data(123, start_date, close_only=True)
        #
        # items inside of ticker_symbols list should be strings
        with self.assertRaises(TypeError):
            temp = source.get_historical_data([ 123, 456 ], start_date, close_only=True)
        #
        # start date must be datetime object
        with self.assertRaises(TypeError):
            temp = source.get_historical_data([ ticker_symbols[0] ], '2019-01-01', close_only=True)
        #
        # end date must be a datetime object
        with self.assertRaises(TypeError):
            temp = source.get_historical_data([ ticker_symbols[0] ], start_date, '2019-01-01', close_only=True)
        #
        # start_date must not be in the future
        with self.assertRaises(ValueError):
            temp = source.get_historical_data([ ticker_symbols[0] ], datetime.now() + timedelta(days=1), close_only=True)
        #
        # end_date must not be in the future
        with self.assertRaises(ValueError):
            temp = source.get_historical_data([ ticker_symbols[0] ], start_date, datetime.now() + timedelta(days=1), close_only=True)
        #
        # end_date must be before start_date
        with self.assertRaises(ValueError):
            temp = source.get_historical_data([ ticker_symbols[0] ], start_date, start_date - timedelta(days=1), close_only=True)
        #
        # the start date must come before the end date
        with self.assertRaises(ValueError):
            temp = source.get_historical_data([ ticker_symbols[0] ], end_date, start_date)

    def test_get_ticker_symbols(self):
        pass

    def test_get_current_price(self):
        pass

    def test_get_news_article(self):
        pass

class HelpersTestCase(TestCase):
    """
    All tests are related to the helper functions in helpers.py
    """
    @patch('api.lib.utils.helpers.Stock')
    def test_pull_historical_data_download_source_only(self, mock_stock):
        # Set up
        stock1 = test_data.stock1
        stock2 = test_data.stock2
        start_date = test_data.start_date
        end_date = test_data.end_date

        mock_stock.objects.filter.return_value = []

        # Requests
        request1 = helpers.pull_historical_data([stock1], start_date, close_only=True)
        request2 = helpers.pull_historical_data([stock1], start_date, end_date, close_only=True)

        request3 = helpers.pull_historical_data([stock1], start_date, close_only=False)
        request4 = helpers.pull_historical_data([stock1], start_date, end_date, close_only=False)

        request5 = helpers.pull_historical_data([stock1, stock2], start_date, close_only=True)
        request6 = helpers.pull_historical_data([stock1, stock2], start_date, end_date, close_only=True)

        request7 = helpers.pull_historical_data([stock1, stock2], start_date, close_only=False)
        request8 = helpers.pull_historical_data([stock1, stock2], start_date, end_date, close_only=False)

        request_close_only_defaults_false = helpers.pull_historical_data([stock1], start_date)


        # Tests
        self.assertEqual(request1, test_data.correct_test2)
        self.assertEqual(request2, test_data.correct_test4)

        self.assertEqual(request3, test_data.correct_test1)
        self.assertEqual(request4, test_data.correct_test3)

        self.assertEqual(request5, test_data.correct_test6)
        self.assertEqual(request6, test_data.correct_test8)

        self.assertEqual(request7, test_data.correct_test5)
        self.assertEqual(request8, test_data.correct_test7)

        # tests whether close_only's default value is false
        self.assertEqual(request3, request_close_only_defaults_false)


    @patch('api.lib.utils.helpers.Stock')
    def test_pull_historical_data_db_only(self, mock_stock):
        # Set up
        stock1 = test_data.stock1
        stock2 = test_data.stock2
        start_date = test_data.start_date
        end_date = test_data.end_date

        ### TESTS close_only=True
        mock_stock.objects.filter.return_value = [
            Stock(symbol=stock1,
                date=date1,
                close=test_data.stock_data[stock1][start_date].close,
                volume=test_data.stock_data[stock1][start_date].volume),
            Stock(symbol=stock1,
                date=date2,
                close=test_data.stock_data[stock1][end_date].close,
                volume=test_data.stock_data[stock1][end_date].volume)
        ]

        # Requests
        request1 = helpers.pull_historical_data([stock1], start_date, end_date)

        ### TESTS close_only=False
        mock_stock.objects.filter.return_value = [
            Stock(symbol=stock1,
                date=date1,
                open=test_data.stock_data[stock1][start_date].open,
                high=test_data.stock_data[stock1][start_date].high,
                low=test_data.stock_data[stock1][start_date].low,
                close=test_data.stock_data[stock1][start_date].close,
                volume=test_data.stock_data[stock1][start_date].volume),
            Stock(symbol=stock1,
                date=date2,
                open=test_data.stock_data[stock1][end_date].open,
                high=test_data.stock_data[stock1][end_date].high,
                low=test_data.stock_data[stock1][end_date].low,
                close=test_data.stock_data[stock1][end_date].close,
                volume=test_data.stock_data[stock1][end_date].volume)
        ]

        # Requests
        request1 = helpers.pull_historical_data([stock1], start_date, close_only=True)
        request2 = helpers.pull_historical_data([stock1], start_date, end_date, close_only=True)

        request3 = helpers.pull_historical_data([stock1], start_date, close_only=False)
        request4 = helpers.pull_historical_data([stock1], start_date, end_date, close_only=False)
