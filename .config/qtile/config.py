#          _     _   _         
#         | |   (_) | |        
#   __ _  | |_   _  | |   ___  
#  / _` | | __| | | | |  / _ \ 
# | (_| | | |_  | | | | |  __/ 
#  \__, |  \__| |_| |_|  \___| 
#     | |                      
#     |_|                      
#
# yeyee2901 - 14 Sept 2021

from typing import List  # noqa: F401
import subprocess
import os

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"

WALLPAPER = "~/Pictures/pop/nord_circuit.png"
WALLPAPER_MODE = "fill"

nord = {
    "white" : "#E4E4E4",
    "bg" : "#454545",
    "frost" : [
        "#5e81ac",
        "#81a1c1",
        "#88c0d0",
        "#8fbcbb",
        "#E2C17D",
        "#AF87AF",
        "#82AAFF"
    ]

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

    # File Manager
    Key([mod], "f", lazy.spawn("pcmanfm"), desc="Launch File Manager"),
    
    # Terminal = Super + T
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Restart qtile : Super + Ctrl + r
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),

    # Logout : Super + Ctrl + q
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    # Launcher using rofi
    Key([mod], "Return", lazy.spawn("rofi -sidebar-mode -show window"),
        desc="Spawn a command using a prompt widget"
    ), 

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
        border_focus = nord["frost"][6], 
        border_width = 4,
        margin = 10
    ),
    layout.Floating(
        border_focus = nord["frost"][6],
        border_width = 4
    )
]







# SCREEN SECTION  -------------------------------------------
widget_defaults = dict(
    font='JetBrainsMonoMedium NF',
    fontsize=12,
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
    # SCREEN 1 ------------------------------------
    Screen(

        # WALLPAPER -------------------------------
        wallpaper = WALLPAPER,
        wallpaper_mode= WALLPAPER_MODE,

        bottom = bar.Bar(
            [
                # LEFT SIDE
                # CURRENT WINDOW NAME
                widget.WindowName(
                    background = nord["frost"][0],
                    foreground = "#121212",
                    format = "{name}",
                    fontsize = 14
                ),
                separator_widget(True, nord["bg"], nord["frost"][0]),

                
                widget.Spacer(background = nord["bg"]),

                # RIGHT SIDE
                # CPU
                widget.CPU(
                    foreground = nord["frost"][4],
                    fontsize = 16
                ),

                # MEMORY
                widget.Memory(
                    foreground = nord["frost"][4],
                    fontsize = 16,
                    format = " RAM:{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}"
                )

            ],
            24,
            margin = 0,
            background = nord["bg"]
        ),

        top=bar.Bar(
            [
                # LEFT SIDE
                widget.Spacer(length=5, background = nord["frost"][0]),

                # MY NAME
                widget.TextBox(
                    "💻 yeyee2901",
                    background = nord["frost"][0],
                    foreground = nord["white"]
                ),

                # WINDOW GROUPS
                separator_widget(True, nord["frost"][1], nord["frost"][0]),
                widget.GroupBox(
                    fontsize = 10,
                    highlight_method = "block",
                    background = nord["frost"][1],
                    foreground = nord["bg"],
                ),

                # ACTIVE SCREEN
                separator_widget(True, nord["frost"][2], nord["frost"][1]),
                widget.CurrentScreen(
                    background = nord["frost"][2],
                    inactive_color = nord["frost"][2],
                    active_color = nord["bg"],
                ),

                # CURRENT LAYOUT
                separator_widget(True, nord["white"], nord["frost"][2]),
                widget.CurrentLayout(
                    background = nord["white"],
                    foreground = nord["bg"]
                ),

                # PROMPT
                widget.Prompt(
                    background = nord["white"],
                    foreground = nord["bg"],
                ),

                widget.Spacer(1, background = nord["white"]),

                separator_widget(True, nord["bg"], nord["white"]),

                # RIGHT SIDE
                widget.Spacer(background = nord["bg"]),

                # MOC - music player
                separator_widget(False, nord["bg"], nord["white"]),
                widget.Moc(
                    background = nord["white"],
                    foreground = nord["bg"],
                    play_color = nord["bg"],
                    noplay_color = nord["bg"],
                ),

                # DATE
                separator_widget(False, nord["white"], nord["frost"][2]),
                widget.Clock(
                    background = nord["frost"][2],
                    foreground = nord["bg"],
                    format = "%d/%m/%Y"
                ),

                # CLOCK
                separator_widget(False, nord["frost"][2], nord["frost"][1]),
                widget.Clock(
                    background = nord["frost"][1],
                    foreground = nord["bg"],
                ),

                # WIFI INDICATOR
                separator_widget(False, nord["frost"][1], nord["frost"][0]),
                widget.Wlan(
                    interface = "wlo1",
                    fontsize = 14,
                    format = "WLAN: {essid} ",
                    background = nord["frost"][0],
                    foreground = nord["white"],
                ),

            ],
            24,
            margin = 0,
            background = nord["bg"],
        ),
    ),

    # SCREEN 2 ------------------------------------
    Screen(

        # WALLPAPER -------------------------------
        wallpaper = WALLPAPER,
        wallpaper_mode= WALLPAPER_MODE,

        bottom=bar.Bar(
            [
                # LEFT SIDE
                # CURRENT WINDOW NAME
                widget.WindowName(
                    background = nord["white"],
                    foreground = nord["bg"],
                    format = "{name}"
                ),
                separator_widget(True, nord["bg"], nord["white"]),

                
                widget.Spacer(background = nord["bg"]),

                # RIGHT SIDE
                # CPU
                widget.CPU(
                    foreground = nord["frost"][4],
                    fontsize = 16
                ),

                # MEMORY
                widget.Memory(
                    foreground = nord["frost"][4],
                    fontsize = 16,
                    format = " RAM:{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}"
                )

            ],
            24,
            margin = 0,
            background = nord["bg"]
        ),

        top=bar.Bar(
            [
                # LEFT SIDE
                widget.Spacer(length=5, background = nord["frost"][0]),

                # MY NAME
                widget.TextBox(
                    "💻 yeyee2901",
                    background = nord["frost"][0],
                    foreground = nord["white"]
                ),

                # WINDOW GROUPS
                separator_widget(True, nord["frost"][1], nord["frost"][0]),
                widget.GroupBox(
                    fontsize = 10,
                    highlight_method = "block",
                    background = nord["frost"][1],
                    foreground = nord["bg"],
                ),

                # ACTIVE SCREEN
                separator_widget(True, nord["frost"][2], nord["frost"][1]),
                widget.CurrentScreen(
                    background = nord["frost"][2],
                    inactive_color = nord["frost"][2],
                    active_color = nord["bg"],
                ),

                # CURRENT LAYOUT
                separator_widget(True, nord["white"], nord["frost"][2]),
                widget.CurrentLayout(
                    background = nord["white"],
                    foreground = nord["bg"]
                ),

                # PROMPT
                widget.Prompt(
                    background = nord["white"],
                    foreground = nord["bg"],
                ),

                widget.Spacer(1, background = nord["white"]),

                separator_widget(True, nord["bg"], nord["white"]),

                # RIGHT SIDE
                widget.Spacer(background = nord["bg"]),

                # MOC - music player
                separator_widget(False, nord["bg"], nord["white"]),
                widget.Moc(
                    background = nord["white"],
                    foreground = nord["bg"],
                    play_color = nord["bg"],
                    noplay_color = nord["bg"],
                ),

                # DATE
                separator_widget(False, nord["white"], nord["frost"][2]),
                widget.Clock(
                    background = nord["frost"][2],
                    foreground = nord["bg"],
                    format = "%d/%m/%Y"
                ),

                # CLOCK
                separator_widget(False, nord["frost"][2], nord["frost"][1]),
                widget.Clock(
                    background = nord["frost"][1],
                    foreground = nord["bg"],
                ),

                # WIFI INDICATOR
                separator_widget(False, nord["frost"][1], nord["frost"][0]),
                widget.Wlan(
                    interface = "wlo1",
                    fontsize = 14,
                    format = "WLAN: {essid} ",
                    background = nord["frost"][0],
                    foreground = nord["white"],
                ),

            ],
            24,
            margin = 0,
            background = nord["bg"],
        ),
    ),
]


# MOUSE BINDINGS --------------------------------------
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
    Match(wm_class="gnome-calculator"),
])

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True


#### AUTOSTART ---------------------------------------------------
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


wmname = "LG3D"
