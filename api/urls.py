from django.urls import path, include
from . import views

urlpatterns = [
    # Data Format:
    # Comma separated list for ticker_symbols (using URL encoding for commas)
    path('historical-data/ticker-symbols/<str:ticker_symbols>/date/<int:year>/<int:month>/<int:day>/', views.HistoricalDataOneParameter.as_view(), name='historical data'),
    path('historical-data/ticker-symbols/<str:ticker_symbols>/start-date/<int:start_year>/<int:start_month>/<int:start_day>/end-date/<int:end_year>/<int:end_month>/<int:end_day>/', views.HistoricalDataTwoParameters.as_view(), name='historical data'),

    path('ticker-symbols/', views.TickerSymbols.as_view(), name='ticker symbols')
]
