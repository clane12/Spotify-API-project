from webscrap import Top_songs
import requests
from dotenv import load_dotenv
import os
import base64
import webbrowser # you can use this to directly load the url in a default browser.
import pprint

"""load the .env file and get all the variables"""
# load the .env file for environment variables.
load_dotenv()

# get all the environment variables from the .env file.
spotify_secret = os.getenv("SPOTIFY_SECRET")
spotify_id = os.getenv("SPOTIFY_ID")
spotify_redirect_uri = "http://localhost/"
# print(spotify_secret, spotify_id)



"""webscapping getting the names of all the songs"""
# import the webscrap.py file and from that import Top_songs() class.
songs = Top_songs()
my_songs = songs.songs_list # this songs.songs.list contains all the top 100 songs.
print(my_songs)



"""SPOTIFY API"""

"""oauth2 first is to get the access code"""
# the access code will be at on the url that will be redirected from the spotify.
def get_access_code():
    param = {
        "client_id": spotify_id,
        "response_type": "code",
        "redirect_uri": spotify_redirect_uri,
        "scope": "playlist-modify-private playlist-modify-public"
    }

    # responce = requests.get(url="https://accounts.spotify.com/authorize?", params=param)
    # print(responce.url) # you can either print and then click on it.
    # webbrowser.open(responce.url) # or use webbrowser library to directly open the url in default browser.

get_access_code()
# the access code paste it here, it expires after 1 hour.
code="AQC4I8pwIvbh4-pRlSgo0NRlli54qN9dhHK2jbc5HohHSxZe6-XNLF77vF_EkgH8D8jyrDPXNWYQJuElYB6hldduVEWVh6jDlJFc63snlVyQcDNTL0Y-PP8tLNZ0LlzJ121NrfETpmG8cMH31pRgkwjdsvBhTExLcZr0vfWew_7rnDW9Fs23GJfs_XTQeMqBZF_ANiRn203PAuBSTzfnnPmCpGHyqw"


"""get the API spotify token"""
"""once you get the code, send a post request for the api access token"""
def get_token(code):
    # token url
    token_url = "https://accounts.spotify.com/api/token"

    # set data parameters
    body = {
        "code": code,
        "redirect_uri": spotify_redirect_uri, # the uri we added while creating spotify app.
        "grant_type": "authorization_code"
    }


    # here we need the spotify id:secret but with base64 encoded, so this is the step to convert it into bs64 and then into string.
    auth_string = spotify_id + ":" + spotify_secret
    auth_string = auth_string.encode("utf-8")
    auth_string64 = str(base64.b64encode(auth_string), "utf-8")
    # print(auth_string64)

    # set the headers for to get the access token according to api documentation.
    headers = {
        "Authorization": "Basic " + auth_string64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # send a post request to send the details and get the token.
    # responce2 = requests.post(url=token_url, headers=headers, data=body)
    # print(responce2.content)

get_token(code) # call the function


# once token is retrieved set it as a variable.
access_token = "BQDQ-tOsHn2FO3WKkAdTJ4MuPUKiZp9jz_gJTcY785RgulO7QBx47Ab_AspBaE4S15JpXQyn4fETFzcTWy3f-HWpw046P80ZqbdTouixChZQsPn11KR0NYpWKOP49fq828iZYJaI7W2nA-frPDFP36RhCqYylppDdnfSJ9XSb95w_9S37NjsYOscBMmA1Z5ku4Z3LMuYoj9nsGQKi1xKzZs-VDwbr8fhd6b8aIA-965MXVaJFxnk1WZiyy8ZIpAq6K6K6IJd7EVHIwoZKJH985PR3MI7DK4"


"""once the token is retrieved create a playlist, with the use of token"""
def create_playlist(access_token):
    header = {
        "Authorization": "Bearer " + access_token,
        # "Content-Type": "application/json"
    }

    data = {
        "name": "2014 playlist",
        "description": "New playlist description",
    }

    my_id = "4jj0n7v2a88amruktslrdohoz" # your spotify clied user id.
    # responce3 = requests.post(url=f"https://api.spotify.com/v1/users/{my_id}/playlists", json=data, headers=header)
    # print(responce3.text)

create_playlist(access_token)


"""once the playlist is created get the songs spotify uri"""
header2 = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json" # this line is needed to add all the songs in the playlist, so once all the uri's are retrieved this line can be comment out.
}


track_uri = [] # create a list to store all the uri's.

# go through all the songs list and get all the uri's from spotify.
for song in my_songs:
    parameters_songs = {
        "q": song,
        "type": "track",
        "limit": 1
    }

    responce4 = requests.get(url="https://api.spotify.com/v1/search?", params=parameters_songs, headers=header2)
    # pprint.pprint(responce4.json())

    track_uri.append(responce4.json()['tracks']['items'][0]['uri'])
print(track_uri)


"""once all the uri's are retrieved and also the playlist is created, set the playlist id as a variable and add all the songs in the playist."""
plylist_id = "4vuVamYOrqti02gU7nKQ1E"

body2 = {
    "uris": track_uri,
}
responce5 = requests.post(url=f"https://api.spotify.com/v1/playlists/{plylist_id}/tracks", headers=header2, json=body2)
print(responce5.text)