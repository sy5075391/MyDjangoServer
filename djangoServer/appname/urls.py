from appname import views
from appname.views import PersonViewSet
from rest_framework.routers import DefaultRouter

from django.conf.urls import url, include

router = DefaultRouter()
router.register(r'', PersonViewSet, base_name='person')

urlpatterns = [
    url('test/', views.Test.as_view()),
    url('', include(router.urls))

]
