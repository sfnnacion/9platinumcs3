class Song:
    def __init__(self, title: str, artist: str, duration: int):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_info(self):
        return f"{self.title} by {self.artist}, duration: {self.duration} seconds"

class VideoGame:
    def __init__(self, title: str, genre: str):
        self.title = title
        self.genre = genre
        self._songs = []

    def add_song(self, song: Song):
        self._songs.append(song)

    def display_songs(self):
        for song in self._songs:
            print(f"- {song.get_info()}")

if __name__ == "__main__":
    print("--- BEFORE RELATIONSHIP ---")
    game = VideoGame("Fortnite", "Battle Royale")
    song1 = Song("No Doubt", "Enhypen", 167)
    song2 = Song("Magnetic", "ILLIT", 160)
    song3 = Song("Dynamite", "BTS", 199)

    print(f"Game: {game.title}, Genre: {game.genre}")
    print(f"Song 1: {song1.get_info()}")
    print(f"Song 2: {song2.get_info()}")
    print(f"Song 3: {song3.get_info()}")

    print("\n--- BUILDING RELATIONSHIP ---")
    print("Adding songs to the video game...")
    game.add_song(song1)
    game.add_song(song2)
    game.add_song(song3)

    print("\n--- AFTER RELATIONSHIP ---")
    print(f"Songs in {game.title} ({game.genre}):")
    game.display_songs()