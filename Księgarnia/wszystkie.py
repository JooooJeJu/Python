import wx
import ksiazka

class Wszystko(wx.Frame):
    def __init__ (self,parent,zbior):
        super(Wszystko, self).__init__(parent, title="Wszystkie książki", size=(800, 800))
        self.panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5,7)
        zbior_szukaj=zbior

        sizer.Add(wx.StaticText(self.panel,label='Wszystkie książki:'),pos=(0,3),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        for book in zbior_szukaj:
            dane = wx.StaticText(self.panel,label=book.Title+'\n'+book.Author+'\n'+str(book.Rack))
            miejsce = book.Rack 
            
            if miejsce <= 5:
                sizer.Add(dane, pos=(1, miejsce),flag=wx.ALIGN_CENTER|wx.EXPAND)
            elif miejsce > 5 and miejsce <= 10:
                sizer.Add(dane, pos=(2, miejsce-5),flag=wx.ALIGN_CENTER|wx.EXPAND)
            elif miejsce > 10 and miejsce <= 15:
                sizer.Add(dane, pos=(3, miejsce-10),flag=wx.ALIGN_CENTER|wx.EXPAND)
            else:
                sizer.Add(dane, pos=(4, miejsce-15),flag=wx.ALIGN_CENTER|wx.EXPAND)
            
        
        
        
        sizer.Add(wx.StaticText(self.panel,label=''),pos=(0,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label=''),pos=(0,1),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label=''),pos=(0,2),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label=''),pos=(0,4),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label=''),pos=(0,5),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label=''),pos=(0,6),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label=''),pos=(1,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label=''),pos=(2,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label=''),pos=(3,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.StaticText(self.panel,label=''),pos=(4,0),flag=wx.ALIGN_CENTER|wx.EXPAND)
        
        i=1
        j=1
        while j <= 4:
            while  i <= 5:
                try:
                    sizer.Add(wx.StaticText(self.panel,label=' Wolne\nMiejsce'),pos=(j,i),flag=wx.ALIGN_CENTER|wx.EXPAND) 
                except:
                    pass
                i = i + 1
            j = j + 1
            i = 1 
        
        sizer.AddGrowableRow(0)
        sizer.AddGrowableRow(1)
        sizer.AddGrowableRow(2)
        sizer.AddGrowableRow(3)
        sizer.AddGrowableRow(4)
        
        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
        sizer.AddGrowableCol(2)
        sizer.AddGrowableCol(3)
        sizer.AddGrowableCol(4)
        sizer.AddGrowableCol(5)
        sizer.AddGrowableCol(6)
        
        
            
        
        self.panel.SetSizer(sizer)
            
        self.Centre()
        self.Show()