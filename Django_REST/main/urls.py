
from django.contrib import admin
from django.urls import path,include
from .api import router
from api import api_views as myapp_views

urlpatterns = [
    path('register/', myapp_views.user_list),
    path('user/<int:pk>', myapp_views.userid),
    path('userdelete/<int:pk>',myapp_views.userdelete),
    path('admin/', admin.site.urls),
    path('base/',myapp_views.base),
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
    #path('api/', include(router.urls)),
]
