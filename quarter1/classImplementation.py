class Song:
    def __init__(self, title, artist, yearReleased, genre, duration_in_seconds):
        self.title = title
        self.artist = artist
        self.yearReleased = yearReleased
        self.genre = genre
        self.__duration_in_seconds = duration_in_seconds
        self.__is_playing = False

    def play(self):
        self.__is_playing = True
        print(f"'{self.title}' is now playing.")

    def pause(self):
        self.__is_playing = False
        print(f"'{self.title}' is paused.")

    def replay(self):
        self.__is_playing = True
        print(f"Replaying '{self.title}'...")

    def fastForward(self, seconds):
        print(f"Fast-forwarding '{self.title}' by {seconds} seconds.")

    def get_status(self):
        return(
            f'Title: {self.title}", '
            f'Artist: {self.artist}", '
            f'Year Released: {self.yearReleased}, '
            f'Genre: {self.genre}, '
            f'Duration: {self.__duration_in_seconds}, '
            f'Is Playing: {"Yes" if self.__is_playing else "No"}'
        )

if __name__ == "__main__":
    song1 = Song("Magnets", "NIKI", 2021, "Alt-Pop", 217)
    song2 = Song("No Way Back", "Enhypen", 2026, "K-Pop", 186)

    song1.play()
    song1.fastForward(30)

    print(song1.get_status())
    print(song2.get_status())
