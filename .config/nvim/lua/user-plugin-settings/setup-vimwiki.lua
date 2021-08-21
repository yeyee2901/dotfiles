local M = {}

local init_wiki = function()

  vim.cmd[[
    let wiki = {}
    let wiki.path = '~/vimwiki/'
    let wiki.automatic_nested_syntaxes = 1

    let g:vimwiki_list = [wiki]
  ]]

end

init_wiki()

return M
