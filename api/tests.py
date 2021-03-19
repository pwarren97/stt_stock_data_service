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

        # THIS GROUPING OF TESTS MAKES SURE THAT THE FUNCTION RETURNS THE CORRECT RESULT
        # Pattern goes: 1 stock, 1 date, no close only,
        # 1 stock, 1 date, no close only,
        # 1 stock, 1 date, close only(=True),
        # 1 stock, 2 date, no close only,
        # 1 stock, 2 date, close only(=True),
        # etc., max out at 2 stock, 2 date, close only(=True)
        # (Think incrementing a binary number)
        #
        # 1 stock passed through
        test1 = source.get_historical_data([ test_data.stock1 ], test_data.start_date)
        test2 = source.get_historical_data([ test_data.stock1 ], test_data.start_date, close_only=True)
        test3 = source.get_historical_data([ test_data.stock1 ], test_data.start_date, test_data.end_date)
        test4 = source.get_historical_data([ test_data.stock1 ], test_data.start_date, test_data.end_date, close_only=True)
        #
        # 2 stocks passed through
        test5 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date)
        test6 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date, close_only=True)
        test7 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date, test_data.end_date)
        test8 = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date, test_data.end_date, close_only=True)
        #
        #
        # Tests
        self.assertEqual(test1, test_data.correct_test1)
        self.assertEqual(test2, test_data.correct_test2)
        self.assertEqual(test3, test_data.correct_test3)
        self.assertEqual(test4, test_data.correct_test4)
        #
        self.assertEqual(test5, test_data.correct_test5)
        self.assertEqual(test6, test_data.correct_test6)
        self.assertEqual(test7, test_data.correct_test7)
        self.assertEqual(test8, test_data.correct_test8)


        # Test to make sure that having the same date for the start date and the end date still pulls data
        test1_1 = source.get_historical_data([ test_data.stock1 ], test_data.start_date, test_data.start_date)
        self.assertEqual(test1, test1_1)


        # THIS GROUPING OF TESTS MAKES SURE THAT close_only=False IS THE SAME THING AS USING THE DEFAULT PARAMETER VALUE
        # tests to make sure that close_only=False is the same thing as leaving
        test1_F = source.get_historical_data([ test_data.stock1 ], test_data.start_date, close_only=False)
        test3_F = source.get_historical_data([ test_data.stock1 ], test_data.start_date, test_data.end_date, close_only=False)
        test5_F = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date, close_only=False)
        test7_F = source.get_historical_data([ test_data.stock1, test_data.stock2 ], test_data.start_date, test_data.end_date, close_only=False)
        #
        self.assertEqual(test1, test1_F)
        self.assertEqual(test3, test3_F)
        self.assertEqual(test5, test5_F)
        self.assertEqual(test7, test7_F)


        # THIS GROUPING OF TESTS MAKES SURE THAT THE APPROPRIATE ERROR CHECK AS PROVDED BY THE Source CLASS IS BEING USED
        # ticker_symbols has to be a string when it is not a list of strings
        with self.assertRaises(TypeError):
            temp = source.get_historical_data(123, test_data.start_date, close_only=True)
        #
        # items inside of ticker_symbols list should be strings
        with self.assertRaises(TypeError):
            temp = source.get_historical_data([ 123, 456 ], test_data.start_date, close_only=True)
        #
        # start date must be datetime object
        with self.assertRaises(TypeError):
            temp = source.get_historical_data([test_data.stock1], '2019-01-01', close_only=True)
        #
        # end date must be a datetime object
        with self.assertRaises(TypeError):
            temp = source.get_historical_data([test_data.stock1], test_data.start_date, '2019-01-01', close_only=True)
        #
        # start_date must not be in the future
        with self.assertRaises(ValueError):
            temp = source.get_historical_data([test_data.stock1], datetime.now() + timedelta(days=1), close_only=True)
        #
        # end_date must not be in the future
        with self.assertRaises(ValueError):
            temp = source.get_historical_data([test_data.stock1], test_data.start_date, datetime.now() + timedelta(days=1), close_only=True)
        #
        # end_date must be before start_date
        with self.assertRaises(ValueError):
            temp = source.get_historical_data([test_data.stock1], test_data.start_date, test_data.start_date - timedelta(days=1), close_only=True)
        #
        # the start date must come before the end date
        with self.assertRaises(ValueError):
            temp = source.get_historical_data([test_data.stock1], test_data.end_date, test_data.start_date)

    def test_get_ticker_symbols(self):
        pass

    def test_get_current_price(self):
        pass

    def test_get_news_article(self):
        pass
