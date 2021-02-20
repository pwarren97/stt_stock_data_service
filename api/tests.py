from django.test import TestCase
from datetime import datetime, timedelta
from . import test_data
from api.download_sources.template import Source

source = Source.import_source()

# Create your tests here.
class DownloadSourceTestCase(TestCase):
    """
    All Tests assume internet connection is sound, that the token for the
    download source is valid, and that
    """
    def setUp(self):
        pass

    def test_get_historical_data(self):

        # Pattern goes: 1 stock, 1 date, no close only,
        # 1 stock, 1 date, no close only,
        # 1 stock, 1 date, close only(=True),
        # 1 stock, 2 date, no close only,
        # 1 stock, 2 date, close only(=True),
        # etc., max out at 2 stock, 2 date, close only(=True)
        # (Think incrementing a binary number)

        # 1 stock passed through
        test1 = source.get_historical_data([ test_data.stock1 ], test_data.start_date)
        test2 = source.get_historical_data([ test_data.stock1 ], test_data.start_date, close_only=True)
        test3 = source.get_historical_data([ test_data.stock1 ], test_data.start_date, test_data.end_date)
        test4 = source.get_historical_data([ test_data.stock1 ], test_data.start_date, test_data.end_date, close_only=True)
        # # 2 stocks passed through
        #
        test5 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date)
        test6 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date, close_only=True)
        test7 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date, test_data.end_date)
        test8 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date, test_data.end_date, close_only=True)
        #
        #
        # # Tests
        self.assertEqual(test1, test_data.correct_test1)
        self.assertEqual(test2, test_data.correct_test2)
        self.assertEqual(test3, test_data.correct_test3)
        self.assertEqual(test4, test_data.correct_test4)
        #
        self.assertEqual(test5, test_data.correct_test5)
        self.assertEqual(test6, test_data.correct_test6)
        self.assertEqual(test7, test_data.correct_test7)
        self.assertEqual(test8, test_data.correct_test8)


    def test_get_ticker_symbols(self):
        pass

    def test_get_current_price(self):
        pass
