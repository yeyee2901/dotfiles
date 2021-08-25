############################################################################################
#                                                                                          #
#    ████████  ████████ ██      ██     ██████                      ████ ██                 #
#   ░░░░░░██  ██░░░░░░ ░██     ░██    ██░░░░██                    ░██░ ░░   █████          #
#        ██  ░██       ░██     ░██   ██    ░░   ██████  ███████  ██████ ██ ██░░░██         #
#       ██   ░█████████░██████████  ░██        ██░░░░██░░██░░░██░░░██░ ░██░██  ░██         #
#      ██    ░░░░░░░░██░██░░░░░░██  ░██       ░██   ░██ ░██  ░██  ░██  ░██░░██████         #
#     ██            ░██░██     ░██  ░░██    ██░██   ░██ ░██  ░██  ░██  ░██ ░░░░░██         #
#    ████████ ████████ ░██     ░██   ░░██████ ░░██████  ███  ░██  ░██  ░██  █████          #
#   ░░░░░░░░ ░░░░░░░░  ░░      ░░     ░░░░░░   ░░░░░░  ░░░   ░░   ░░   ░░  ░░░░░           #
#                                                                                          #
############################################################################################
# Last update: August 2021

###################
# PATH EXPORTS    #
###################
export ZSH_CONFIG=$HOME/.zshrc
export PICO_SDK_PATH=$HOME/Documents/EmbeddedSystem/raspberry-pico/pico-sdk/
export NEOVIM_CONF=$HOME/.config/nvim/
export PATH=$PATH:$HOME/bin:/usr/local/bin:$HOME/.config/nvim/plugged/:$HOME/.local/bin

##################################################################
# ZSH Configs                                                    #
##################################################################
export ZSH=$HOME/.oh-my-zsh

# awesomepanda, af-magic, amuse
ZSH_THEME="awesomepanda"

# Uncomment the following line to use case-sensitive completion.
CASE_SENSITIVE="true"

DISABLE_AUTO_UPDATE="true"
DISABLE_UPDATE_PROMPT="true"

plugins=(
	git
	zsh-autosuggestions
	zsh-syntax-highlighting
    fzf
)

source $ZSH/oh-my-zsh.sh

if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='nvim'
else
  export EDITOR='nvim'
fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

##################################################################
# End of ZSH Configs                                             #
##################################################################


###################
# Aliases         #
###################
alias ls="exa"
alias la="exa -lah"
alias grep='rg'
alias cat='bat'
alias cls="clear ; la"
alias sk='screenkey'
alias r='. ranger'

# TMUX aliases
alias t='env TERM=screen-256color tmux'
alias tls='t list-session'
alias tat='t attach-session'
alias tnews='t new-session -d -s'
alias tneww='t new-window -n'           
alias tkills='t kill-session -t'        # kill session, specify session name
alias tkillw='t kill-window'            # kill current window
alias tka='t kill-server'

# Vim aliases
alias v='vim'
alias nv='nvim'
alias wiki='cd ~/vimwiki ; nvim ~/vimwiki/index.wiki'

# Dot files
alias dotfiles='/usr/bin/git --git-dir=/home/yeyee2901/.dotfiles/ --work-tree=/home/yeyee2901'


###################
# FZF stuffs      #
###################
alias fzf-cd='cd $(fdfind --type directory . $HOME | fzf-tmux)'
FZF_DEFAULT_COMMAND='fzf'


###################
# Header          #
###################
figlet -f /usr/share/figlet/fonts/pagga.tlf "Pop-OS 21.04" | lolcat

###################
# REMOTES         #
###################
WM_BIMA=te18003@bima.eng.wima.ac.id


###################
# DIO             #
###################
DIODA=~/Pictures/Dio.png

###################
# Other aliases   #
# set by system   #
###################
alias luamake=/home/yeyee2901/bin/lua-language-server/3rd/luamake/luamake
