from rest_framework import serializers
from .models import Friend

class FriendSerializer(serializers.ModelSerializer):
    # リクエストユーザーを自動的に使用する
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Friend
        fields = '__all__'