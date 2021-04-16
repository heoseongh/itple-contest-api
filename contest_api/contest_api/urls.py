from django.urls import path, include
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/contests', include('contest.urls')),  # app명.urls
    # path('api/v1', include('rest_framework.urls', namespace='api')) # contest 안에 url로 
]
