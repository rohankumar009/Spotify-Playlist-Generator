import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Authenticate with Spotify API
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

# Function to generate the playlist
def generate_playlist():
    print("Enter the artist names (up to 4):")
    artist_names = []
    for i in range(4):
        artist_name = input(f"Artist {i+1}: ")
        if artist_name:
            artist_names.append(artist_name)
        else:
            break

    if not artist_names:
        print("No artist names provided.")
        return

    print("\nGenerating playlist...\n")
    playlist_tracks = []

    # Search for artist IDs
    for artist_name in artist_names:
        results = sp.search(q=artist_name, type='artist', limit=1)
        if results['artists']['items']:
            artist_id = results['artists']['items'][0]['id']
            tracks = get_artist_top_tracks(artist_id)
            playlist_tracks.extend(tracks)

    # Display the playlist
    if playlist_tracks:
        print("Playlist:\n")
        for artist, tracks in playlist_tracks.items():
            print(f"Artist: {artist}")
            for i, track in enumerate(tracks):
                print(f"- Track {i+1}: {track}")
            print()
    else:
        print("No tracks found for the provided artist names.")
        print("Try Again")

# Function to get the top tracks of an artist
def get_artist_top_tracks(artist_id):
    tracks = []
    results = sp.artist_top_tracks(artist_id)
    artist_name = results['tracks'][0]['artists'][0]['name']
    for track in results['tracks'][:3]:
        tracks.append(track['name'])
    return {artist_name: tracks}

if __name__ == "__main__":
    generate_playlist()
