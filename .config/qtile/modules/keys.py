from libqtile.lazy import lazy
from libqtile.config import Key


# from modules.groups import groups
# from modules.layouts import layouts, floating_layout
# from modules.mouse import mouse
# from modules.hooks import *
# from libqtile.lazy import lazy
# import os
# from modules.screens import screens

mod = "mod4"
alt = "mod1"
terminal = "kitty"
browser = "firefox"


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([alt], "d", lazy.spawn("rofi -show run"), desc="spawn rofi"),
    Key([mod], "b", lazy.spawn(browser), desc="Firefox"),

    # Keyboard layout
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Switch keyboard layouts"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"],
        "j",
        lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Shrink/Grow
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "r",
        lazy.restart(),
        desc="Restart QTile"),
    # Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
    # Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
    # Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),
    # Switch focus to specific monitor (out of three)
    Key([mod], "w",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'
        ),
    Key([mod], "e",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'
        ),
    Key([mod], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    # CMUS
    # Key([mod], "p",
    #     lazy.spawn("cmus-remote -n"),
    #     desc='cmus next'
    #     ),
    # Key([mod], "o",
    #     lazy.spawn("cmus-remote -r"),
    #     desc='cmus prev'
    #     ),

    # MPC
    Key([mod], "v",
        lazy.spawn("mpc next"),
        desc='mpc next'
        ),
    Key([mod], "z",
        lazy.spawn("mpc prev"),
        desc='mpc prev'
        ),
    Key([mod], "x",
        lazy.spawn("mpc toggle"),
        desc='mpc start/stop'
        ),
    Key([mod, "shift"], "v",
        lazy.spawn("mpc volume +10"),
        desc='vol +10%'
        ),
    Key([mod, "shift"], "z",
        lazy.spawn("mpc volume -10"),
        desc='vol -10%'
        ),
    # Key([mod, "shift"], "m", monocle)
]
