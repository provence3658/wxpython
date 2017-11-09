import wx

app = wx.App()

frame = wx.Frame(None, title = "taylor's list")
 
bkg = wx.Panel(frame)

openButton = wx.Button(bkg, label = 'open')
saveButton = wx.Button(bkg, label = 'save')
filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style = wx.HSCROLL | wx.TE_MULTILINE)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion = 1, flag = wx.EXPAND, border = 5)
hbox.Add(openButton, proportion = 0, flag = wx.LEFT, border = 5)
hbox.Add(saveButton, proportion = 0, flag = wx.LEFT, border = 5)

bbox = wx.BoxSizer(wx.VERTICAL)
bbox.Add(hbox, proportion = 0, flag = wx.EXPAND | wx.ALL)
bbox.Add(contents, proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

bkg.SetSizer(bbox)
#frame.Centre
frame.Show()

app.MainLoop()
