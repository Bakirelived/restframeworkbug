from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from restbugapp.views import *

router = DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/publisher/$', PublisherList.as_view()),
    url(r'^api/publisher/(?P<pk>[0-9]+)/$', PublisherDetail.as_view()),
]