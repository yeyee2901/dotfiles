#!/bin/bash
env TERM=screen-256color tmux new-session -d -s 'FZF'

tmux send-keys -t 'FZF' 'fzf-cd' Enter
