from django.urls import path, include
from . import views

urlpatterns = [
    # Data Format:
    # Comma separated list for ticker_symbols (using URL encoding for commas)
    path('historical-data/<str:start_date>/<str:ticker_symbols>', views.HistoricalData.as_view(), name='historical data'),
    path('historical-data/<str:start_date>-<str:end_date>/<str:ticker_symbols>', views.HistoricalData.as_view(), name='historical data'),

    path('ticker-symbols/', views.TickerSymbols.as_view(), name='ticker symbols')
]
