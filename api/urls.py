from django.urls import path, include
from . import views

urlpatterns = [
    # Data Format:
    # Comma separated list for ticker_symbols (using URL encoding for commas)
    path('historical-data/ticker-symbols/<str:ticker_symbols>/date/<str:date>', views.HistoricalData.as_view(), name='historical data'),
    path('historical-data/ticker-symbols/<str:ticker_symbols>/start_date/<str:start_date>/end_date/<str:end_date>', views.HistoricalData.as_view(), name='historical data'),

    path('ticker-symbols/', views.TickerSymbols.as_view(), name='ticker symbols')
]
