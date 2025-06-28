🎵 Spotify Billboard 100 Playlist Creator
A Python project that scrapes the top 100 songs from the Billboard Hot 100 and creates a private Spotify playlist containing those songs. It utilizes BeautifulSoup for web scraping and the Spotify API for playlist creation and song search.

✨ Features
🔥 Scrapes the Billboard Hot 100 chart for the top tracks.

🎧 Searches Spotify for each scraped track.

🎵 Creates a new playlist in your Spotify account.

➕ Adds the top 100 songs to the playlist using their Spotify URIs.

🔐 Uses OAuth2.0 to authenticate with Spotify securely.

📦 Requirements
Python 3.x

Spotify Developer Account (for API credentials)

A .env file with your credentials:

SPOTIFY_ID

SPOTIFY_SECRET

Required Libraries:
pip install requests beautifulsoup4 python-dotenv
🚀 How to Run
Clone the repository.

Set up your .env file:
SPOTIFY_ID=your_spotify_client_id
SPOTIFY_SECRET=your_spotify_client_secret

Run the Python script:

python main.py
The script will:

Open a Spotify Auth URL in your browser.

You'll log in and copy the access code from the redirect URL.

Paste it into the script where prompted.

Your playlist will be created and automatically filled with the current Billboard Top 100 songs!

🎮 How It Works
🧠 webscrap.py: Scrapes Billboard to get the top 100 songs.

🔑 Authenticates with Spotify via OAuth 2.0.

🎯 Searches Spotify for each song and retrieves its URI.

🛠 Creates a playlist in your Spotify account.

➕ Adds all songs to the playlist.

🧩 Future Enhancements
📅 Allow date input to scrape historical Billboard charts (e.g., "Top 100 from June 2015").

📁 Export playlist data to CSV or JSON for logging.

💬 Better error handling for missing Spotify matches.

💡 Option to create public playlists instead of private ones.

