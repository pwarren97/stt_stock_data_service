# Input validation related functions to be used by views.py for URL paramters

class UrlInputValids:
    # Error messages to be passed through through to the response
    invalid_ticker_symbols_msg = "The ticker-symbol variable must be in a comma separated list."
    _invalid_date_msg = " must be in the form year/month/day."
    invalid_start_date_msg = "The start date" + _invalid_date_msg
    invalid_end_date_msg = "The end date" + _invalid_date_msg
    invalid_close_only_msg = "The close-only variable was not set correctly. It must be true or false."

    @staticmethod
    def validate_hist_data_one_param(ticker_symbols, year, month, day, close_only):
        valid, err_msg = UrlInputValids.validate_common_params(ticker_symbols, close_only)

        try:
            validate_date(year, month, day)
        except:
            err_msg["Error"]["date"] = _invalid_date_msg
            valid = False

            return valid, err_msg

    @staticmethod
    def validate_hist_data_two_params(ticker_symbols, start_year, start_month, start_day, end_year, end_month, end_day, close_only):
        valid, err_msg = validate_common_params(ticker_symbols, close_only)

        try:
            validate_date(start_year, start_month, start_day)
        except:
            err_msg["Error"]["start-date"] = invalid_start_date_msg

            try:
                validate_date(end_year, end_month, end_day)
            except:
                err_msg["Error"]["end-date"] =  invalid_end_date_msg
                valid = False

                return valid, err_msg

    # Validate parameters that are commmon to bother historical data validation functions
    @staticmethod
    def validate_common_params(ticker_symbols, close_only):
        err_msg = dict()
        err_msg["Error"] = dict()
        valid = True

        try:
            validate_ticker_symbols(ticker_symbols)
        except:
            err_msg["Error"]["ticker-symbols"] = invalid_ticker_symbols_msg
            valid = False

            try:
                UrlInputValids.validate_close_only(close_only)
            except ValueError:
                err_msg["Error"]["close-only"] = invalid_close_only_msg
                valid = False

                return valid, err_msg

    @staticmethod
    def validate_ticker_symbols(ticker_symbols):
        for ticker_symbol in ticker_symbols:
            if not len(ticker_symbol) == 4:
                raise ValueError()

    @staticmethod
    def validate_date(year, month, day):
        pass

    @staticmethod
    def validate_close_only(close_only):
        if not (close_only == 'true' or close_only == 'false'):
            raise ValueError()
