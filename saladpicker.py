import os
import sys

# read config
cfile = os.getenv('HOME') + "/.config/saladpicker/saladrc"
fo = open(cfile, "r")
current = fo.read(5)
# themes
term_light = "gruvbox_light.yaml"
term_dark  = "gruvbox_material.yml"

doom_light = "doom-gruvbox-light"
doom_dark  = "doom-gruvbox"

poly_light = ['#222', '#dfdfdf'] # [foreground, background]
poly_dark  = ['#dfdfdf', '#222']

# variables sent to os.system()
notif = ""
cmd = ""

def light_now():
    if current == "ligh":
        notif = "notify-send -u normal -t 3000  \"themepicker\" \"You are already in light mode, stupid\""
        os.system(notif)
        return "ligh"

    fo.close()
    cmd = "alacritty-colorscheme apply " + term_light
    os.system(cmd)
    return "ligh"

def dark_now():
    if current == "dark":
        notif = "notify-send -u normal -t 3000  \"themepicker\" \"You are already in dark mode, stupid\""
        os.system(notif)
        return "dark"

    fo.close()
    cmd = "alacritty-colorscheme apply " + term_dark
    os.system(cmd)
    return "dark"


def main():
    if len(sys.argv) == 1:
        notif = "notify-send -u normal -t 3000 \"themepicker\" \"Current theme : " + os.environ['UTHEME'] + '"'
        os.system(notif)
    elif sys.argv[1] == "ligh":
        os.system("notify-send -u normal -t 3000 \"themepicker\" \"Switching to light theme\"")
        current = light_now()
    elif sys.argv[1] == "dark":
        os.system("notify-send -u normal -t 3000 \"themepicker\" \"Switching to dark theme\"")
        current = dark_now()
    newf = open(cfile, "w")
    newf.write(current)
    newf.close()

if __name__ == '__main__':
    main()
