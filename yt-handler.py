from ytmusicapi import YTMusic
import webbrowser

yt = YTMusic()

def play_yt_music(mood_string):
    # We search for a "Radio" or "Playlist" based on the mood
    # Example: "Moody lo-fi" or "High energy pop"
    search_results = yt.search(f"{mood_string} music", filter="songs")
    
    if search_results:
        top_song = search_results[0]
        video_id = top_song['videoId']
        url = f"https://music.youtube.com/watch?v={video_id}"
        
        print(f"🎵 Playing on YT Music: {top_song['title']} by {top_song['artists'][0]['name']}")
        webbrowser.open(url) # Opens the song in your browser
    else:
        print("No results found on YT Music.")