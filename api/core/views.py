from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import PmvgDataService
from .repositories import LaboratoriesMedsRepository


class PmvgDataInsertView(APIView):
    def post(self, request):
        pmvg_data_service = PmvgDataService()

        success_store_pmvg_data_in_data_base = pmvg_data_service.insert_pmvg_data_in_database()
        response_http_status: int

        if success_store_pmvg_data_in_data_base:
            response_http_status = status.HTTP_201_CREATED
        else:
            response_http_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(
            data={"success": success_store_pmvg_data_in_data_base},
            status=response_http_status
        )


class MedsView(APIView):
    def get(self, request):
        FIRST_PAGE = 1

        laboratories_meds_repository = LaboratoriesMedsRepository()
        page = int(request.GET.get('page', FIRST_PAGE))
        page = page if page >= FIRST_PAGE else FIRST_PAGE

        data = laboratories_meds_repository.get_by_page(page)
        response_http_status = status.HTTP_200_OK if len(data['data']) > 0 else status.HTTP_204_NO_CONTENT

        return Response(
            data=data,
            status=response_http_status
        )
