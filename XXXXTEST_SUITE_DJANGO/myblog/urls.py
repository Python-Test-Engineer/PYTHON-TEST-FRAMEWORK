from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("posts.urls")),
    path("admin/", admin.site.urls),
    path("posts/", include("posts.urls"), name="posts"),
    path("authuser/", include("authuser.urls"), name="authuser"),
    path("filemanager/", include("filemanager.urls")),
    path("", include("filemanager.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
