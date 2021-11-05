local pickers = require('telescope.pickers')
local finders = require('telescope.finders')
local actions = require('telescope.actions')
local actions_state = require('telescope.actions.state')
local sorters = require('telescope.sorters')

local todo = {

  -- I just pre-instantiated it
  -- so I know what the todo class hass
  picker = {},
  results = {},

  opts = {
    prompt_title = "< To Do List >",
    layout_strategy = "vertical",
    layout_config = {
      width = 0.5,
      height = 0.7,
      prompt_position = "top",
    },

    -- let's just use the generic fuzzy sorter
    sorter = sorters.get_generic_fuzzy_sorter({}),
    sorting_strategy = "ascending",

    -- pre-instantiate
    -- initialized when calling get_results()
    finder = {},

    attach_mappings = function(prompt_bufnr, map)
      return true
    end
  },
}

function todo:get_results()

  -- populate the results
  self.results = {"NOVEMBER", "DESEMBER"}
  self.opts.finder = finders.new_table(self.results)

  -- create the picker
  self.picker = pickers.new(self.opts)
  self.picker:find()
end

function todo:go_to_month()
end

todo:get_results()

return todo
