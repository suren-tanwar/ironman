from rest_framework import viewsets
from .models import DragonMasterModel
from .serializers import DragonMasterSerializer
from rest_framework.generics import ListAPIView
from .myPaginations import myPageNumber
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class BasicViewSet(viewsets.ModelViewSet):
    queryset = DragonMasterModel.objects.all()
    serializer_class = DragonMasterSerializer
    pagination_class = myPageNumber
    # filter_backends = [DjangoFilterBackend ,SearchFilter]
    # filterset_fields =['title', 'author']
    # # filter_backends = [SearchFilter]
    # search_fields = ['^title',]
    filter_backends = [DjangoFilterBackend ,SearchFilter,OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'author']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

   
class BasicReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DragonMasterModel.objects.all()
    serializer_class = DragonMasterSerializer








    # class BasicList(ListAPIView ):
#     queryset = DragonMasterModel.objects.all()
#     serializer_class = DragonMasterSerializer
#     pagination_class = myPageNumber



     

