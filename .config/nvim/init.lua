--                                                   ████     ████     ████     ██       --
--       ██   ██          ██   ██                   █░░░ █   █░░░ █   █░░░██   ███       --
--      ░░██ ██   █████  ░░██ ██   █████   █████   ░    ░█  ░█   ░█  ░█  █░█  ░░██       --
--       ░░███   ██░░░██  ░░███   ██░░░██ ██░░░██     ███   ░ ████   ░█ █ ░█   ░██       --
--        ░██   ░███████   ░██   ░███████░███████    █░░     ░░░█    ░██  ░█   ░██       --
--        ██    ░██░░░░    ██    ░██░░░░ ░██░░░░    █          █     ░█   ░█   ░██       --
--       ██     ░░██████  ██     ░░██████░░██████  ░██████    █      ░ ████    ████      --
--      ░░       ░░░░░░  ░░       ░░░░░░  ░░░░░░   ░░░░░░    ░        ░░░░    ░░░░       --
--               ██              ██     ██           ██                                  --
--              ░░              ░░     ░██          ░██                                  --
--               ██   ███████    ██   ██████        ░██ ██   ██  ██████                  --
--              ░██  ░░██░░░██  ░██  ░░░██░         ░██░██  ░██ ░░░░░░██                 --
--              ░██   ░██  ░██  ░██    ░██          ░██░██  ░██  ███████                 --
--              ░██   ░██  ░██  ░██    ░██     ██   ░██░██  ░██ ██░░░░██                 --
--              ░██   ███  ░██  ░██    ░░██   ░██   ███░░██████░░████████                --
--              ░░   ░░░   ░░   ░░      ░░    ░░   ░░░  ░░░░░░  ░░░░░░░░                 --
-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------
require('basic-settings')
require('packer-plugins-setup')
require('GLOBALS')

require('user-plugin-settings.setup-vim_cmake')
require('user-plugin-settings.setup-nvim-tree')
require('user-plugin-settings.setup-telescope')
require('user-plugin-settings.setup-snippets')
require('user-plugin-settings.setup-markdown-preview')
require('user-plugin-settings.setup-distant')
vim.cmd[[source ~/.config/nvim/VimWiki/setup-vimwiki.vim]]

require('LSP-TS-Compe.cmp-config')
require('LSP-TS-Compe.lsp-diagnostic-setup')
require('LSP-TS-Compe.lsp-starters')
require('LSP-TS-Compe.tree-sitter-configs')

require('keymaps')

require('themes.my-themes').set_nord()

-- Temporary for LaTeX stuffs
-- Currently, no API for autocommand & defining command
vim.cmd('source ~/.config/nvim/autocmds.vim')
vim.cmd('source ~/.config/nvim/LaTeX/LaTeX_commands.vim')

-- User defined commands
vim.cmd('source ~/.config/nvim/commands.vim')
