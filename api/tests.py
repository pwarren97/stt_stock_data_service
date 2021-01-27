from django.test import TestCase
from datetime import datetime, timedelta
import test_data
from api.download_sources.template.Source import import_source

source = import_source()

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
        # 1 stock, 1 date, close only,
        # 1 stock, 2 date, no close only,
        # etc., max out at 2 stock, 2 date, close only
        # (Think incrementing a binary number)

        # 1 stock passed through
        test1 = source.get_historical_data([ test_data.stock1 ], test_data.start_date)
        test2 = source.get_historical_data([ test_data.stock1 ], test_data.start_date, close_only=True)
        test3 = source.get_historical_data([ test_data.stock1 ], test_data.start_date, test_data.end_date, close_only=False)
        test4 = source.get_historical_data([ test_data.stock1 ], test_data.start_date, test_data.end_date, close_only=True)

        # 2 stocks passed through
        test5 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date)
        test6 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date, close_only=True)
        test7 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date, test_data.end_date, close_only=False)
        test8 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date, test_data.end_date, close_only=True)

        self.assertEqual(test1, )

    def test_get_ticker_symbols(self):
        pass
