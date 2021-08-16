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

require('user-plugin-settings.setup-vim_cmake')
require('user-plugin-settings.setup-nvim-tree')
require('user-plugin-settings.setup-telescope')
require('user-plugin-settings.setup-snippets')
require('user-plugin-settings.setup-markdown-preview')

require('LSP-TS-Compe.compe_config')
require('LSP-TS-Compe.lsp-diagnostic-setup')
require('LSP-TS-Compe.lsp-starters')
require('LSP-TS-Compe.tree-sitter-configs')

require('keymaps')

-- require('themes.my-themes').set_aurora()
-- require('themes.my-themes').set_tokyonight("night")
--require('themes.my-themes').set_codedark()
-- require('themes.my-themes').set_gruvbox()
-- require('themes.my-themes').set_gruvbox_material()

-- Can be set to transparent
require('themes.my-themes').set_gruvbuddy()
-- require('themes.my-themes').set_ayu("mirage")
-- require('themes.my-themes').set_monokai()

-- Temporary for LaTeX stuffs
-- Currently, no API for autocommand & defining command
vim.cmd('source ~/.config/nvim/autocmds.vim')
vim.cmd('source ~/.config/nvim/LaTeX/LaTeX_comamands.vim')
