from django.urls import path,include
from django.urls.resolvers import URLPattern
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'details',views.Detailview)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]