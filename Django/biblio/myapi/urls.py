from django.urls import include, path, re_path as url
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
"""path('', include(router.urls)),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),"""
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/books$', views.books_list)
]
