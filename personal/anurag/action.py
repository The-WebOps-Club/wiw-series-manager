#Boa:Frame:ACTION

import wx
import wx.lib.buttons

def create(parent):
    return ACTION(parent)

[wxID_ACTION, wxID_ACTIONGENBITMAPBUTTON1, wxID_ACTIONGENBITMAPTEXTBUTTON1, 
 wxID_ACTIONGENBITMAPTEXTBUTTON2, wxID_ACTIONGENBITMAPTEXTBUTTON3, 
 wxID_ACTIONGENBITMAPTEXTBUTTON4, wxID_ACTIONGENBITMAPTEXTBUTTON5, 
] = [wx.NewId() for _init_ctrls in range(7)]

class ACTION(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_ACTION, name=u'ACTION', parent=prnt,
              pos=wx.Point(831, 113), size=wx.Size(400, 485),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Action')
        self.SetClientSize(wx.Size(384, 446))
        self.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.genBitmapTextButton1 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ACTIONGENBITMAPTEXTBUTTON1, label='genBitmapTextButton1',
              name='genBitmapTextButton1', parent=self, pos=wx.Point(48, 64),
              size=wx.Size(288, 56), style=0)
        self.genBitmapTextButton1.Center(wx.HORIZONTAL)
        self.genBitmapTextButton1.SetLabelText(u'aaa')
        self.genBitmapTextButton1.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Segoe UI'))
        self.genBitmapTextButton1.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.genBitmapTextButton1.SetBitmapDisabled(wx.Bitmap(u'undo.png',
              wx.BITMAP_TYPE_JPEG))
        self.genBitmapTextButton1.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton1Button, id=wxID_ACTION1)

        self.genBitmapTextButton2 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ACTIONGENBITMAPTEXTBUTTON2, label='genBitmapTextButton2',
              name='genBitmapTextButton2', parent=self, pos=wx.Point(48, 208),
              size=wx.Size(288, 56), style=0)
        self.genBitmapTextButton2.Center(wx.HORIZONTAL)
        self.genBitmapTextButton2.SetLabelText(u'abc')
        self.genBitmapTextButton2.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Segoe UI'))
        self.genBitmapTextButton2.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.genBitmapTextButton2.SetBitmapDisabled(wx.Bitmap(u'undo.png',
              wx.BITMAP_TYPE_JPEG))
        self.genBitmapTextButton2.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton2Button, id=wxID_ACTION2)

        self.genBitmapTextButton3 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ACTIONGENBITMAPTEXTBUTTON3, label='genBitmapTextButton3',
              name='genBitmapTextButton3', parent=self, pos=wx.Point(48, 280),
              size=wx.Size(288, 56), style=0)
        self.genBitmapTextButton3.Center(wx.HORIZONTAL)
        self.genBitmapTextButton3.SetLabelText(u'bad')
        self.genBitmapTextButton3.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Segoe UI'))
        self.genBitmapTextButton3.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.genBitmapTextButton3.SetBitmapDisabled(wx.Bitmap(u'undo.png',
              wx.BITMAP_TYPE_JPEG))
        self.genBitmapTextButton3.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton3Button, id=wxID_ACTION3)

        self.genBitmapTextButton4 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ACTIONGENBITMAPTEXTBUTTON4, label='genBitmapTextButton4',
              name='genBitmapTextButton4', parent=self, pos=wx.Point(48, 352),
              size=wx.Size(288, 56), style=0)
        self.genBitmapTextButton4.Center(wx.HORIZONTAL)
        self.genBitmapTextButton4.SetLabelText(u'cda')
        self.genBitmapTextButton4.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Segoe UI'))
        self.genBitmapTextButton4.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.genBitmapTextButton4.SetBitmapDisabled(wx.Bitmap(u'undo.png',
              wx.BITMAP_TYPE_JPEG))
        self.genBitmapTextButton4.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton4Button, id=wxID_ACTION4)

        self.genBitmapTextButton5 = wx.lib.buttons.GenBitmapTextButton(bitmap=wx.NullBitmap,
              id=wxID_ACTIONGENBITMAPTEXTBUTTON5, label='genBitmapTextButton5',
              name='genBitmapTextButton5', parent=self, pos=wx.Point(48, 136),
              size=wx.Size(288, 56), style=0)
        self.genBitmapTextButton5.Center(wx.HORIZONTAL)
        self.genBitmapTextButton5.SetLabelText(u'aab')
        self.genBitmapTextButton5.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL,
              wx.NORMAL, False, u'Segoe UI'))
        self.genBitmapTextButton5.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.genBitmapTextButton5.SetBitmapDisabled(wx.Bitmap(u'undo.png',
              wx.BITMAP_TYPE_JPEG))
        self.genBitmapTextButton5.Bind(wx.EVT_BUTTON,
              self.OnGenBitmapTextButton5Button, id=wxID_ACTION5)

        self.genBitmapButton1 = wx.lib.buttons.GenBitmapButton(bitmap=wx.NullBitmap,
              id=wxID_ACTIONGENBITMAPBUTTON1, name='genBitmapButton1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(48, 48), style=0)
        self.genBitmapButton1.SetBackgroundColour(wx.Colour(255, 255, 0))
        self.genBitmapButton1.SetBitmapDisabled(wx.Bitmap(u'undo.png',
              wx.BITMAP_TYPE_JPEG))
        self.genBitmapButton1.Bind(wx.EVT_BUTTON, self.OnGenBitmapButton1Button,
              id=wxID_ACTIONGENBITMAPBUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnGenBitmapTextButton1Button(self, event):
        event.Skip()

    def OnGenBitmapTextButton2Button(self, event):
        event.Skip()

    def OnGenBitmapTextButton3Button(self, event):
        event.Skip()

    def OnGenBitmapTextButton4Button(self, event):
        event.Skip()

    def OnGenBitmapTextButton5Button(self, event):
        event.Skip()

    def OnGenBitmapButton1Button(self, event):
        event.Skip()



if __name__ == '__main__':
    app = wx.App()
    frame = ACTION(None)
    frame.Show()

    app.MainLoop()
