from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from restbugapp.views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]