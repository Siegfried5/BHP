import win32gui
import win32ui
import wincon
import win32api

# grab a handle to the main desktop windows
hdesktop = win32gui.GetDesktopWindow()

# determine the size of all monitors in pixels
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)

# create a device context
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)

# create a memory based device context
mem_dc = img_dc.CreateCompatibleDC()

# create a bitmap object
screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(screenshot)