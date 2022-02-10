from django.db.models import Q, Model
from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView

from csfd_app.forms import SearchForm
from csfd_app.models import Actors, Movies


class Homepage(FormView):
    template_name = "homepage.html"
    form_class = SearchForm


class SearchView(ListView, FormView):
    template_name = "search_results.html"
    form_class = SearchForm
    model = Actors

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Actors.objects.filter(name__icontains=query)
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)

        query = self.request.GET.get('q')
        movies = Movies.objects.filter(title__icontains=query)

        context['movies_list'] = movies
        return context


def actor_detail(request, actor_id):
    actor = Actors.objects.get(id=actor_id)
    # movies = Movies.objects.filter(actors=actor)
    movies = actor.movies.all()
    context = {
        "actor": actor,
        "movies": movies
    }
    return render(request, 'actor_detail.html', context=context)


def movie_detail(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    actors = movie.actors.all()
    context = {
        "movie": movie,
        "actors": actors
    }
    return render(request, 'movie_detail.html', context=context)


class MoviesList(ListView):
    template_name = "movies_list.html"
    queryset = Movies.objects.all().order_by("title")
    context_object_name = "movies"


class ActorsList(ListView):
    template_name = "actors_list.html"
    queryset = Actors.objects.all().order_by("name")
    context_object_name = "actors"
