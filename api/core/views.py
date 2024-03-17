from rest_framework.views import APIView
from rest_framework.response import Response

from .services import PmvgDataService


class PmvgDataInsertView(APIView):
    def post(self, request):
        pmvg_data_service = PmvgDataService()

        return Response({
            "success": pmvg_data_service.insert_pmvg_data_in_database()
        })
