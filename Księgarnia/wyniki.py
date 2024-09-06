import wx

class Wynik_Tytul(wx.Frame):
    def __init__ (self,parent,zbior):
        super(Wynik_Tytul, self).__init__(parent, title="Wynik", size=(600, 600))
        self.panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5,4)
        
        zbior_szukaj=zbior
        ksiazka = ''
        
        okno = wx.TextEntryDialog(None, 'Podaj tytuł','Tytuł','Tytuł')
        odpowiedz = okno.ShowModal()
        if odpowiedz == wx.ID_OK:
            tytul = okno.GetValue()
        else:
            pass
        
        okno.Destroy()

        for book in zbior_szukaj:
            if book.Title == tytul:
                ksiazka = book
                break  
        
        
        if ksiazka == '':
            wx.MessageDialog(self, "Podana książka nie istnieje lub wpisano błędne dane !", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            self.Destroy()
        else:
            sizer.Add(wx.StaticText(self.panel,label = 'Znaleziono następującą Książkę:'),pos=(0,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = 'Tytuł:'),pos=(1,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = 'Autor:'),pos=(2,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = 'Półka:'),pos=(3,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = ksiazka.Title),pos=(1,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = ksiazka.Author),pos=(2,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = str(ksiazka.Rack)),pos=(3,2),flag=wx.ALIGN_CENTER|wx.EXPAND)

            sizer.AddGrowableRow(1)
            sizer.AddGrowableRow(2)
            sizer.AddGrowableRow(3)

            sizer.AddGrowableCol(2)
            
            self.panel.SetSizer(sizer)
            
            self.Centre()
            self.Show()


class Wynik_Autor(wx.Frame):
    def __init__ (self,parent,zbior):
        super(Wynik_Autor, self).__init__(parent, title="Wynik wyszukiwania", size=(600, 600))
        self.panel = wx.Panel(self)
        sizer = wx.GridBagSizer(2,4)
        zbior_szukaj=zbior
        ksiazka = ''
        
        okno = wx.TextEntryDialog(None, 'Podaj Autora','Autor','Autor')
        odpowiedz = okno.ShowModal()
        if odpowiedz == wx.ID_OK:
            tytul = okno.GetValue()
        else:
            pass
        
        okno.Destroy()

        for book in zbior_szukaj:
            if book.Author == tytul:
                ksiazka = book
                break  
        
        
        if ksiazka == '':
            wx.MessageDialog(self, "Podana książka nie istnieje lub wpisano błędne dane !", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            self.Destroy()
        else:
            sizer.Add(wx.StaticText(self.panel,label = 'Znaleziono następującą Książkę:'),pos=(0,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = 'Tytuł:'),pos=(1,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = 'Autor:'),pos=(2,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = 'Półka:'),pos=(3,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = ksiazka.Title),pos=(1,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = ksiazka.Author),pos=(2,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = str(ksiazka.Rack)),pos=(3,2),flag=wx.ALIGN_CENTER|wx.EXPAND)

            sizer.AddGrowableRow(1)
            sizer.AddGrowableRow(2)
            sizer.AddGrowableRow(3)

            sizer.AddGrowableCol(2)
            
            self.panel.SetSizer(sizer)
            
            self.Centre()
            self.Show()
        
        
class Wynik_Regal(wx.Frame):
    def __init__ (self,parent,zbior):
        super(Wynik_Regal, self).__init__(parent, title="Wynik wyszukiwania", size=(600, 600))
        self.panel = wx.Panel(self)
        sizer = wx.GridBagSizer(2,4)
        zbior_szukaj=zbior
        ksiazka = ''
        
        okno = wx.TextEntryDialog(None, 'Podaj miejsce na półce','miejsce','0')
        odpowiedz = okno.ShowModal()
        if odpowiedz == wx.ID_OK:
            tytul = okno.GetValue()
            while True:
                try:
                    tytul = int(tytul)
                    break
                except ValueError:
                    okno = wx.TextEntryDialog(None, 'Nie podano poprawnej liczby, spróbuj ponownie','miejsce','0')
                    odpowiedz = okno.ShowModal()
                    if odpowiedz == wx.ID_OK:
                        tytul = okno.GetValue()    
        else:
            pass
        
        okno.Destroy()

        for book in zbior_szukaj:
            if book.Rack == tytul:
                ksiazka = book
                break  
        
        
        if ksiazka == '':
            wx.MessageDialog(self, "Podana książka nie istnieje lub wpisano błędne dane !", "Komunikat", wx.OK | wx.ICON_INFORMATION).ShowModal()
            self.Destroy()
        else:
            sizer.Add(wx.StaticText(self.panel,label = 'Znaleziono następującą Książkę:'),pos=(0,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = 'Tytuł:'),pos=(1,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = 'Autor:'),pos=(2,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = 'Półka:'),pos=(3,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = ksiazka.Title),pos=(1,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = ksiazka.Author),pos=(2,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
            sizer.Add(wx.StaticText(self.panel,label = str(ksiazka.Rack)),pos=(3,2),flag=wx.ALIGN_CENTER|wx.EXPAND)

            sizer.AddGrowableRow(1)
            sizer.AddGrowableRow(2)
            sizer.AddGrowableRow(3)

            sizer.AddGrowableCol(2)
            
            self.panel.SetSizer(sizer)
            
            self.Centre()
            self.Show()

    
