# Salad Picker

This is a very simple python script intended to switch themes from light to dark and back.

## Supported programs :

- Alacritty
- polybar
- (doom) Emacs (WIP)

## Preparations :

### General :

- have a notification deamon

- be cool

### Alacritty :

- install [alacritty-colorscheme](https://github.com/toggle-corp/alacritty-colorscheme) 

### Polybar :

- have two polybar configs named `config.dark` & `config.light`.

- add the following lines to your polybar launch script :

``` sh
cfg="$HOME/.config/polybar/config.$1"
....
polybar "...." --config=$cfg
```

-------------------------------------------------------------------------------
