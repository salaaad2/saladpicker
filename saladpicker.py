import os
import sys

# read config
cfile = os.getenv('HOME') + "/.config/saladpicker/saladrc"
fo = open(cfile, "r")
current = fo.readline()

# themes
term_light = "night_owlish_light.yaml"
term_dark  = "gruvbox_material.yml"

doom_light = "doom-gruvbox-light"
doom_dark  = "doom-gruvbox"

polybar_cpath = os.getenv('HOME') + "/.config/polybar/launch.sh"

# variables sent to os.system()
notif = ""
cmd = ""

def light_now():
    if current == "light":
        notif = "notify-send -u normal -t 3000  \"themepicker\" \"You are already in light mode, stupid\""
        os.system(notif)
        return "ligh"

    # alacritty
    cmd = "alacritty-colorscheme apply " + term_light
    os.system(cmd)

    # polybar
    cmd = polybar_cpath + " light"
    os.system(cmd)
    return "ligh"

def dark_now():
    if current == "dark":
        notif = "notify-send -u normal -t 3000  \"themepicker\" \"You are already in dark mode, stupid\""
        os.system(notif)
        return "dark"

    # alacritty
    cmd = "alacritty-colorscheme apply " + term_dark
    os.system(cmd)

    # polybar
    cmd = polybar_cpath + " dark"
    os.system(cmd)
    return "dark"


def main():
    global current
    if len(sys.argv) == 1:
        notif = "notify-send -u normal -t 3000 \"themepicker\" \"Current theme : " + os.environ['UTHEME'] + '"'
        os.system(notif)
    elif sys.argv[1] == "ligh":
        os.system("notify-send -u normal -t 3000 \"themepicker\" \"Switching to light theme\"")
        current = light_now()
    elif sys.argv[1] == "dark":
        os.system("notify-send -u normal -t 3000 \"themepicker\" \"Switching to dark theme\"")
        current = dark_now()
    fo.close()
    newf = open(cfile, "w")
    newf.write(current)
    newf.close()

if __name__ == '__main__':
    main()
