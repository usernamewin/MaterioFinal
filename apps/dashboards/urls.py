from django.urls import path
from .views import DashboardsView, albums_over_time, album_type_distribution, awards_by_album

urlpatterns = [
    path("", DashboardsView.as_view(template_name="dashboard_analytics.html"), name="index"),

    # Chart API Endpoints
    path("api/albums-over-time/", albums_over_time, name="albums_over_time"),
    path("api/album-type-distribution/", album_type_distribution, name="album_type_distribution"),
    path("api/awards-by-album/", awards_by_album, name="awards_by_album"),
]