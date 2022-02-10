from bs4 import BeautifulSoup
import requests
from django.core.management.base import BaseCommand
from csfd_app.models import Movies, Actors


class Command(BaseCommand):
    def handle(self, *args, **options):
        urls = ["https://www.csfd.cz/zebricky/filmy/nejlepsi/?showMore=1",
                "https://www.csfd.cz/zebricky/filmy/nejlepsi/?from=100",
                "https://www.csfd.cz/zebricky/filmy/nejlepsi/?from=200"
                ]
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }
        for url in urls:
            html_text = requests.get(url, headers=headers).text
            soup = BeautifulSoup(html_text, "lxml")
            movies = soup.find_all("article", class_="article article-poster-60")
            for movie in movies:
                movie_href = movie.header.h3.a["href"]
                movie_url = "https://www.csfd.cz" + movie_href
                movie_html_text = requests.get(movie_url, headers=headers).text
                movie_page = BeautifulSoup(movie_html_text, "lxml")
                movie_page_title = movie_page.find("h1").text.strip()
                movie_page_creators = movie_page.find("div", class_="creators").text.split("Hrají:")[-1]
                t = Movies(title=movie_page_title)
                t.save()
                movie_page_actors = movie_page_creators.split("(více)")[0]
                actors = movie_page_actors.split(", ")
                for actor in actors:
                    actor = actor.strip()
                    try:
                        if actor in str(Actors.objects.get(name=actor)):
                            a1 = Actors.objects.get(name=actor)
                            a1.movies.add(t)
                        else:
                            a = Actors(name=actor)
                            a.save()
                            a.movies.add(t)
                    except:
                        a = Actors(name=actor)
                        a.save()
                        a.movies.add(t)
                        continue
        self.stdout.write(self.style.SUCCESS("Data byla úspěšně stažená"))
