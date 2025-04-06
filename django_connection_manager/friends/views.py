from .models import Friend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import FriendSerializer

class FriendListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # ログインユーザーに紐づく友達一覧を取得
        friends = Friend.objects.filter(user=request.user)
        serializer = FriendSerializer(friends, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # 新しい友人を追加
        serializer = FriendSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FriendDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Friend.objects.get(pk=pk, user=user)
        except Friend.DoesNotExist:
            return None

    def get(self, request, pk):
        friend = self.get_object(pk, request.user)
        if friend is None:
            return Response({"error": "Friend not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = FriendSerializer(friend, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        friend = self.get_object(pk, request.user)
        if friend is None:
            return Response({"error": "Friend not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = FriendSerializer(friend, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        friend = self.get_object(pk, request.user)
        if friend is None:
            return Response({"error": "Friend not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = FriendSerializer(friend, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        friend = self.get_object(pk, request.user)
        if friend is None:
            return Response({"error": "Friend not found"}, status=status.HTTP_404_NOT_FOUND)
        friend.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)