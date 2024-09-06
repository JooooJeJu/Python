import wx 
import ksiazka

class Zamien(wx.Frame):
    def __init__(self,parent,zbior):
        super(Zamien, self).__init__(parent, title="Zamiana miejsc", size=(600, 600))
        self.panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5,3)
        self.zbior_szukaj=zbior
        sizer.Add(wx.StaticText(self.panel,label="Wypełnij wszystkie pola"),pos=(0,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        sizer.Add(wx.StaticText(self.panel,label="< Podaj tytuł książki >"),pos=(1,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label="< Podaj autora książki >"),pos=(2,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label="< Podaj miejsce ksiażki >"),pos=(3,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        
        self.tytul_one = wx.TextCtrl(self.panel,value="Podaj tytuł")
        sizer.Add(self.tytul_one,pos=(1,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.autor_one = wx.TextCtrl(self.panel,value="Podaj autora")
        sizer.Add(self.autor_one,pos=(2,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.miejsce_one = wx.TextCtrl(self.panel,value="Podaj miejsce")
        sizer.Add(self.miejsce_one,pos=(3,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.tytul_two = wx.TextCtrl(self.panel,value="Podaj tytuł")
        sizer.Add(self.tytul_two,pos=(1,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.autor_two = wx.TextCtrl(self.panel,value="Podaj autora")
        sizer.Add(self.autor_two,pos=(2,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.miejsce_two = wx.TextCtrl(self.panel,value="Podaj miejsce")
        sizer.Add(self.miejsce_two,pos=(3,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        self.button_zamien = wx.Button(self.panel,label="Zamień")
        self.button_zamien.Bind(wx.EVT_BUTTON,self.zamien)
        sizer.Add(self.button_zamien,pos=(4,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        
        
        sizer.AddGrowableRow(0)
        sizer.AddGrowableRow(1)
        sizer.AddGrowableRow(2)
        sizer.AddGrowableRow(3)
        sizer.AddGrowableRow(4)

        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
        sizer.AddGrowableCol(2)
        
        
        self.panel.SetSizer(sizer)
            
        self.Centre()
        self.Show()
        
    def zamien(self,evt):
        title_one = self.tytul_one.GetValue()
        author_one = self.autor_one.GetValue()
        place_one = self.miejsce_one.GetValue()
        
        title_two = self.tytul_two.GetValue()
        author_two = self.autor_two.GetValue()
        place_two = self.miejsce_two.GetValue()
        
        book_one_check = 0
        book_two_check = 0
        
        book_one = ksiazka.Book(title_one, author_one, place_one)
        book_two = ksiazka.Book(title_two, author_two, place_two)
        

        

            
        
        try:
            place_one = int(place_one)
        except:
            wx.MessageDialog(self, "Nie podano liczby w pierwszej książce! spróbuj ponowanie!", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return 
        
        if not (1 <= place_one <= 20):
            wx.MessageDialog(self, "Podane miejsce nie istnieje!", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return
        
        
        try:
            place_two = int(place_two)
        except:
            wx.MessageDialog(self, "Nie podano liczby w drugiej książce! spróbuj ponowanie!", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return 
        
        if not (1 <= place_two <= 20):
            wx.MessageDialog(self, "Podane miejsce nie istnieje!", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return

        
        for item_one in self.zbior_szukaj:
            if item_one.Title == title_one and item_one.Author == author_one and item_one.Rack == place_one:
                book_one_check = 1
                book_one_checked = item_one
                break
            
            
        for item_two in self.zbior_szukaj:
            if item_two.Title == title_two and item_two.Author == author_two and item_two.Rack == place_two:
                book_two_check = 1
                book_two_checked = item_two
                break

        
        if book_one_check == 1 and book_two_check == 1:
            
            self.zbior_szukaj.remove(book_one_checked)
            self.zbior_szukaj.remove(book_two_checked)
            
            temp = int(book_one.Rack)
            
            book_one.Rack = int(book_two.Rack)
            book_two.Rack = int(temp)
            
            self.zbior_szukaj.append(book_one)
            self.zbior_szukaj.append(book_two)
            
            wx.MessageDialog(self, "Pomyślnie zamienione miejsca książek", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            self.Destroy()
            return self.zbior_szukaj
            
        elif book_one_check == 0:
            wx.MessageDialog(self, "Nie odnaleziono pierwszej książki", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return
        elif book_two_check == 0:
            wx.MessageDialog(self, "Nie odnaleziono drugiej książki", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return
        else:
            wx.MessageDialog(self, "Nie żadnej książki", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            return
        

        