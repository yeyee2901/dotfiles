" For common knowledge such as technologies, etc
let knowledge = {}
let knowledge.ext = '.wiki'
let knowledge.path = '~/knowledge-wiki/'
let knowledge.template_path = '~/knowledge-wiki/'
let knowledge.template_ext = '.html'
let knowledge.template_default = 'my-wiki'
let knowledge.path_html = '~/knowledge-wiki/docs/'
let knowledge.automatic_nested_syntaxes = 1

" For academic purposes
let academy = {}
let academy.ext = '.wiki'
let academy.path = '~/academy-wiki/'
let academy.template_path = '~/academy-wiki/'
let academy.template_ext = '.html'
let academy.template_default = 'my-wiki'
let academy.automatic_nested_syntaxes = 1
let academy.path_html = '~/academy-wiki/docs/'

" For embedded system & Arduino related things
" Project to come
let arduino_wiki = {}
let arduino_wiki.path = '~/arduino-wiki/'
let arduino_wiki.automatic_nested_syntaxes = 1
let arduino_wiki.path_html = '~/arduino-wiki/docs/'
let arduino_wiki.ext = '.wiki'
let arduino_wiki.template_path = '~/.config/nvim/VimWiki/'
let arduino_wiki.template_ext = '.tpl'
let arduino_wiki.template_default = 'syntax-highlighted'

let g:vimwiki_list = [knowledge,academy, arduino_wiki]
