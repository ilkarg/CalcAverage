from rest_framework.views import APIView
from core.usecase.average.get.us_get_average import UsGetAverage

class ViewAverage(APIView):
    def get(self, request):
        return UsGetAverage.execute(request)
