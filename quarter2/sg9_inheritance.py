class Publication: #Create a class called Publication
    def __init__(self, title: str, author: str): # define the constructor method
        self.__title = title
        self.__author = author

    # getter methods for title  
    def get_title(self):
        return self.__title

    # getter methods for author 
    def get_author (self):
        return self.__author

    # setter methods for title 
    def set_title(self, title: str):
        self.__title = title

    #setter methods for author
    def set_author(self, author: str):
        self.__author = author

    # method to display the information of the publication class
    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")

class Book(Publication): # create another class called Book (the child class) that inherits features from the Publication class (the parent class)
    def __init__(self, title: str, author: str, number_pages):
        super().__init__(title, author)
        self.__number_pages = number_pages

    def set_number_pages(self, number_pages): 
        if number_pages < 0: # check if the number of pages is valid and not a negative number
            print("Number of pages must be positive.")
        else:
            self.__number_pages = number_pages
            

    def display_info(self):
        super().display_info() # call the display_info method from the parent class (Publication) to display the title and author information using the super() function 
        print(f"Number of Pages: {self.__number_pages}")

class Magazine(Publication): # create the last class called Magazine (another child class) that inherits features from the Publication class (the parent class)
    def __init__(self, title: str, author: str, issue_number):
        super().__init__(title, author) # call the constructor of the parent class (Publication) to initialize the title and author attributes using the super() function
        self.__issue_number = issue_number

    def display_info(self):
        super().display_info() # call the display_info method from the Publication class which is the parent class to be able to display the title & author using the super() function
        print(f"Issue Number: {self.__issue_number}")

    def get_issue_number(self):
        return self.__issue_number

#Instantiate and create sample objects of the Publication, Book, and Magazine classes
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

#Print the information of the Publication, book, and magazine classes
print("Pubication Information: ")
pub1. display_info()

print("\nBook Information: ")
book1.display_info()
book1.set_number_pages(-50) # test the setter method for number of pages with a negative number to check if it prints a warning message
book1.set_number_pages(350) # test the setter method for number of pages with a valid positive number

print("\nMagazine Information: ")
mag1.display_info()
print(mag1.get_issue_number()) # use getter method to get issue number of the magazine object
