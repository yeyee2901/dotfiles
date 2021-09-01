local M = {}

local cmp = require('cmp')

cmp.setup({
  completion = {
    completeopt = 'menuone,noselect',
  },

  mapping = {
    ['<C-n>'] = cmp.mapping.select_next_item(),
    ['<C-p>'] = cmp.mapping.select_prev_item(),
    ['<C-b>'] = cmp.mapping.scroll_docs(-4),
    ['<C-f>'] = cmp.mapping.scroll_docs(4),
    ['<C-c>'] = cmp.mapping.complete(),
    ['<C-q>'] = cmp.mapping.close(),
    ['<Tab>'] = cmp.mapping.confirm({
      select = true,
    })
  },

  -- Autocomplete source
  sources = {
    -- { name = 'buffer' },
    { name = 'path' },
    { name = 'nvim_lsp' }
  },

  snippet = {
    expand = function()
    end,
  },

  documentation = {
    border = "rounded",
    winhighlight = "NormalFloat:CompeDocumentation,FloatBorder:CompeDocumentationBorder",
    max_width = 100,
    min_width = 60,
    max_height = math.floor(vim.o.lines * 0.3),
    min_height = 1,
  },

  -- Symbols via lspkind-nvim
  formatting = {
    format = function(entry, vim_item)
      vim_item.kind = require('lspkind').presets.default[vim_item.kind]

      -- Label the source
      vim_item.menu = ({
        buffer = "[Buffer]",
        nvim_lsp = "[LSP]",
        path = "[Path]",
        ultisnips = "[Snippet]",
      })[entry.source.name]

      return vim_item
    end
  }
})

-- nvim-compe (deprecated)
-- vim.o.completeopt = "menuone,noselect"

-- require('compe').setup {
--   enabled = true;
--   autocomplete = true;
--   debug = false;
--   min_length = 1;
--   preselect = 'enable';
--   throttle_time = 80;
--   source_timeout = 200;
--   incomplete_delay = 400;
--   max_abbr_width = 60;
--   max_kind_width = 70;
--   max_menu_width = 100;
--   documentation = {
--     border = "rounded",
--     winhighlight = "NormalFloat:CompeDocumentation,FloatBorder:CompeDocumentationBorder",
--     max_width = 100,
--     min_width = 60,
--     max_height = math.floor(vim.o.lines * 0.3),
--     min_height = 1,
--   };

--   source = {
--     path = true;
--     buffer = true;
--     ultisnips = true;
--     nvim_lsp = true;

--     -- disabled sources
--     tags = false;
--     snippets_nvim = false;
--     nvim_lua = false;
--     calc = false;
--     vsnip = false;
--     spell = false;
--   };
-- }

return M
