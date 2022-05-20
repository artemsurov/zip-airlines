
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'airplanes', views.AitPlaneViewSet)

urlpatterns = router.urls