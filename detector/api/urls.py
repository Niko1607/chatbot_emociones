from django.urls import path
from .views import chatbot, chat_view


urlpatterns = [
    path("chatbot/", chatbot),
    path("chat/", chat_view),
]

