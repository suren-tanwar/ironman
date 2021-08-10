from rest_framework.pagination import PageNumberPagination

class myPageNumber(PageNumberPagination):
 page_size = 5
 ordering =  'title'