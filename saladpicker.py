import os
import sys

# themes
term_light = "gruvbox_light.yaml"
term_dark =  "gruvbox_material.yaml"

doom_light = "doom-gruvbox-light"
doom_dark =  "doom-gruvbox"

#variables sent to os.system()
notif = ""
cmd = ""

def light_now():
    if os.environ['UTHEME'] == "light":
        notif = "notify-send -u normal -t 3000  \"themepicker\" \"You are already in light mode, stupid\""
        os.system(notif)
        return ;
    os.environ['UTHEME'] = "light"

    cmd = "alacritty-colorscheme apply " + term_light
    os.system(cmd)

def dark_now():
    if os.environ['UTHEME'] == "dark":
        notif = "notify-send -u normal -t 3000  \"themepicker\" \"You are already in dark mode, stupid\""
        os.system(notif)
        return ;
    os.environ['UTHEME'] = "dark"
    cmd = "alacritty-colorscheme apply " + term_dark
    os.system(cmd)


def main():
    if sys.argv[1] == "light":
        os.system("notify-send -u normal -t 3000 \"themepicker\" \"Switching to light theme\"")
        light_now()
    elif sys.argv[1] == "dark":
        os.system("notify-send -u normal -t 3000 \"themepicker\" \"Switching to dark theme\"")
        dark_now()
    else:
        notif = "notify-send -u normal -t 3000 \"themepicker\" \"Current theme : " + os.environ['UTHEME'] + '"'
        os.system(notif)

if __name__ == '__main__':
    main()
