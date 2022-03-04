from libqtile import hook
import subprocess
import os

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
@hook.subscribe.startup
def start_always():
    subprocess.call(['/home/andrew/.config/polybar/forest/launch.sh'])
