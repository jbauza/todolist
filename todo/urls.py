from django.conf.urls import include, url, patterns
from rest_framework.authtoken import views

urlpatterns = patterns('',
    url(r'^todo/', include('todolist.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
)
