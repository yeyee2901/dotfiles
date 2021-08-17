require('nvim-treesitter.configs').setup {

	ensure_installed = "maintained",

	highlight = {
		enable = true,

    -- ISSUE: Breaks some text highlighting
    disable = { "markdown", "latex", "html" },
		additional_vim_regex_highlighting = false,
	},

	indent = {
		enable = true,
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
