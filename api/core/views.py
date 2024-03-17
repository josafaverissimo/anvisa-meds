from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import PmvgDataService


class PmvgDataInsertView(APIView):
    def post(self, request):
        pmvg_data_service = PmvgDataService()

        success_store_pmvg_data_in_data_base = pmvg_data_service.insert_pmvg_data_in_database()
        response_http_status = status.HTTP_201_CREATED if pmvg_data_service else status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(
            data={"success": success_store_pmvg_data_in_data_base},
            status=response_http_status
        )
