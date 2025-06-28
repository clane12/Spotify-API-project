import requests
from bs4 import BeautifulSoup

# website of the billboard 2015
WEBSITE = "https://www.billboard.com/charts/hot-100/"


class Top_songs():
    def __init__(self):
        self.page = self.get_page()
        self.songs_list = self.top_list()

    """get all the contents of the website to figure the path to names of music"""
    def get_page(self):
        responce = requests.get(url=WEBSITE)
        contents = responce.text
        return contents

    """collect all the names of songs."""
    def top_list(self):
        my_songs = []
        soup = BeautifulSoup(self.page, "html.parser")
        songs = soup.select(selector="ul li ul li h3") # this is the location where all the names are stored in html code.
        # print(songs)
        for song in songs:
            # print(song.getText().strip())
            my_songs.append(song.text.strip()) # strip() is used to get rid of all the whitespaces in the text.
        # print(my_songs)
        return my_songs