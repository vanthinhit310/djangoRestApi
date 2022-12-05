from django.urls import path
from hello.views import HelloView

urlpatterns = [
    path("", HelloView.as_view()),
]
