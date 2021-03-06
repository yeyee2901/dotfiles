require('nvim-treesitter.configs').setup {

	-- ensure_installed = "maintained",

	highlight = {
		enable = true,

    -- ISSUE: Markdown Breaks some text highlighting
    -- For some reason, php has better syntax highlighting without TS,
    -- might be an issue for my colorscheme though
    disable = { "markdown", "latex", "html", "php" },
		additional_vim_regex_highlighting = false,
	},

	indent = {
		enable = false,
	},

  incremental_selection = {
    enable = true,
    keymaps = {
      init_selection = 'gnn',
      node_incremental = 'grn',
      scope_incremental = 'grc',
      node_decremental = 'grm'
    }
  },

  -- Custom text objects
  textobjects = {
    select = {
      enable = true,
      lookahead = true,

      keymaps = {

        -- around function
        ['af'] = '@function.outer',

        -- inside function
        ['if'] = '@function.inner',

        -- around class
        ['ac'] = '@class.outer',

        -- inside class
        ['ic'] = '@class.inner',

      }
    }
  }
}
