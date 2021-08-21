local M = {}

-- Dashboard
require('themes.startify')

-- Lualine
local lualine = require('themes.lualine')

-- Default
M.lualine_set_themes = "nightfly"

-- Tokyonight theme
M.set_tokyonight = function (variant)
  vim.g.tokyonight_style = variant
  vim.cmd('colorscheme tokyonight')
  lualine.setup_lualine('tokyonight')

  -- Transparency
  vim.cmd('hi CursorLine guibg=#3F3F3F')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi SignColumn guibg=none')
  vim.cmd('hi LineNr guibg=none')
  vim.cmd('hi Normal guibg=none')
  vim.cmd('hi TabLineSel guibg=none')
  vim.cmd('hi TabLineFill guibg=none')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi ColorColumn guibg=#555555')

end

-- CodeDark theme (VSCode)
M.set_codedark = function ()
  vim.cmd('colorscheme codedark')
  lualine.setup_lualine('onedark')

  -- Transparency
  vim.cmd('hi CursorLine guibg=#3F3F3F')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi SignColumn guibg=none')
  vim.cmd('hi LineNr guibg=none')
  vim.cmd('hi Normal guibg=none')
  vim.cmd('hi TabLineSel guibg=none')
  vim.cmd('hi TabLineFill guibg=none')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi ColorColumn guibg=#555555')

end

-- Ayu Theme
M.set_ayu = function (variant)
  vim.cmd('let ayucolor = "'..variant..'"')
  vim.cmd('colorscheme ayu')
  lualine.setup_lualine('ayu_'..variant)

  -- Transparency
  vim.cmd('hi CursorLine guibg=#3F3F3F')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi SignColumn guibg=none')
  vim.cmd('hi LineNr guibg=none')
  vim.cmd('hi Normal guibg=none')
  vim.cmd('hi TabLineSel guibg=none guifg=#ff8f00')
  vim.cmd('hi TabLineFill guifg=none guibg=none')
  vim.cmd('hi TabLine gui=none guibg=none guifg=none')
  vim.cmd('hi ColorColumn guibg=#555555')
end

-- Monokai (Sublime Text)
M.set_monokai = function ()
  require('monokai')
  vim.cmd('colorscheme monokai_pro')
  vim.opt.termguicolors = true
  lualine.setup_lualine('horizon')

  -- Transparency
  vim.cmd('hi CursorLine guibg=#3F3F3F')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi SignColumn guibg=none')
  vim.cmd('hi LineNr guibg=none')
  vim.cmd('hi Normal guibg=none')
  vim.cmd('hi TabLineSel guifg=#d00980 guibg=none')
  vim.cmd('hi TabLineFill guibg=none')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi ColorColumn guibg=#555555')

end

-- Aurora theme by ray X, strong but can hurt eyes
M.set_aurora = function()
  vim.cmd('colorscheme aurora')
  lualine.setup_lualine('palenight')

  -- Transparency
  vim.cmd('hi CursorLine guibg=#3F3F3F')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi SignColumn guibg=none')
  vim.cmd('hi LineNr guibg=none')
  vim.cmd('hi Normal guibg=none')
  vim.cmd('hi TabLineSel guibg=none')
  vim.cmd('hi TabLineFill guibg=none')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi ColorColumn guibg=#555555')

end

-- Gruvbuddy by TJDevries, calming for some reason
M.set_gruvbuddy = function ()
  require('colorbuddy').setup()
  require('colorbuddy').colorscheme('gruvbuddy')
  lualine.setup_lualine('seoul256')

  -- Transparency
  vim.cmd('hi CursorLine guibg=#3F3F3F')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi SignColumn guibg=none')
  vim.cmd('hi LineNr guibg=none')
  vim.cmd('hi Normal guibg=none')
  vim.cmd('hi TabLineSel guibg=none')
  vim.cmd('hi TabLineFill guibg=none')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi ColorColumn guibg=#555555')

end

-- The almighty gruvbox
M.set_gruvbox = function ()
  -- Options has to set before setting colorscheme
  local gruv_opts = {
    gruvbox_italicize_comments = true,
    gruvbox_italicize_strings = true, -- avoid confusion
    gruvbox_contrast_dark = 'medium',
  }

  for option,value in pairs(gruv_opts) do
    vim.g[option] = value
  end

  vim.o.background = 'dark'
  vim.cmd('colorscheme gruvbox')
  lualine.setup_lualine('gruvbox')
  vim.cmd('autocmd VimEnter * highlight SignColumn guibg=#2929229')

  -- to avoid confusion
  vim.cmd('hi link Function GruvboxAquaBold')

  -- Transparency
  vim.cmd('hi CursorLine guibg=#3F3F3F')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi SignColumn guibg=none')
  vim.cmd('hi LineNr guibg=none')
  vim.cmd('hi Normal guibg=none')
  vim.cmd('hi TabLineSel guibg=none')
  vim.cmd('hi TabLineFill guibg=none')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi ColorColumn guibg=#555555')

end

-- More almighty gruvbox material, with treesitter support
M.set_gruvbox_material = function ()
  if vim.fn.has('termguicolors') then
    vim.o.termguicolors = true
    local opts = {
      gruvbox_material_enable_bold = true,
      gruvbox_material_enable_italic = true,
      gruvbox_material_transparent_background = true,
      gruvbox_material_visual = 'reverse',
      gruvbox_material_sign_column_background = 'none',
      gruvbox_material_ui_contrast = 'high',
      gruvbox_material_diagnostic_line_highlight = false,
      gruvbox_material_diagnostic_text_highlight = false,
      gruvbox_material_palette = 'mix',
      gruvbox_material_disable_italic_comment = false, -- apparently, only works with icursive fonts
    }

    for option,value in pairs(opts) do
      vim.g[option] = value
    end

    vim.cmd("colorscheme gruvbox-material")

  else
    print('Your Neovim apparently does not support termguicolors')
  end

  lualine.setup_lualine('gruvbox')

  -- Fix tabline transparency
  vim.cmd('hi TabLineSel guibg=none guifg=#B8BB26')

  -- Transparency
  vim.cmd('hi CursorLine guibg=#3F3F3F')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi SignColumn guibg=none')
  vim.cmd('hi LineNr guibg=none')
  vim.cmd('hi Normal guibg=none')
  vim.cmd('hi TabLineSel guibg=none')
  vim.cmd('hi TabLineFill guibg=none')
  vim.cmd('hi TabLine guibg=none')
  vim.cmd('hi ColorColumn guibg=#555555')
end



-- Vim colorizer
-- require('colorizer').setup()

return M
