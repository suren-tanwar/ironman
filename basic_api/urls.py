from django.conf.urls import url
from rest_framework import routers
from django.urls import include, path
from .views import BasicReadOnlyModelViewSet , BasicViewSet
# from . import views
router = routers.DefaultRouter()
router.register(r'books',BasicViewSet , basename='books')
router.register(r'get-books',BasicReadOnlyModelViewSet , basename='get-books')
urlpatterns = router.urls
# urlpatterns = [
#     path('books/', views.BasicList.as_view()),
    
# ]

# urlpatterns = [
#aisa bhi ho skta h     # path('', include(router.urls)),
#     # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#     path('books/' ,BasicAPIView.as_view())
# ]

# urlpatterns = [
#     url('books/', BasicViewSet),
# ]
# urlpatterns += router.urls