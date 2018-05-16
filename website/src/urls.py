from django.contrib import admin
from django.urls import path, include
from blog import urls as blog_urls
from blog.views import index as home_page

urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('blog/', include(blog_urls)),
]
