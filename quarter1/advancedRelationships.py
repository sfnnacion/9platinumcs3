class Song:
    def __init__(self, title: str, artist: str, duration: int):
        self.title = title
        self.artist = artist
        self.__duration = duration

    def get_info(self):
        return f"{self.title} by {self.artist}, Duration: {self.__duration} seconds"

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

class RhythmGame(VideoGame):
    def __init__(self, title: str, genre: str, difficulty_level: int):
        super().__init__(title, genre)
        self.difficulty_level = difficulty_level

    def display_game_info(self):
        print(f"Rhythm Game: {self.title}, Genre: {self.genre}, Difficulty Level: {self.difficulty_level}")

if __name__ == "__main__":
    print("--- Testing Inheritance ---")
    rhythm_game = RhythmGame("Rhythm Hive", "Mobile Rhythm", 6)
    print(f"Parent attribute (title): {rhythm_game.title}")
    print(f"Parent attribute (genre): {rhythm_game.genre}")
    print(f"Child attribute (difficulty_level): {rhythm_game.difficulty_level}")

    print("\n--- Testing Aggregation ---")
    song1 = Song("No Doubt", "Enhypen", 167)
    song2 = Song("Magnetic", "ILLIT", 160)

    rhythm_game.add_song(song1)
    rhythm_game.add_song(song2)

    print(f"Songs in {rhythm_game.title}:")
    rhythm_game.display_songs()