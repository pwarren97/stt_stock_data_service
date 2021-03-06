# Interface for stock data service
REST API

## Admin access via the web browser
The django admin panel should be passed through by routing through the Web Interface. This means an HTML web pages are the data that is returned.

## Internal Access
The data requested should be passed through via a JSON object.

GET historical-data/ticker-symbols/{ticker_symbols}/date/{year}/{month}/{day}/close-only={true/false}
    historical-data/ticker-symbols/{ticker_symbols}/start-date/{start_year}/{start_month}/{start_day}/end-date/{end_year}/{end_month}/{end_day}/
  - all of url should be lowercase
  - close-only should be a lowercase true and false, but capital letters should be excepted (e.g. TRUE, True, FALSE, etc.)
  - returns JSON object
    {
      "AAPL": {
        '2021-01-25': {
          "open": 143.07,
          "high": 145.09,
          "low": 136.54.
          "close": 142.92,
          "volume": 157611713
        },
        '2021-01-26': {
          "open": 143.60,
          "high": 144.30,
          "low": 141.37,
          "close": 143.16,
          "volume": 98390555
        }
      },
      "TSLA": {
        '2021-01-25': {
          "open": 855.00,
          "high": 900.40,
          "low": 838.82,
          "close":  880.80,
          "volume": 41173397
        },
        '2021-01-26': {
          "open": 891.38,
          "high": 895.90,
          "low": 871.60,
          "close": 883.09,
          "volume": 23131603
        }
      }
    }

    - example is as follows (using Python speak):
    {
      "AAPL": {
        str(datetime(2021, 1, 25).date()): {
          "open": 143.07,
          "high": 145.09,
          "low": 136.54.
          "close": 142.92,
          "volume": 157611713
          },
          str(datetime(2021, 1, 26).date()): {
            "open": 143.60,
            "high": 144.30,
            "low": 141.37,
            "close": 143.16,
            "volume": 98390555
          }
          },
          "TSLA": {
            str(datetime(2021, 1, 25).date()): {
              "open": 855.00,
              "high": 900.40,
              "low": 838.82,
              "close":  880.80,
              "volume": 41173397
              },
              str(datetime(2021, 1, 26).date()) {
                "open": 891.38,
                "high": 895.90,
                "low": 871.60,
                "close": 883.09,
                "volume": 23131603
              }
            }
          }
          - str(datetime(2021, 1, 25).date()) => '2021-01-25'
        - data for examples is:

        symbol       date    open    high       low   close     volume
        0   AAPL 2021-01-25  143.07  145.09  136.5400  142.92  157611713
        1   AAPL 2021-01-26  143.60  144.30  141.3700  143.16   98390555
        2   TSLA 2021-01-25  855.00  900.40  838.8201  880.80   41173397
        3   TSLA 2021-01-26  891.38  895.90  871.6000  883.09   23131603

GET current-data/ticker-symbols/{ticker_symbols}
  - pulls the current price data in JSON object
  - all of url should be lowercase
  - JSON example should look like:
    {
      "AAPL": {
        str(datetime.now()): {
          "price": 144,
          "volume": 100000
        }
      }
    }

    OR
    {
      "ticker_symbol": 'AAPL',
      "timestamp": datetime.now(),
      "price": 100.00,
      "volume": 1000000
    }
    - str(datetime().now()) => '2021-01-31'

GET ticker-symbols/
  - pulls all ticker symbols of all stocks on the exchange as well as relevant meta data

GET news-articles/ticker-symbols/{ticker_symbols}/start-date/{start_date}/end-date/{end_date}/
  - pulls all news articles corresponding to the specific ticker symbols and specific date
