# This file is a representation of the data that will be used for
# tests.py tests.
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

start_date = datetime(2021, 1, 25)
end_date = start_date + timedelta(days=2)

stock1 = 'AAPL'
stock2 = 'TSLA'

date1 = start_date.date()
date2 = end_date.date()
# _columns = ['symbol', 'date', 'open', 'high', 'low', 'close', 'volume']
# _columns_close_only = ['symbol', 'date', 'close', 'volume']


# close_only = False
correct_test1 = {
    stock1: {
        date1: {
            "open": 143.07,
            "high": 145.09,
            "low": 136.54,
            "close": 142.92,
            "volume": 157611713
        },
    }
}
# close_only = True
correct_test2 = {
    stock1: {
        date1: {
            "close": 142.92,
            "volume": 157611713
        }
    }
}




# correct_test1 = pd.DataFrame(correct_test1, columns=_columns)
# correct_test2 = pd.DataFrame(correct_test2, columns=_columns_close_only)
