from django.urls import re_path
from rest_framework.routers import DefaultRouter

from goods import views
urlpatterns = [
    re_path(r'^brands/$', views.BrandListView.as_view()),
    re_path(r'^categorys/$', views.CategoryListView.as_view()),
    re_path(r'^category/(?P<pk>\d+)/$', views.CgoryListView.as_view()),
    re_path(r'^categories/brand/$', views.SKUBrandListView.as_view()),
    re_path(r'^categories/skus/$', views.SKUListView.as_view()),

]
router = DefaultRouter()
router.register('skus/search', views.SKUSearchViewSet, basename='skus_search')
urlpatterns += router.urls
