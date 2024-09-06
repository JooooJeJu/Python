class Book:
        
    def __init__(self,Title = '',Author = '',Rack = 0):
        self.Title = Title
        self.Author = Author
        self.Rack = Rack
        
    def AddBook(self): 
        self.Title = input('Podaj tytuł książki > ')
        self.Author = input('Podaj autora książki > ')
        self.Rack = input('Podaj miejsce na regale na którym ma się znaleźć książka > ')
        while True:
            try:
                self.Rack = int(self.Rack)
                break
            except ValueError:
                self.Rack = input('Podano miejsce nie istnieje ! Podaj poprawne miejsce na regale w którym ma się znaleźć książka > ')            