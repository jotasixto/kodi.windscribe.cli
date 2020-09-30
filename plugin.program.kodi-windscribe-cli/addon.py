
import xbmcaddon
import xbmcgui

from subprocess import Popen, PIPE

addon 		= xbmcaddon.Addon()
addonname 	= addon.getAddonInfo('name')

enable		= addon.getSetting('enable')
username	= addon.getSetting('username')
password	= addon.getSetting('password')
location	= addon.getSetting('location')

def windscribe_login(param_username, param_password):
    if username == "" :
        return ""
    
    p = Popen(['/usr/bin/windscribe', 'login'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    inputlogin = username+"\n"+password+"\n"
    out, err = p.communicate(inputlogin.encode())
    return_code = p.returncode
    return out

def windscribe_connect():
    locations = ["best","GB","DE","NL","FR","US","CA"]
    intlocation = 0
    
    try: 
        intlocation = int(location)
        
        if (intlocation > len(locations)):
            intlocation = 0
    except ValueError:
        pass
    
    p = Popen(['/usr/bin/windscribe', 'connect', locations[intlocation]], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return_code = p.returncode
    return out
    
def windscribe_disconnect():
    locations = ["best","GB","DE","NL","FR","US","CA"]
    
    intlocation = int(location)
    
    p = Popen(['/usr/bin/windscribe', 'disconnect'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return_code = p.returncode
    return out

def windscribe_status():
    p = Popen(['/usr/bin/windscribe', 'status'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return_code = p.returncode
    return out

pDialog = xbmcgui.DialogProgress()
pDialog.create('Kodi', 'Windscribe...')
pDialog.update(5, 'Windscribe updating...')

status = windscribe_status()

if enable == "true":
    if "DISCONNECTED" in status:
        pDialog.update(35, 'Windscribe login...')
        windscribe_login(username, password)

    pDialog.update(55, 'Windscribe connecting...')
    windscribe_connect()
else:
    if "CONNECTED" in status:
        pDialog.update(55, 'Windscribe desconnecting...')
        windscribe_disconnect()


pDialog.update(75, 'Windscribe status...')
status = windscribe_status()

xbmcgui.Dialog().ok(addonname, status)
