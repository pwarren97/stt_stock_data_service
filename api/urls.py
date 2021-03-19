from django.urls import path, include
from . import views

urlpatterns = [
    # Data Format:
    # Comma separated list for ticker_symbols (using URL encoding for commas)
    path('historical-data/ticker-symbols/<str:ticker_symbols>/date/<int:year>/<int:month>/<int:day>/close-only=<str:close_only>', views.HistoricalDataOneParameter.as_view(), name='historical data'),
    path('historical-data/ticker-symbols/<str:ticker_symbols>/start-date/<int:start_year>/<int:start_month>/<int:start_day>/end-date/<int:end_year>/<int:end_month>/<int:end_day>/close-only=<str:close_only>', views.HistoricalDataTwoParameters.as_view(), name='historical data'),
    path('current-price/ticker-symbols/<str:ticker_symbols>/', views.CurrentPrice.as_view(), name='current price'),

    path('ticker-symbols/', views.TickerSymbols.as_view(), name='ticker symbols'),
    path('news-articles/ticker_symbols/<str:ticker_symbols>/start-date/<str:start_date>/end-date/<str:end_date>', views.CurrentPrice.as_view(), name='news article'),
]
