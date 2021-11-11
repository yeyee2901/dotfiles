local M = {}

-- Dashboard
require('themes.startify')

-- Lualine
local lualine = require('themes.lualine')

-- NORD THEME
M.set_nord = function()
  local opts = {
    nord_contrast = true,
    nord_borders = true,
    nord_disable_background = true,
    nord_italic = true,
  }

  for option,value in pairs(opts) do
    vim.g[option] = value
  end

  require('nord').set()
  lualine.setup_lualine('nord')

  -- Cursor Line
  vim.opt.colorcolumn = '0'
  vim.opt.cursorline = false

  -- default:
  --  guibg = #3B4252
  if opts.nord_disable_background then
    vim.cmd[[highlight TelescopeNormal guibg=none]]
  end

  -- default:
  --  guibg = #3B4252
  vim.cmd[[highlight Visual guibg=#696969]]

  -- TablineSel colors
  -- default: #4C566A
  vim.cmd[[highlight TablineSel guibg=none]]
end

M.set_solarized = function ()

  local opts = {
    termguicolors = true,
    solarized_italics = true,
    solarized_visibility = 'normal',
    solarized_diffmode = 'high',
    solarized_termtrans = 0
  }

  for opt, val in ipairs(opts) do
    vim.g[opt] = val
  end

  lualine.setup_lualine('solarized_dark')
  vim.cmd('colorscheme solarized-high')

  vim.cmd("highlight Normal guibg=none")
  vim.cmd("highlight LineNr guibg=none")
  vim.cmd("highlight TSFunction guibg=none")
  vim.cmd("highlight TSVariable guibg=none")
end

-- Vim colorizer
require('colorizer').setup()

return M
