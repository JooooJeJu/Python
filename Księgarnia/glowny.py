import wx
from wyniki import Wynik_Tytul,Wynik_Autor,Wynik_Regal
from wszystkie import Wszystko
from dodajusun import Dodaj,Usun
from zamien import Zamien
import ksiazka 
    
    
class Window(wx.Frame):
    def __init__(self,title):
        super().__init__(parent = None, title = title, size =(700,500))
        
        k1 = ksiazka.Book('a','b',int(3))
        k2 = ksiazka.Book('c','d',int(2))
        self.books = [k1,k2] 
        self.panel = wx.Panel(self)
        
        sizer = wx.GridBagSizer(4,5)
        
        sizer.Add(wx.StaticText(self.panel,label = 'Zarządzanie książkami:'),pos=(0,0),flag=wx.ALIGN_CENTER)
        
        self.button_dodaj = wx.Button(self.panel,label='Dodaj')
        self.button_dodaj.Bind(wx.EVT_BUTTON,self.dodaj)
        sizer.Add(self.button_dodaj,pos=(1,0), flag = wx.EXPAND)

        self.button_usun = wx.Button(self.panel,label='Usuń')
        self.button_usun.Bind(wx.EVT_BUTTON,self.usun)
        sizer.Add(self.button_usun,pos=(2,0), flag = wx.EXPAND)
        
        self.button_zamien = wx.Button(self.panel,label='Zamień miejscem')
        self.button_zamien.Bind(wx.EVT_BUTTON,self.zamien)
        sizer.Add(self.button_zamien,pos=(3,0),flag = wx.EXPAND)
        
        sizer.Add(wx.StaticText(self.panel,label = 'Wyszukiwanie książek po:'),pos=(0,2),flag=wx.ALIGN_CENTER)
        
        self.button_tytul = wx.Button(self.panel,label='Tytule')
        self.button_tytul.Bind(wx.EVT_BUTTON,self.Wyszukajt) 
        sizer.Add(self.button_tytul,pos=(1,2), flag = wx.EXPAND)
        
        self.button_autor = wx.Button(self.panel,label='Autorze')
        self.button_autor.Bind(wx.EVT_BUTTON,self.Wyszukaja)
        self.button_autor = sizer.Add(self.button_autor,pos=(2,2), flag = wx.EXPAND)
        
        self.button_regal = wx.Button(self.panel,label='Miejscu na półce')
        self.button_regal.Bind(wx.EVT_BUTTON,self.Wyszukajr)
        self.button_regal = sizer.Add(self.button_regal,pos=(3,2), flag = wx.EXPAND)
        
        self.button_wszystkie = wx.Button(self.panel,label='Wyświetl wszystkie książki')
        self.button_wszystkie.Bind(wx.EVT_BUTTON,self.wyswietlwszystkie)
        self.button_wszystkie = sizer.Add(self.button_wszystkie,pos=(4,1), flag = wx.EXPAND)
        
        self.panel.SetSizer(sizer)
        
        sizer.AddGrowableRow(1)
        sizer.AddGrowableRow(2)
        sizer.AddGrowableRow(3)
        sizer.AddGrowableRow(4)
        
        
        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
        sizer.AddGrowableCol(2)
        
        self.Centre()
        self.Show()
    
    def Wyszukajt(self,evt):
        okno_wyniki = Wynik_Tytul(None,self.books)
        okno_wyniki.Show()
        
    def Wyszukaja(self,evt):
        okno_wyniki = Wynik_Autor(None,self.books)
        okno_wyniki.Show()
        
        
    def Wyszukajr(self,evt):
        okno_wyniki = Wynik_Regal(None,self.books)
        okno_wyniki.Show()
        
    def dodaj(self,evt):
        okno_wyniki = Dodaj(None,self.books)
        okno_wyniki.Show()
    
        
    def wyswietlwszystkie(self,evt):
        okno_wszystkie = Wszystko(None,self.books)
        okno_wszystkie.Show()
        
    def usun(self,evt):
        okno_wszystkie = Usun(None,self.books)
        okno_wszystkie.Show()
        
    def zamien(self,evt):
        okno_wszystkie = Zamien(None,self.books)
        okno_wszystkie.Show()
        

    

app = wx.App()
window = Window("Biblioteka")
app.MainLoop()