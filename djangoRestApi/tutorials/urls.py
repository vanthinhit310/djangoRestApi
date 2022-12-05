from django.urls import path
from tutorials.views import TutorialView

urlpatterns = [
    path("api/tutorials", TutorialView.as_view()),
]
