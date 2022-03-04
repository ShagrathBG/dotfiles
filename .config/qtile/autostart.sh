#!/bin/sh
xrandr --output DP1 --mode 1280x1024 --noprimary --right-of DP-0 
xrandr --output DP2 --mode 1280x1024 --noprimary --right-of DP-0 
# feh --bg-scale /home/andrew/Pictures/Wallpapers/wp6889832.jpg
nitrogen --restore &
picom --experimental-backends -b #should prevent screen tearing on most setups if needed
setxkbmap -layout 'us,bg' -variant ',phonetic' -option 'grp:lalt_lshift_toggle'
~/.config/polybar/launch.sh --forest
# Low battery notifier
#~/.config/qtile/scripts/check_battery.sh & disown
dunst &
mpd &
viber &
# Start welcome
#eos-welcome & disown

#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
