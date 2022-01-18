from libqtile import bar
from .widgets import *
from libqtile.config import Screen
import os

colors = [["#282c34", "#282c34"], #0 #2f343f
          ["#1c1f24", "#1c1f24"], #1
          ["#dfdfdf", "#dfdfdf"], #2
          ["#ff6c6b", "#ff6c6b"], #3
          ["#98be65", "#98be65"], #4 
          ["#da8548", "#da8548"], #5 
          ["#99c0de", "#99c0de"], #6 #99c0de
          ["#c678dd", "#c678dd"], #7
          ["#e3937f", "#e3937f"], #8 
          ["#a9a1e1", "#a9a1e1"]] #9

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#2f343f", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"), 
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96",
                                background=colors[0]),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=colors[0]
                       ),    
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground=colors[6],fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(alacritt + ' -e yay -Syu')
                    },
                    background=colors[0]),
                widget.Systray(icon_size = 20),
                widget.DF(
                       foreground = colors[6],
                    warn_color = colors[8],
                    partition = '/',
                    visible_on_warn = False
                ),
                widget.TextBox(
                       text = '',
                       foreground =colors[0], 
                       padding = 0,
                       fontsize = 28, 
                       ),
                widget.KeyboardLayout(
                       foreground = colors[6],
                       background = colors[0],
                       configured_keyboards = ['us','bg'],
                       display_map = {'bg phonetic':'bg'},
                       fmt = 'Keyboard: {}',
                       padding = 5
                       ),
                widget.TextBox(                                                                    
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=colors[0],
                       ), 
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=colors[0]
                       ), 
                volume,
                widget.TextBox(                                                                    
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=colors[0],
                       ),
                widget.Cmus(
                        play_color = colors[6]
                        ),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=colors[0]
                       ),    
                #widget.Clock(format=' %Y-%m-%d %a %I:%M %p',
                widget.Clock(format=' %H:%M, %d-%m-%Y',
                       background=colors[0],
                       foreground='#9bd689',
                       fontsize = 20,
                             ),
                       widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground=colors[0],
                       ),   
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#e39378'
                )
                
            ],
            30,  # height in px
            background="#404552"  # background color
        ), ),
]
