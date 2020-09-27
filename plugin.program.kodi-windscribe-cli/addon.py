
import xbmcaddon
import xbmcgui

import subprocess

addon 		= xbmcaddon.Addon()
addonname 	= addon.getAddonInfo('name')

line1 = "Hola mundo"
line2 = "Linea dos de datos"
line3 = "Power by Python"

subprocess.call(["/bin/touch", "/tmp/runaddon.log"])

xbmcgui.Dialog().ok(addonname, line1, line2, line3)
 
