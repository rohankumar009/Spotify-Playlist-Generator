# Spotify-Playlist-Generator

## Overview
This Spotify Playlist Generator is a command-line program written in Python which allows the users to generate a curated playlist based on entries of artists (*up to four artist names*). The program interacts with the Spotify API through the Spotify library to search for the artists' unique Spotify IDs and create a playlist using those IDs. The generated playlist is then displayed in the terminal.

##### New Update: 
In my previous iteration, the functionality was limited to selecting just four artists for playlist curation. However, I'm excited to share that I'm actively developing an upcoming update for this project. With this update, you'll have the flexibility to choose from a selection of 10 artists and even delve into specific genres. This expanded capability will empower you to craft your playlists with a personal touch, blending diverse artists and genres to create a truly authentic and tailored listening experience that caters to your unique preferences.


I'm aiming to complete this project by December and have plans to integrate it into a web application in the near future.

###### Example for Upcoming Update:
```bash
$ python playlist_generator.py
Enter the artist names and/or genres you want to listen to: 
Artist/Genre 1: Drake
Artist/Genre 2: Sleep
Artist/Genre 3: Study
Artist/Genre 4: Taylor Swift
.
.
.
Artist/Genre 10: Holiday Music
```

    Sorting Issues and adding some features like accessing genres along with artists
## Prerequisites
- Python 3.6 or above
- Spotify library (Install using pip install Spotify)

## Usage
1. Open your terminal and navigate to the project directory:
```bash
cd Spotify-playlist-generator
```

2. Run the program:
```bash
python playlist_generator.py
```
### In Terminal:
```bash
$ python playlist_generator.py
Enter the artist names (up to 4): 
Artist 1: Drake
Artist 2: The Weeknd
Artist 3: Led Zeppelin
Artist 4: The Beatles

Generating playlist...

Playlist:

Artist: Drake
- Track 1: Tuscan Leather
- Track 2: Back to Back
- Track 3: Free Smoke

Artist: The Weeknd
- Track 1: Starboy
- Track 2: Low Life
- Track 3: The Hills

Artist: Led Zeppelin
- Track 1: Stairway to Heaven
- Track 2: Whole Lotta Love
- Track 3: Kashmir



Artist: The Beatles
- Track 1: Let It Be
- Track 2: And I Love Her
- Track 3: Yesterday
```

## Contributing
Contributions are welcome- if you have suggestions, bug fixes, or improvements, please open an issue or submit a pull request!

## License
This project is licensed under the MIT License.
