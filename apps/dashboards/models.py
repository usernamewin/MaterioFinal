from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AlbumType(models.TextChoices):
    STUDIO = 'Studio', 'Studio'
    EP = 'EP', 'EP'
    COMPILATION = 'Compilation', 'Compilation'
    SINGLE = 'Single', 'Single'
    MIXTAPE = 'Mixtape', 'Mixtape'

class Artist(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Album(BaseModel):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    album_type = models.CharField(max_length=20, choices=AlbumType.choices)
    language = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return self.title

class Song(BaseModel):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=200)
    duration = models.DurationField()
    is_title_track = models.BooleanField(default=False)
    music_video_views = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Award(BaseModel):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='awards')
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"
