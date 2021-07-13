from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = []
router = SimpleRouter()
router.register(r'areas', views.AreasViewSet, basename='areas')
urlpatterns += router.urls