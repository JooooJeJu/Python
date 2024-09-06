import wx 
import ksiazka

class Dodaj(wx.Frame):
    def __init__(self,parent,zbior):
        super(Dodaj, self).__init__(parent, title="Dodawanie książki", size=(600, 600))
        self.panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5,2)
        self.zbior_szukaj=zbior
        
        sizer.Add(wx.StaticText(self.panel,label="Wypełnij wszystkie pola"),pos=(0,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        sizer.Add(wx.StaticText(self.panel,label="Podaj tytuł książki >"),pos=(1,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label="Podaj autora książki >"),pos=(2,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label=" Podaj miejsce ksiażki >\n(na półce jest 20 miejsc)"),pos=(3,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.tytul = wx.TextCtrl(self.panel,value="Podaj tytuł")
        sizer.Add(self.tytul,pos=(1,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.autor = wx.TextCtrl(self.panel,value="Podaj autora")
        sizer.Add(self.autor,pos=(2,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.miejsce = wx.TextCtrl(self.panel,value="Podaj miejsce")
        sizer.Add(self.miejsce,pos=(3,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.button_dodaj = wx.Button(self.panel,label="Dodaj")
        self.button_dodaj.Bind(wx.EVT_BUTTON,self.dodaj)
        sizer.Add(self.button_dodaj,pos=(4,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        
        sizer.AddGrowableRow(0)
        sizer.AddGrowableRow(1)
        sizer.AddGrowableRow(2)
        sizer.AddGrowableRow(3)
        sizer.AddGrowableRow(4)

        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
            
        
        
        
        self.panel.SetSizer(sizer)
            
        self.Centre()
        self.Show()
        
    def dodaj(self,evt):
        title = self.tytul.GetValue()
        author = self.autor.GetValue()
        place = self.miejsce.GetValue()

        try:
            place = int(place)
        except:
            wx.MessageDialog(self, "Nie podano liczby! spróbuj ponowanie!", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return 
        
        if not (1 <= place <= 20):
            wx.MessageDialog(self, "Podane miejsce nie istnieje!", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return
        
        book = ksiazka.Book(title,author,place)
        
        for item in self.zbior_szukaj:
            if item.Rack == book.Rack:
                wx.MessageDialog(self, "Podane miejsce jest zajęte wybierz inne!", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
                return
            
        self.zbior_szukaj.append(book)
        wx.MessageDialog(self, "Pomyślnie dodane książkę!", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
        self.Destroy()
        return self.zbior_szukaj
        
        
class Usun(wx.Frame):
    def __init__(self,parent,zbior):
        super(Usun, self).__init__(parent, title="Usuwanie książki", size=(600, 600))
        self.panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5,2)
        self.zbior_szukaj=zbior
        
        sizer.Add(wx.StaticText(self.panel,label="Wypełnij wszystkie pola"),pos=(0,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        sizer.Add(wx.StaticText(self.panel,label="Podaj tytuł książki >"),pos=(1,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label="Podaj autora książki >"),pos=(2,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label=" Podaj miejsce ksiażki >\n(na półce jest 20 miejsc)"),pos=(3,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.tytul = wx.TextCtrl(self.panel,value="Podaj tytuł")
        sizer.Add(self.tytul,pos=(1,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.autor = wx.TextCtrl(self.panel,value="Podaj autora")
        sizer.Add(self.autor,pos=(2,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.miejsce = wx.TextCtrl(self.panel,value="Podaj miejsce")
        sizer.Add(self.miejsce,pos=(3,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.button_dodaj = wx.Button(self.panel,label="Usuń")
        self.button_dodaj.Bind(wx.EVT_BUTTON,self.usun)
        sizer.Add(self.button_dodaj,pos=(4,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        
        sizer.AddGrowableRow(0)
        sizer.AddGrowableRow(1)
        sizer.AddGrowableRow(2)
        sizer.AddGrowableRow(3)
        sizer.AddGrowableRow(4)

        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
            
        
        
        
        self.panel.SetSizer(sizer)
            
        self.Centre()
        self.Show()
        
    def usun(self,evt):
        title = self.tytul.GetValue()
        author = self.autor.GetValue()
        place = self.miejsce.GetValue()

        try:
            place = int(place)
        except:
            wx.MessageDialog(self, "Nie podano liczby! spróbuj ponowanie!", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return 
        
        if not (1 <= place <= 20):
            wx.MessageDialog(self, "Podane miejsce nie istnieje!", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return
        
        book = ksiazka.Book(title,author,place)
        
        counter = 0
        
        for book in self.zbior_szukaj:
            if book.Title == title and book.Author == author and book.Rack == place:
                self.zbior_szukaj.remove(book)
                counter += 1
                break
        
        if counter != 0:
            wx.MessageDialog(self, "Pomyślnie Usunięto książkę!", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            self.Destroy()
            return self.zbior_szukaj
        else:
            wx.MessageDialog(self, "Nie odnalezion podanej książki", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return 
        
                