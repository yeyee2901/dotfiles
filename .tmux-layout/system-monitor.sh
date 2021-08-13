#!/bin/bash
env TERM=screen-256color tmux new-session -d -s 'SystemMonitor' -n 'System'
tmux new-window -d -t 'SystemMonitor' -n 'Network'

tmux send-keys -t 'SystemMonitor':'System'    'htop' Enter
tmux send-keys -t 'SystemMonitor':'Network'   'wavemon' Enter
