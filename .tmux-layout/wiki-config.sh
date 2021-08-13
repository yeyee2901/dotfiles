#!/bin/bash
env TERM=screen-256color tmux new-session -d -s 'WikiConfig' -n 'VimWiki'
tmux new-window -d -t 'WikiConfig' -n 'Nvim_config'
tmux new-window -d -t 'WikiConfig' -n 'Tmux_config'

tmux send-keys -t 'WikiConfig':'VimWiki'       'wiki' Enter
tmux send-keys -t 'WikiConfig':'Nvim_config'   'cd ~/.config/nvim/ ; nv' Enter
tmux send-keys -t 'WikiConfig':'Tmux_config'   'nv ~/.tmux.conf' Enter
