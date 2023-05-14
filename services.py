from bs4 import BeautifulSoup
import requests
import pandas as pd

from config.settings import BASE_DIR


class ScraperMovieService():
    url = "https://www.imdb.com/chart/top"

    def get_top_movies(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        poster_tags = soup.find_all('td', class_="posterColumn")
        title_tags = soup.find_all('td', class_="titleColumn")
        rating_tags = soup.find_all('td', class_="ratingColumn imdbRating")

        assert len(poster_tags) == len(title_tags) == len(rating_tags) == 250, "Error occured while scrapping"
        results = []
        for i in range(len(poster_tags)):
            poster_image = self.parse_poster_image(tag=poster_tags[i])
            title = self.parse_title(tag=title_tags[i])
            year = self.parse_year(tag=title_tags[i])
            rating = self.parse_rating(tag=rating_tags[i])
            results.append(
                {
                    'Poster Image:': poster_image,
                    'Poster Title:': title,
                    'Year:': year,
                    'Rating:': rating

                }
            )
        return results

    def parse_poster_image(self, tag):
        return tag.find('img')['src']

    def parse_title(self, tag):
        return tag.find('a').text

    def parse_year(self, tag):
        return int(tag.find('span').text.lstrip('(').rstrip(')').strip())

    def parse_rating(self, tag):
        return float(tag.find('strong').text.strip())


class ScraperShowsService():
    url = 'https://www.imdb.com/chart/toptv/'

    def get_top_shows(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')

        show_poster_tags = soup.find_all('td', class_="posterColumn")
        show_title_tags = soup.find_all('td', class_="titleColumn")
        show_rating_tags = soup.find_all('td', class_="ratingColumn imdbRating")

        assert len(show_poster_tags) == len(show_title_tags) == len(
            show_rating_tags) == 250, "Error occured while scraping"

        show_results = []

        for i in range(len(show_poster_tags)):
            show_poster_image = self.parse_show_image(tag=show_poster_tags[i])
            show_title = self.parse_show_title(tag=show_title_tags[i])
            show_year = self.parse_show_year(tag=show_title_tags[i])
            show_rating = self.parse_show_rating(tag=show_rating_tags[i])

            show_results.append(

                {
                    'show_image:': show_poster_image,
                    'show_title:': show_title,
                    'show_year:': show_year,
                    'show_rating:': show_rating

                }
            )
        print(show_results)
        return show_results

    def parse_show_image(self, tag):
        return tag.find('img')['src']

    def parse_show_title(self, tag):
        return tag.find('a').text

    def parse_show_year(self, tag):
        return tag.find('span').text.lstrip('(').rstrip(')')

    def parse_show_rating(self, tag):
        return float(tag.find('strong').text.strip())


if __name__ == "__main__":
    service = ScraperMovieService()
    top_movies = service.get_top_movies()

    df = pd.DataFrame.from_dict(top_movies)

    output_file_path = BASE_DIR / 'movies.csv'
    df.to_csv(output_file_path)

    service_shows = ScraperShowsService()
    top_show = service_shows.get_top_shows()

    dp = pd.DataFrame.from_dict(top_show)
    output_file_path = BASE_DIR / 'shows.csv'
    dp.to_csv(output_file_path)
