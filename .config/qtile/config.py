from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

WALLPAPER = "~/Pictures/pop/gruvbox2.jpg"
WALLPAPER_MODE = "fill"

# Colorscheme taken from: https://github.com/morhetz/gruvbox
gruvbox = {
    "bg"        : "#282828",
    "red"       : "#cc241d",
    "green"     : "#98971a",
    "yellow"    : "#d79921",
    "blue"      : "#458588",
    "purple"    : "#b16286",
    "aqua"      : "#689d6a",
    "gray"      : "#a89984",
    "orange"    : "#d65d0e",
    
    "red2"      : "#fb4934",
    "green2"    : "#b8bb26",
    "yellow2"   : "#fabd2f",
    "blue2"     : "#83a598",
    "purple2"   : "#d3869b",
    "aqua2"     : "#8ec07c",
    "gray2"     : "#928374",
    "orange2"   : "#fe8019",

    "fg"        : "#ebdbb2",
    "bg0_h"     : "#1d2021",
    "bg0"       : "#282828",
    "bg1"       : "#3c3836",
    "bg2"       : "#504945",
    "bg3"       : "#665c54",
    "bg4"       : "#7c6f64",
}


#### MAPPINGS -----------------------------------------------------
keys = [
    # Switch between screens
    Key(
        [mod], "F1",
        lazy.to_screen(0),
        desc="Switch focus on Main Screen"
    ),

    Key(
        [mod], "F2",
        lazy.to_screen(1),
        desc="Switch focus on Screen 1"
    ),


    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Kill window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    # Rotating Windows -----------------------
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Resize windows -------------------------
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    # Reset window size
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),


    # Toggle between splitting / stacking windows
    # Windows stacked will still exist (kinda like maximizing)
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Terminal = Super + T
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Restart qtile : Super + Ctrl + r
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),

    # Logout : Super + Ctrl + q
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Launch program
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"), 

    # Take screenshots
    Key([mod], "Print", 
        lazy.spawn("gnome-screenshot -i"))
]



groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # Move window to desired group: Super + shift + <group>
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])


# LAYOUT ----------------------------------------------------
# Well, I only use 2 kinds of layouts. So I don't bother trying
# The others. I'm comfortable with the column
layouts = [
    layout.Max(),
    layout.Columns(
        border_focus= gruvbox["aqua"], 
        border_width=2,
        margin = 4
    ),
    layout.Floating(
        border_focus =gruvbox["aqua"],
        border_width = 2
    )
]







# SCREEN SECTION  -------------------------------------------
widget_defaults = dict(
    font='JetBrainsMonoMedium NF',
    fontsize=15,
    padding=5,
)
extension_defaults = widget_defaults.copy()

# Separator
# TRUE: right arrow
# FALSE: left arrow
def separator_widget(arrow_right: bool, bg: str, fg: str):
    if arrow_right:
        arrow = ""
    else:
        arrow = ""

    return widget.TextBox(arrow, background=bg, foreground=fg, fontsize=18, padding=0)


screens = [
    Screen(

        # WuALLPAPER -------------------------------
        wallpaper = WALLPAPER,
        wallpaper_mode= WALLPAPER_MODE,

        top=bar.Bar(
            [
                widget.Spacer(length=5, background=gruvbox["bg"]),

                # TABLE FLIP ----------------------
                widget.TextBox(
                    "(╯°□°）╯︵ ┻━┻ ",
                    background=gruvbox["green"],
                    foreground=gruvbox["bg"]
                ),
                separator_widget(True, fg=gruvbox["green"], bg=gruvbox["bg3"]),


                # GROUPS LIST --------------------
                widget.GroupBox(background=gruvbox["bg3"],
                                foreground=gruvbox["fg"],
                                highlight_method="block",
                ),
                separator_widget(True, fg=gruvbox["bg3"], bg=gruvbox["bg2"]),

                # SCREEN FOCUS POSITION ----------
                widget.CurrentScreen(
                    background=gruvbox["bg2"],
                    foreground=gruvbox["bg4"]
                ),
                separator_widget(True, fg=gruvbox["bg2"], bg=gruvbox["bg"]),

                # WINDOW NAME ---------------------
                widget.WindowName(
                    background=gruvbox["bg"],
                    foreground=gruvbox["fg"],
                    max_chars=15,
                    padding=10
                ),

                # LAUNCHER ------------------------
                widget.Spacer(length=1, background=gruvbox["bg"]),
                widget.Prompt(
                    background=gruvbox["bg"],
                    foreground=gruvbox["orange"],
                    fontsize=16,
                ),

                widget.Spacer(background=gruvbox["bg"]),

                # LAYOUT INDICATOR
                separator_widget(False, bg=gruvbox["bg"], fg=gruvbox["yellow"]),
                widget.CurrentLayout(
                    background=gruvbox["yellow"],
                    foreground=gruvbox["bg"]
                ),

                # DATE --------------------------
                separator_widget(False, bg=gruvbox["yellow"], fg=gruvbox["blue2"]),
                widget.Clock(
                    background=gruvbox["blue2"], 
                    foreground=gruvbox["bg"], 
                    format='%Y-%m-%d'),

                # CLOCK -------------------------
                separator_widget(False, bg=gruvbox["blue2"], fg=gruvbox["purple2"]),
                widget.Clock(
                    background=gruvbox["purple2"], 
                    foreground=gruvbox["bg"], 
                    format='%I:%M %p'),

                separator_widget(False, bg=gruvbox["purple2"], fg=gruvbox["green"]),
                widget.Memory(
                    background=gruvbox["green"],
                    foreground=gruvbox["bg"],
                )
            ],
            24,
        ),
    ),

    Screen(

        # WALLPAPER -------------------------------
        wallpaper = WALLPAPER,
        wallpaper_mode= WALLPAPER_MODE,

        top=bar.Bar(
            [
                widget.Spacer(length=5, background=gruvbox["bg"]),

                # TABLE FLIP ----------------------
                widget.TextBox(
                    "(╯°□°）╯︵ ┻━┻ ",
                    background=gruvbox["green"],
                    foreground=gruvbox["bg"]
                ),
                separator_widget(True, fg=gruvbox["green"], bg=gruvbox["bg3"]),


                # GROUPS LIST --------------------
                widget.GroupBox(background=gruvbox["bg3"],
                                foreground=gruvbox["fg"],
                                highlight_method="block",
                ),
                separator_widget(True, fg=gruvbox["bg3"], bg=gruvbox["bg2"]),

                # SCREEN FOCUS POSITION ----------
                widget.CurrentScreen(
                    background=gruvbox["bg2"],
                    foreground=gruvbox["bg4"]
                ),
                separator_widget(True, fg=gruvbox["bg2"], bg=gruvbox["bg"]),

                # WINDOW NAME ---------------------
                widget.WindowName(
                    background=gruvbox["bg"],
                    foreground=gruvbox["fg"],
                    max_chars=15,
                    padding=10
                ),

                # LAUNCHER ------------------------
                widget.Spacer(length=1, background=gruvbox["bg"]),
                widget.Prompt(
                    background=gruvbox["bg"],
                    foreground=gruvbox["orange"],
                    fontsize=16,
                ),

                widget.Spacer(background=gruvbox["bg"]),

                # LAYOUT INDICATOR
                separator_widget(False, bg=gruvbox["bg"], fg=gruvbox["yellow"]),
                widget.CurrentLayout(
                    background=gruvbox["yellow"],
                    foreground=gruvbox["bg"]
                ),

                # DATE --------------------------
                separator_widget(False, bg=gruvbox["yellow"], fg=gruvbox["blue2"]),
                widget.Clock(
                    background=gruvbox["blue2"], 
                    foreground=gruvbox["bg"], 
                    format='%Y-%m-%d'),

                # CLOCK -------------------------
                separator_widget(False, bg=gruvbox["blue2"], fg=gruvbox["purple2"]),
                widget.Clock(
                    background=gruvbox["purple2"], 
                    foreground=gruvbox["bg"], 
                    format='%I:%M %p'),

                separator_widget(False, bg=gruvbox["purple2"], fg=gruvbox["green"]),
                widget.Memory(
                    background=gruvbox["green"],
                    foreground=gruvbox["bg"],
                )
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title="gnome-calculator"),
])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
