from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('friends/', include(('friends.urls', 'friends'), namespace='friends')),  # 名前空間追加
    path('admin/', admin.site.urls),
]
