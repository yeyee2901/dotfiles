# Dotfiles
My personal collection of dotfiles.


## Sync Dotfiles with remote
1. Pastikan di remote, ada _alias_ nya seperti ini:
```bash
#file: .zshrc
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```

 
2. Buat _.gitignore_ di $HOME (PENTING) Kalau tidak di ignore, nanti recursive, isi dengan:
```
.dotfiles
```

3. _clone_ dari remote
```bash
git clone --bare https://github.com/yeyee2901/dotfiles $HOME/.dotfiles
```


4. buat _alias_ sementara di shell session ini.
```bash
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```


5. _sync_ dengan checkout
```bash
dotfiles checkout 
```
* Step diatas kemungkinan besar akan gagal (_uncommited files_)
* Bisa jadi karena sudah ada file _.zshrc_, _.gitignore_, etc.. 
  di system, remove it.

7. Set dotfiles agar tidak show  _untracked files_
```bash
dotfiles config --local status.showUntrackedFiles no
```  
