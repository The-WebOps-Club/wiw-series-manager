#!/usr/bin/python

# simple.py

import wx

app = wx.App()

frame = wx.Frame(None, -1, 'simple.py', wx.DefaultPosition, wx.DefaultSize, wx.DEFAULT_FRAME_STYLE, "frame")
frame.Show()

app.MainLoop()