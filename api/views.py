from django.http import HttpResponse
from django.views import View

# Create your views here.
class HistoricalData(View):
    def get(self, request):
        response = HttpResponse()

        # Do work
        return response

class Symbols(View):
    def get(self, request):
        response = HttpResponse()
        response.content = 'Hello world'
        
        # Do work
        return response
