from appname import views
from appname.views import PersonViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

from django.conf.urls import url, include

router = DefaultRouter()
router.register(r'person', PersonViewSet, base_name='')
router.register(r'', UserViewSet, base_name='')

urlpatterns = [
    url('test/', views.Test.as_view()),
    url('', include(router.urls))

]
