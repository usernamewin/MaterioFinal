from django.urls import path
from .views import DashboardsView, albums_over_time, album_type_distribution, awards_by_album, most_awarded_artist, ArtistView, AlbumView, SongView, AwardView

urlpatterns = [
    path("", DashboardsView.as_view(template_name="dashboard_analytics.html"), name="index"),

    # Chart API Endpoints
    path("api/albums-over-time/", albums_over_time, name="albums_over_time"),
    path("api/album-type-distribution/", album_type_distribution, name="album_type_distribution"),
    path("api/awards-by-album/", awards_by_album, name="awards_by_album"),
    path("api/most-awarded-artist/", most_awarded_artist, name="most-awarded-artist"),
    path("artist/list/", ArtistView.as_view(template_name="artist_list.html"), name="artist-list"),
    path("album/list/", AlbumView.as_view(template_name="album_list.html"), name="album-list"),
    path("song/list/", SongView.as_view(template_name="song_list.html"), name="song-list"),
    path("award/list/", AwardView.as_view(template_name="award_list.html"), name="award-list"),
]