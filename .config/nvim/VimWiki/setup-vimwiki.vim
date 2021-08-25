let wiki1 = {}
let wiki1.path = '~/vimwiki/'
let wiki1.automatic_nested_syntaxes = 1
let wiki1.path_html = '~/Documents/VimWiki/'
let wiki1.ext = '.wiki'
let wiki1.template_path = '~/.config/nvim/VimWiki/'
let wiki1.template_ext = '.tpl'
let wiki1.template_default = 'syntax-highlighted'

let arduino_wiki = {}
let arduino_wiki.path = '~/arduino-wiki/'
let arduino_wiki.automatic_nested_syntaxes = 1
let arduino_wiki.custom_wiki2html = '~/.config/nvim/VimWiki/wiki2HTML.sh'
let arduino_wiki.path_html = '~/Documents/Arduino-wiki/'
let arduino_wiki.ext = '.wiki'
let arduino_wiki.template_path = '~/.config/nvim/VimWiki/'
let arduino_wiki.template_ext = '.tpl'
let arduino_wiki.template_default = 'syntax-highlighted'

let g:vimwiki_list = [wiki1, arduino_wiki]
