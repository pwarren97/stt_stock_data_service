# This file is a representation of the data that will be used for
# tests.py tests.
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

start_date = datetime(2021, 1, 25)
end_date = start_date + timedelta(days=1)

stock1 = 'AAPL'
stock2 = 'TSLA'

# stock2_close1 = 880.8
# stock2_volume1 = 41173397

date1 = str(start_date.date())
date2 = str(end_date.date())
# _columns = ['symbol', 'date', 'open', 'high', 'low', 'close', 'volume']
# _columns_close_only = ['symbol', 'date', 'close', 'volume']

stock_data = {
    stock1: {
        date1: {
            "open": 143.07,
            "high": 145.09,
            "low": 136.54,
            "close": 142.92,
            "volume": 157611713
        },
        date2: {
            "open": 143.6,
            "high": 144.3,
            "low": 141.37,
            "close": 143.16,
            "volume": 98390555
        }
    },
    stock2: {
        date1: {
            "open": 855.0,
            "high": 900.4,
            "low": 838.8201,
            "close": 880.8,
            "volume": 41173397
        },
        date2: {
            "open": 891.38,
            "high": 895.9,
            "low": 871.6,
            "close": 883.09,
            "volume": 23131603
        }
    }
}

# 1 Date
# close_only = False
correct_test1 = {
    stock1: {
        date1: {
            "open":   stock_data[ stock1 ][ date1 ][ 'open' ],
            "high":   stock_data[ stock1 ][ date1 ][ 'high' ],
            "low":    stock_data[ stock1 ][ date1 ][ 'low' ],
            "close":  stock_data[ stock1 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date1 ][ 'volume' ]
        }
    }
}
# close_only = True
correct_test2 = {
    stock1: {
        date1: {
            "close":  stock_data[ stock1 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date1 ][ 'volume' ]
        }
    }
}

# 2 dates
# close_only = False
correct_test3 = {
    stock1: {
        date1: {
            "open":   stock_data[ stock1 ][ date1 ][ 'open' ],
            "high":   stock_data[ stock1 ][ date1 ][ 'high' ],
            "low":    stock_data[ stock1 ][ date1 ][ 'low' ],
            "close":  stock_data[ stock1 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date1 ][ 'volume' ]
        },

        date2: {
            "open":   stock_data[ stock1 ][ date2 ][ 'open' ],
            "high":   stock_data[ stock1 ][ date2 ][ 'high' ],
            "low":    stock_data[ stock1 ][ date2 ][ 'low' ],
            "close":  stock_data[ stock1 ][ date2 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date2 ][ 'volume' ]
        }
    }
}

# close_only = True
correct_test4 = {
    stock1: {
        date1: {
            "close":  stock_data[ stock1 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date1 ][ 'volume' ]
        },

        date2: {
            "close":  stock_data[ stock1 ][ date2 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date2 ][ 'volume' ]
        }
    }
}

# 2 stocks
# 1 date
# close_only = False
correct_test5 = {
    stock1: {
        date1: {
            "open":   stock_data[ stock1 ][ date1 ][ 'open' ],
            "high":   stock_data[ stock1 ][ date1 ][ 'high' ],
            "low":    stock_data[ stock1 ][ date1 ][ 'low' ],
            "close":  stock_data[ stock1 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date1 ][ 'volume' ]
        }
    },
    stock2: {
        date1: {
            "open":   stock_data[ stock2 ][ date1 ][ 'open' ],
            "high":   stock_data[ stock2 ][ date1 ][ 'high' ],
            "low":    stock_data[ stock2 ][ date1 ][ 'low' ],
            "close":  stock_data[ stock2 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock2 ][ date1 ][ 'volume' ]
        }
    }
}
# close_only = True
correct_test6 = {
    stock1: {
        date1: {
            "close":  stock_data[ stock1 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date1 ][ 'volume' ]
        }
    },
    stock2: {
        date1: {
            "close":  stock_data[ stock2 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock2 ][ date1 ][ 'volume' ]
        }
    }
}

# 2 stocks
# 2 dates
# close_only = False
correct_test7 = {
    stock1: {
        date1: {
            "open":   stock_data[ stock1 ][ date1 ][ 'open' ],
            "high":   stock_data[ stock1 ][ date1 ][ 'high' ],
            "low":    stock_data[ stock1 ][ date1 ][ 'low' ],
            "close":  stock_data[ stock1 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date1 ][ 'volume' ]
        },
        date2: {
            "open":   stock_data[ stock1 ][ date2 ][ 'open' ],
            "high":   stock_data[ stock1 ][ date2 ][ 'high' ],
            "low":    stock_data[ stock1 ][ date2 ][ 'low' ],
            "close":  stock_data[ stock1 ][ date2 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date2 ][ 'volume' ]
        }
    },
    stock2: {
        date1: {
            "open":   stock_data[ stock2 ][ date1 ][ 'open' ],
            "high":   stock_data[ stock2 ][ date1 ][ 'high' ],
            "low":    stock_data[ stock2 ][ date1 ][ 'low' ],
            "close":  stock_data[ stock2 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock2 ][ date1 ][ 'volume' ]
        },
        date2: {
            "open":   stock_data[ stock2 ][ date2 ][ 'open' ],
            "high":   stock_data[ stock2 ][ date2 ][ 'high' ],
            "low":    stock_data[ stock2 ][ date2 ][ 'low' ],
            "close":  stock_data[ stock2 ][ date2 ][ 'close' ],
            "volume": stock_data[ stock2 ][ date2 ][ 'volume' ]
        }
    }
}

# close_only = True
correct_test8 = {
    stock1: {
        date1: {
            "close":  stock_data[ stock1 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date1 ][ 'volume' ]
        },
        date2: {
            "close":  stock_data[ stock1 ][ date2 ][ 'close' ],
            "volume": stock_data[ stock1 ][ date2 ][ 'volume' ]
        }
    },
    stock2: {
        date1: {
            "close":  stock_data[ stock2 ][ date1 ][ 'close' ],
            "volume": stock_data[ stock2 ][ date1 ][ 'volume' ]
        },
        date2: {
            "close":  stock_data[ stock2 ][ date2 ][ 'close' ],
            "volume": stock_data[ stock2 ][ date2 ][ 'volume' ]
        }
    }
}
