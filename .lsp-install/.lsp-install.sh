#!/bin/bash

# Language Servers from NPM registry
npm i -g install \
    bash-language-server \
    diagnostic-languageserver \
    intelephense \
    live-server \
    pyright \
    serve \
    sql-language-server \
    typescript \
    typescript-language-server \
    vim-language-server \
    vscode-langservers-extracted

# Language Servers from APT repository
sudo apt install ccls

# Language Servers from PIP registry
pip install cmake-language-server

# Language Servers from Rust Crates
cargo install tectonic rust_analyzer
cargo install --git https://github.com/latex-lsp/texlab.git --locked
