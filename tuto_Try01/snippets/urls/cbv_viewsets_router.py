from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter, SimpleRouter

from ..views.cbv_viewsets import SnippetViewSet

router = SimpleRouter()
router.register(r'', SnippetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
