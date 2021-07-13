from django.urls import re_path
from feedback import views
urlpatterns = [
    re_path(r'^feedback/$', views.FeedbackView.as_view()),
]