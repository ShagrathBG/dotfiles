from modules.keys import keys, mod
from modules.groups import groups
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.hooks import *
from libqtile.lazy import lazy
import os
from modules.screens import screens
# from libqtile.config import Key

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"
widget_defaults = dict(
        font='Cascadia Code',
        fontsize=13,
        padding=3
)
# Group("5", layout="TreeTab", matches=[Match(wm_class=["viber", "discord"])])
@lazy.window.function
def monocle(win):
    win.cmd_toggle_floating()
    if win.floating:
        win.cmd_center()

# keys = [
#     Key([mod, "shift"], "m", monocle)]
