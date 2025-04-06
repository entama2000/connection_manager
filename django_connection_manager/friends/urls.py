from django.urls import path
from .views import FriendListCreateAPIView, FriendDetailAPIView

app_name = "friends"  # 追加

urlpatterns = [
    path('', FriendListCreateAPIView.as_view(), name='friend-list-create'),
    path('<int:pk>/', FriendDetailAPIView.as_view(), name='friend-detail'),
]