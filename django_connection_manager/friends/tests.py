from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Friend

class FriendAPITestCase(APITestCase):
    def setUp(self):
        # テスト用ユーザーの作成と認証
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.friend_list_url = reverse('friends:friend-list-create')

    def test_create_friend(self):
        """
        新しい友人を追加するテスト
        """
        data = {
            "first_name": "Taro",
            "last_name": "Yamada",
            "phone_number": "1234567890",
            "platform": "Twitter"
        }
        response = self.client.post(self.friend_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])

    def test_list_friends(self):
        """
        ログインユーザーに紐づく友達一覧を取得するテスト
        """
        Friend.objects.create(user=self.user, first_name="Taro", last_name="Yamada", phone_number="111", platform="Twitter")
        Friend.objects.create(user=self.user, first_name="Hanako", last_name="Suzuki", phone_number="222", platform="Facebook")
        response = self.client.get(self.friend_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        names = [(friend['first_name'], friend['last_name']) for friend in response.data]
        self.assertIn(("Taro", "Yamada"), names)
        self.assertIn(("Hanako", "Suzuki"), names)

    def test_get_friend_detail(self):
        """
        特定の友達の詳細情報取得テスト
        """
        friend = Friend.objects.create(user=self.user, first_name="Taro", last_name="Yamada", phone_number="111", platform="Twitter")
        detail_url = reverse('friends:friend-detail', kwargs={'pk': friend.pk})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], friend.first_name)
        self.assertEqual(response.data['last_name'], friend.last_name)

    def test_update_friend(self):
        """
        友達情報の更新テスト
        """
        friend = Friend.objects.create(user=self.user, first_name="Taro", last_name="Yamada", phone_number="111", platform="Twitter")
        detail_url = reverse('friends:friend-detail', kwargs={'pk': friend.pk})
        updated_data = {
            "first_name": "Taro",
            "last_name": "Updated",
            "phone_number": "999",
            "platform": "Twitter"
        }
        response = self.client.put(detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['last_name'], "Updated")
        self.assertEqual(response.data['phone_number'], "999")

    def test_delete_friend(self):
        """
        友達情報の削除テスト
        """
        friend = Friend.objects.create(user=self.user, first_name="Taro", last_name="Yamada", phone_number="111", platform="Twitter")
        detail_url = reverse('friends:friend-detail', kwargs={'pk': friend.pk})
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # 削除後、詳細取得で 404 が返るはず
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
