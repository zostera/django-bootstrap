from django.urls import path

from .views import HomeView, TestFormView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("test_form/", TestFormView.as_view(), name="test_form"),
]
