# This file is a representation of the data that will be used for
# tests.py tests.
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

start_date = datetime(2021, 1, 25)
end_date = start_date + timedelta(days=2)

stock1 = 'AAPL'
stock2 = 'TSLA'

_columns = ['symbol', 'date', 'open', 'high', 'low', 'close', 'volume']
_columns_close_only = ['symbol', 'date', 'close', 'volume']



correct_test1 = np.ndarray([
    [stock1, start_date, 143.07, 145.09, 136.54, 142.92, 157611713]
])

correct_test2 = np.ndarray([
    [stock1, start_date, 142.92, 157611713]
])

correct_test3 = np.ndarray([
    [stock1, start_date, ]
])

correct_test1 = pd.DataFrame(correct_test1, columns=_columns)
correct_test2 = pd.DataFrame(correct_test2, columns=_columns_close_only)
