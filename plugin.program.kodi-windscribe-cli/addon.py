
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
    p = Popen(['/usr/bin/windscribe', 'login'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    inputlogin = username+"\n"+password+"\n"
    out, err = p.communicate(inputlogin.encode())
    return_code = p.returncode
    return out

def windscribe_status():
    p = Popen(['/usr/bin/windscribe', 'status'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    return_code = p.returncode
    return out


if enable == "true":
    with open("/tmp/pluginwscli.log", "a") as myfile:
        myfile.write("plugin enable\n")
        myfile.write(enable)
        myfile.write(username)
        myfile.write(password)
        myfile.write(location)
        myfile.write("======================**********====================\n")
else:
    with open("/tmp/pluginwscli.log", "a") as myfile:
        myfile.write("plugin disable\n")
        myfile.write(enable)
        myfile.write(username)
        myfile.write(password)
        myfile.write(location)
        myfile.write("======================**********====================\n")
	
line1 = "Windscribe Status:"

status = windscribe_status()

if enable == "true":
    if "DISCONNECTED" in status:
        windscribe_login(username, password)
        
        status = windscribe_status()
else:
    if "CONNECTED" in status:
        status = windscribe_status()

status = windscribe_status()

xbmcgui.Dialog().ok(addonname, status)
