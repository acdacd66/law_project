from django.contrib import admin
from django.urls import path,include
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),   
    path('account/', include('account.urls')),
    path('detail_board/', include('detail_board.urls')),
    path('lawboard/', include('lawboard.urls')),
]

