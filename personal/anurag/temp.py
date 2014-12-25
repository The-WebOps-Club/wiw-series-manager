#Boa:Frame:SERIES

import wx
import wx.lib.buttons
import wx.lib.hyperlink

def create(parent):
    return SERIES(parent)

[wxID_SERIES, wxID_SERIESGENRE1, wxID_SERIESGENRE2, wxID_SERIESGENRE3, 
] = [wx.NewId() for _init_ctrls in range(4)]

class SERIES(wx.Frame):
    

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SERIES, name=u'SERIES', parent=prnt,
              pos=wx.Point(817, 52), size=wx.Size(400, 485),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Series')
        self.SetClientSize(wx.Size(384, 446))
        self.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.SetAutoLayout(False)
        self.SetBackgroundStyle(wx.BG_STYLE_COLOUR)

        self.genre1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_SERIESGENRE1, label=u'Action', name=u'genre1',
              parent=self, pos=wx.Point(147, 144), size=wx.Size(89, 30),
              style=0)
        self.genre1.SetBackgroundColour(wx.Colour(0, 64, 128))
        self.genre1.SetBitmapDisabled(wx.Bitmap(u'c:/Users/Anurag/Downloads/boa-constructor-0.6.1/Images/Editor/Explorer.png',
              wx.BITMAP_TYPE_PNG))
        self.genre1.Center(wx.HORIZONTAL)
        self.genre1.Bind(wx.EVT_BUTTON, self.g1, id=wxID_SERIESGENRE1)

        self.genre2 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_SERIESGENRE2, label=u'Thriller', name=u'genre2',
              parent=self, pos=wx.Point(147, 208), size=wx.Size(89, 30),
              style=0)
        self.genre2.SetBackgroundColour(wx.Colour(0, 64, 128))
        self.genre2.SetBitmapDisabled(wx.Bitmap(u'c:/Users/Anurag/Downloads/boa-constructor-0.6.1/Images/Editor/Explorer.png',
              wx.BITMAP_TYPE_PNG))
        self.genre2.Center(wx.HORIZONTAL)
        self.genre2.Bind(wx.EVT_BUTTON, self.g2, id=wxID_SERIESGENRE2)

        self.genre3 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_SERIESGENRE3, label=u'Sci-fi', name=u'genre3',
              parent=self, pos=wx.Point(147, 264), size=wx.Size(89, 30),
              style=0)
        self.genre3.SetBackgroundColour(wx.Colour(0, 64, 128))
        self.genre3.SetBitmapDisabled(wx.Bitmap(u'c:/Users/Anurag/Downloads/boa-constructor-0.6.1/Images/Editor/Imports.png',
              wx.BITMAP_TYPE_PNG))
        self.genre3.Center(wx.HORIZONTAL)
        self.genre3.Bind(wx.EVT_BUTTON, self.g3, id=wxID_SERIESGENRE3)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def g1(self, event):
        self.Close()

    def g2(self, event):
        self.Close()
    
    def g3(self, e):
        self.Close()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
