from django.urls import path

from csfd_app.views import Homepage, SearchView, actor_detail, movie_detail, ActorsList, MoviesList

app_name = "csfd_app"

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("result/", SearchView.as_view(), name="result"),
    path("actors/", ActorsList.as_view(), name="actors"),
    path("movies/", MoviesList.as_view(), name="movies"),
    path("actor/<int:actor_id>/", actor_detail, name="actor-detail"),
    path("movie/<int:movie_id>/", movie_detail, name="movie-detail"),
]