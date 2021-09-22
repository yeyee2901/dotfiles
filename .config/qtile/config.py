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

WALLPAPER = "~/Pictures/pop/KR_Meteor.jpg"
WALLPAPER_MODE = "stretch"

nord = {
    "white" : "#E4E4E4",
    "bg" : "#454545",
    "gray" : "#565656",
    "urgent" : "#ff5656",
    "frost" : [
        "#5e81ac",
        "#81a1c1",
        "#88c0d0",
        "#8fbcbb",
        "#E2C17D",
        "#AF87AF",
        "#82AAFF",
        "#215578",
        "#5B7DA6"
    ],
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
    Key([], "Print", 
        lazy.spawn("gnome-screenshot -i"))
]

# GLOBAL LAYOUTS ---------------------------------------------
# Groups use these layouts by default.
# If it's overwritten during group definition, then these will not
# be used
layouts = [
    layout.Max(),
    layout.Columns(
        border_focus = nord["frost"][6], 
        border_width = 4,
        margin = 4
    ),
    layout.Floating(
        border_focus = nord["frost"][6],
        border_width = 4
    )
]


#######################
# GROUPS              #
#######################
groups = [
    Group(
        name = "1",
        label = "WORK"
    ),
    Group(
        name = "2", 
        label = "BROWSE"
    ),
    Group(
        name = "3",
        label = "MEET",
        layouts = [
            layout.Max()
        ]
    ),
    Group(
        name = "4",
        label = "TERMINAL"
    ),
    Group(
        name = "5",
        label = "CHAT",
        layouts = [
            layout.TreeTab(
                sections = [
                    "Social Medias",
                ],
                panel_width = 200,
                border_width = 0,
                margin_left = 0,

                # Title
                section_fontsize = 20,
                section_bottom = 10,
                section_top = 10,

                # Coloring
                bg_color = nord["frost"][8],
                active_bg =  nord["frost"][7],
                active_fg = "#FFFFFF",
                inactive_bg = nord["frost"][8],
                inactive_fg = "#FFFFFF"
            ),
        ]
    ),
    Group(
        name = "6",
        label = "MUSIC",
        layouts = [
            layout.Columns(
                border_focus = nord["frost"][6], 
                border_width = 4,
                margin = 4
            ),
        ]
    ),
    Group(
        name = "7",
        label = "REC"
    ),
    Group(
        name = "8",
        label = "OTHERS"
    ),
]

# Set the keymapping for group
for group in groups:
    keys.append(Key([mod], group.name, lazy.group[group.name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], group.name, lazy.window.togroup(group.name))) # Send current window to another group


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

        # bottom = bar.Bar(
        #     [
        #         widget.CPU(
        #             foreground = nord["frost"][4],
        #             fontsize = 12
        #         ),

        #         # MEMORY
        #         widget.Memory(
        #             foreground = nord["frost"][4],
        #             fontsize = 12,
        #             format = " RAM:{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}"
        #         )

        #     ],
        #     24,
        #     margin = 0,
        #     background = nord["bg"]
        # ),

        top=bar.Bar(
            [
                # LEFT SIDE
                # widget.Spacer(length=5, background = nord["frost"][0]),

                # # MY NAME
                # widget.TextBox(
                #     "💻 yeyee2901",
                #     background = nord["frost"][0],
                #     foreground = nord["white"]
                # ),

                # WINDOW GROUPS
                # separator_widget(True, nord["frost"][1], nord["frost"][0]),
                widget.GroupBox(
                    fontsize = 12,
                    highlight_method = "block",
                    background = nord["frost"][0],
                    other_current_screen_border = "AF87AF",
                    other_screen_border = "AF87AF",
                    this_current_screen_border = "82AAFF"
                ),

                # SYSTEM TRAY INFO & NOTIFICATION
                separator_widget(True, nord["gray"], nord["frost"][0]),
                widget.Systray(
                    background = nord["gray"]
                ),
                widget.Notify(
                    background = nord["gray"],
                    foreground_low = nord["frost"][4],
                    foreground_urgent = nord["urgent"]
                ),
                separator_widget(True, nord["bg"], nord["gray"]),

                # ACTIVE SCREEN
                # separator_widget(True, nord["frost"][2], nord["frost"][1]),
                # widget.CurrentScreen(
                #     background = nord["frost"][2],
                #     inactive_color = nord["frost"][2],
                #     active_color = nord["bg"],
                # ),

                # CURRENT LAYOUT
                # separator_widget(True, nord["white"], nord["frost"][2]),
                # widget.CurrentLayout(
                #     background = nord["white"],
                #     foreground = nord["bg"]
                # ),
                # separator_widget(True, nord["bg"], nord["white"]),

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

                # SYSTEMS INFO
                #   arrow = ""
                #   arrow = ""
                separator_widget(False, nord["frost"][1], nord["frost"][0]),
                widget.WidgetBox(
                    background = nord["frost"][0],
                    foreground = nord["frost"][4],
                    fontsize = 14,
                    text_closed = "🖥️ System ",
                    text_open = "(x)",
                    widgets = [
                        widget.Memory(
                            format = " 💽 {MemUsed: .0f}{mm} |",
                            fontsize = 14,
                            background = nord["frost"][0],
                            foreground = nord["white"],
                        ),
                        widget.CPU(
                            format = "🖥️ {load_percent}% |",
                            fontsize = 14,
                            background = nord["frost"][0],
                            foreground = nord["white"],
                        ),
                        widget.Wlan(
                            interface = "wlo1",
                            fontsize = 14,
                            format = "📶 {essid} ",
                            background = nord["frost"][0],
                            foreground = nord["white"],
                        ),
                    ]
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

        # bottom = bar.Bar(
        #     [
        #         widget.CPU(
        #             foreground = nord["frost"][4],
        #             fontsize = 12
        #         ),

        #         # MEMORY
        #         widget.Memory(
        #             foreground = nord["frost"][4],
        #             fontsize = 12,
        #             format = " RAM:{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}"
        #         )

        #     ],
        #     24,
        #     margin = 0,
        #     background = nord["bg"]
        # ),

        top=bar.Bar(
            [
                # LEFT SIDE
                # widget.Spacer(length=5, background = nord["frost"][0]),

                # # MY NAME
                # widget.TextBox(
                #     "💻 yeyee2901",
                #     background = nord["frost"][0],
                #     foreground = nord["white"]
                # ),

                # WINDOW GROUPS
                # separator_widget(True, nord["frost"][1], nord["frost"][0]),
                widget.GroupBox(
                    fontsize = 12,
                    highlight_method = "block",
                    background = nord["frost"][0],
                    other_current_screen_border = "82AAFF",
                    other_screen_border = "82AAFF",
                    this_screen_border = "AF87AF",
                    this_current_screen_border = "FF56AE"
                ),

                # SYSTEM TRAY INFO & NOTIFICATION
                separator_widget(True, nord["gray"], nord["frost"][0]),
                widget.Systray(
                    background = nord["gray"]
                ),
                widget.Notify(
                    background = nord["gray"],
                    foreground_low = nord["frost"][4],
                    foreground_urgent = nord["urgent"]
                ),
                separator_widget(True, nord["bg"], nord["gray"]),

                # ACTIVE SCREEN
                # separator_widget(True, nord["frost"][2], nord["frost"][1]),
                # widget.CurrentScreen(
                #     background = nord["frost"][2],
                #     inactive_color = nord["frost"][2],
                #     active_color = nord["bg"],
                # ),

                # CURRENT LAYOUT
                # separator_widget(True, nord["white"], nord["frost"][2]),
                # widget.CurrentLayout(
                #     background = nord["white"],
                #     foreground = nord["bg"]
                # ), separator_widget(True, nord["bg"], nord["white"]),
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

                # SYSTEMS INFO
                #   arrow = ""
                #   arrow = ""
                separator_widget(False, nord["frost"][1], nord["frost"][0]),
                widget.WidgetBox(
                    background = nord["frost"][0],
                    foreground = nord["frost"][4],
                    fontsize = 14,
                    text_closed = "🖥️ System ",
                    text_open = "(x)",
                    widgets = [
                        widget.Memory(
                            format = " 💽 {MemUsed: .0f}{mm} |",
                            fontsize = 14,
                            background = nord["frost"][0],
                            foreground = nord["white"],
                        ),
                        widget.CPU(
                            format = "🖥️ {load_percent}% |",
                            fontsize = 14,
                            background = nord["frost"][0],
                            foreground = nord["white"],
                        ),
                        widget.Wlan(
                            interface = "wlo1",
                            fontsize = 14,
                            format = "📶 {essid} ",
                            background = nord["frost"][0],
                            foreground = nord["white"],
                        ),
                    ]
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

# RULE: Set these to always floating
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
    Match(wm_class="gnome-screenshot"),
    Match(wm_class="pcmanfm")
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
