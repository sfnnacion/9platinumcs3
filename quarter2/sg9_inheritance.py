class Publication: #Create a class called Publication
    def __init__(self, title: str, author: str): # define the constructor method
        self.__title = title # initialize the title atteribute as a private attribute using the double underscore.
        self.__author = author # initialize the author attribute as a private attribute using the double underscore to indicate that it is a private attribute.

    # getter methods for title  
    def get_title(self): # define the getter method to retrieve/return thr title attribute
        return self.__title # return the title attribute when the getter method is called

    # getter methods for author 
    def get_author (self): #define the getter method to retrieve/return the author attribute
        return self.__author # return the author attribute when the getter method is called

    # setter methods for title 
    def set_title(self, title: str): # define the setter method to be able to update the title attribute
        self.__title = title #update the title attribute with a new value when the setter method is called

    #setter methods for author
    def set_author(self, author: str): # define the setter method to update the author attribute
        self.__author = author #update the author attribute with a new value when the setter method is called

    # method to display the information of the publication class
    def display_info(self): #define the method to display the information of the class (publication) which includes the title and author attributes
        print(f"Title: {self.__title}") # print the title attribute of the publication class
        print(f"Author: {self.__author}") #print the author attribute of the publication class

class Book(Publication): # create another class called Book (the child class) that inherits features from the Publication class (the parent class)
    def __init__(self, title: str, author: str, number_pages): # define the constructor method to initialize the title, author, as well as the number of pages attributes of the book class
        super().__init__(title, author) #call the constructor of the parent class (Publication) to initialize the title and author attributes using the super() function
        self.__number_pages = number_pages # initialize the number of pages attribute

    def get_number_pages(self):# getter method to retrieve/return the number_pages 
        return self.__number_pages # return the number_pages attribute
    
    def set_number_pages(self, number_pages): # define the setter method to update the number of pages attribute of the class
        if number_pages < 0: # check if the number of pages is valid and not a negative number 
            print("Number of pages must be positive.") #print the warning message if the number of pages is less than 0
        else: # if number of pages is valid and not a negative number then:
            self.__number_pages = number_pages #  update the private __number_pages attribute with the new value
            

    def display_info(self): # define (this is the method to show book info)
        super().display_info() # call the display_info method from the parent class (Publication) to display the title and author information using the super() function 
        print(f"Number of Pages: {self.__number_pages}") # print the no. pages

class Magazine(Publication): # create the last class called Magazine (another child class) that inherits features from the Publication class (the parent class)
    def __init__(self, title: str, author: str, issue_number): # constructor for magazine + with issue number
        super().__init__(title, author) # call the constructor of the parent class (Publication) to initialize the title and author attributes using the super() function
        self.__issue_number = issue_number #save the issue number as a private attribute

    def set_issue_number(self, issue_number): # setter method to update the issue number
        self.__issue_number = issue_number #update the issue number

    def display_info(self): # method to show the magazine info
        super().display_info() # call the display_info method from the Publication class which is the parent class to be able to display the title & author using the super() function
        print(f"Issue Number: {self.__issue_number}") #print the issue number

    def get_issue_number(self): #getter method to retrieve/return issue number 
        return self.__issue_number # return issue number

#Instantiate and create sample objects of the Publication, Book, and Magazine classes
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.") # make a sample publicaation object
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310) # create a sample book object with 310 pages
mag1 = Magazine("National Geographic", "Various Authors", 202) # create a sample magazine object with issue 202

#Print the information of the Publication, book, and magazine classes
print("Pubication Information: ") #print header for publication
pub1. display_info() # display the publication details

print("\nBook Information: ") #print header for book
book1.display_info() #display the book details
book1.set_number_pages(-50) # test the setter method for number of pages with a negative number to check if it prints a warning message
book1.set_number_pages(350) # test the setter method for number of pages with a valid positive number

print("\nMagazine Information: ") #print header for magazine
mag1.display_info() # display the magazine infos
print(mag1.get_issue_number()) # print issue number using getter method to get issue number of the magazine object
