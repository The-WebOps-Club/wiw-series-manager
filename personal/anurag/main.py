#Boa:Frame:SERIES

import wx
import wx.lib.buttons

def create(parent):
    return SERIES(parent)

[wxID_SERIES, wxID_SERIESGENRE1, wxID_SERIESGENRE2, wxID_SERIESGENRE3, 
] = [wx.NewId() for _init_ctrls in range(4)]

class SERIES(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_SERIES, name=u'SERIES', parent=prnt,
              pos=wx.Point(651, 176), size=wx.Size(400, 476),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Series')
        self.SetClientSize(wx.Size(384, 437))
        self.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.genre1 = wx.lib.buttons.GenButton(id=wxID_SERIESGENRE1,
              label=u'Action', name=u'genre1', parent=self, pos=wx.Point(137,
              112), size=wx.Size(109, 35), style=0)
        self.genre1.Center(wx.HORIZONTAL)
        self.genre1.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.genre1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Segoe UI'))
        self.genre1.Bind(wx.EVT_BUTTON, self.OnGenre1Button,
              id=wxID_SERIESGENRE1)

        self.genre2 = wx.lib.buttons.GenButton(id=wxID_SERIESGENRE2,
              label=u'Horror', name=u'genre2', parent=self, pos=wx.Point(137,
              176), size=wx.Size(109, 32), style=0)
        self.genre2.Center(wx.HORIZONTAL)
        self.genre2.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.genre2.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Segoe UI'))
        self.genre2.Bind(wx.EVT_BUTTON, self.OnGenre2Button,
              id=wxID_SERIESGENRE2)

        self.genre3 = wx.lib.buttons.GenButton(id=wxID_SERIESGENRE3,
              label=u'Sci-fi', name=u'genre3', parent=self, pos=wx.Point(137,
              240), size=wx.Size(109, 32), style=0)
        self.genre3.Center(wx.HORIZONTAL)
        self.genre3.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.genre3.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Segoe UI'))
        self.genre3.Bind(wx.EVT_BUTTON, self.OnGenre3Button,
              id=wxID_SERIESGENRE3)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGenre1Button(self, event):
        event.Skip()

    def OnGenre2Button(self, event):
        event.Skip()

    def OnGenre3Button(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    frame = create(None)
    frame.Show()

    app.MainLoop()
