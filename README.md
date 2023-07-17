# Spotify-Playlist-Generator

## Overview
This Spotify Playlist Generator is a command-line program written in Python which allows the users to generate a curated playlist based on entries of artists (*up to four artist names*). The program interacts with the Spotify API through the Spotipy library to search for the artists' unique Spotify IDs and create a playlist using those IDs. The generated playlist is then displayed in the terminal.

    Still in Progress- Expected Compeletion July 14th

## Prerequisites
- Python 3.6 or above
- Spotify library (Install using pip install spotify)

## Useage
1. Open your terminal and navigate to the project directory:
```bash
cd spotify-playlist-generator
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
Contributions are welcome, if you have suggestions, bug fixes, or improvements, please open an issue or submit a pull request!

## License
This project is licensed under the MIT License.
