# B"H





## TO DO ON NEW MACHINE


--- --- --- --- --- --- --- --- --- --- ---
### Step 1:
- Install Chrome
- Easily done following browser instructions
- Add to Dock
- Login to Google with ylazerson@gmail.com login
- Add Extensions:
    1. LastPass
    2. TabCopy
    3. Vimium


--- --- --- --- --- --- --- --- --- --- ---
### Step 2:
- Install `git`

```sh
cp ~/repos/repos-other/comp-config/config-files/.gitconfig ~/.gitconfig
```

--- --- --- --- --- --- --- --- --- --- ---
### Step 3:
- Using Chrome login to GitHub
- Generate SSH Key for GitHub
- Follow GitHub online instructions


--- --- --- --- --- --- --- --- --- --- ---
### Step 4:

#### Initial repos to get started:
```sh
mkdir ~/repos
mkdir ~/repos/repos-other

cd ~/repos/repos-other

git clone git@github.com:Ylazerson/comp-config.git
git clone git@github.com:Ylazerson/laz-main.git
```

- Open this `01-setup-machine.md` to "follow along"


--- --- --- --- --- --- --- --- --- --- ---
### Step 5:

#### Next repos:
```sh
mkdir ~/repos/go-workspace
mkdir ~/repos/x-large-files
```

Clone relevant _personal_ repos utilizing `comp-config/os-agnostic/clone-repos.md`


--- --- --- --- --- --- --- --- --- --- ---
### Step 6: Copy config files

- Besides below, any others need to be copied over?

```
mkdir ~/bin
cp ~/repos/repos-other/comp-config/config-files/home-bin/* ~/bin

mkdir ~/app-keys
cp ~/repos/repos-other/comp-config/config-files/home-app-keys/* ~/app-keys
```








--- --- --- --- --- --- --- --- --- --- ---
--- --- --- --- --- --- --- --- --- --- ---
            INTERLUDE FOR ....
               INTSIGHTS               
--- --- --- --- --- --- --- --- --- --- ---

**Google**
Add login yisroel.lazerson@intsights.com 


**Login to GitHub**
Login to https://github.com/izzy-lazerson


**Add SSH Key to GitHub**
https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh

When it asks to save to file, save to `/home/bizon/.ssh/id_rsa_intsights`


**Clone Repos**

```sh
git clone git@github.com:Intsights/backend.git ~/backend
```

Clone relevant _intsights_ repos utilizing `comp-config/os-agnostic/clone-repos.md`


**Slack**

`sudo snap install slack --classic`


--- --- --- --- --- --- --- --- --- --- ---
--- --- --- --- --- --- --- --- --- --- ---
--- --- --- --- --- --- --- --- --- --- ---





--- --- --- --- --- --- --- --- --- --- ---
### Step 7 - Install Google Cloud SDK

https://cloud.google.com/sdk/docs/downloads-snap

```sh
snap install google-cloud-sdk --classic

# Sign-in using IntSights Google account:
gcloud auth login
gcloud auth list

gcloud init
```










--- --- --- --- --- --- --- --- --- --- ---
### Step 8: `.bashrc`

- Just add two lines to bottom of `.bashrc`: 

```sh
source ~/.commonrc
source /snap/google-cloud-sdk/current/completion.bash.inc
``` 

- USE THEIRS (bizon's) NOT MINE!!!!!!
- Then copy that `.bashrc` back here.


FOR BIZON-OS DO NOT USE ZSH!





--- --- --- --- --- --- --- --- --- --- ---
### Step 9:


```sh
cp ~/repos/repos-other/comp-config/config-files/.bashrc    ~
cp ~/repos/repos-other/comp-config/config-files/.commonrc  ~  
cp ~/repos/repos-other/comp-config/config-files/.gitconfig ~
cp ~/repos/repos-other/comp-config/config-files/.tmux.conf ~
cp ~/repos/repos-other/comp-config/config-files/.zshrc     ~
```

Restart terminal




--- --- --- --- --- --- --- --- --- --- ---
### Step 10:
- Install VS Code

Run `install-vscode-extensions.sh`
- Make sure nothing failed.


Then:
```sh
cp ~/repos/repos-other/comp-config/vscode-config/*.json ~/.config/Code/User
cp ~/repos/repos-other/comp-config/vscode-config/snippets/* ~/.config/Code/User/snippets
```

Close vscode, restart terminal, then `cwsconf`



--- --- --- --- --- --- --- --- --- --- ---
### Step 11:
Install anaconda
- Do not use `sudo` when installing.
- https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html




--- --- --- --- --- --- --- --- --- --- ---
### Step 12 - Install fzf 

Use repo approach: https://github.com/junegunn/fzf#using-git

```
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf

~/.fzf/install

```


--- --- --- --- --- --- --- --- --- --- ---
### Step 12:
- Install `tmux`

```sh
sudo apt install tmux
```

- Install `tpm`, [TMUX Package Manager](https://github.com/tmux-plugins/tpm)


- Run `tmux`
- Hit `ctrl+z r` then `ctrl+z shift+i` (don't wait too long between key strokes ...)
- You should now be able to use all the plugins: `ls ~/.tmux/plugins`


![tmux](img/tmux.png)


--- --- --- --- --- --- --- --- --- --- ---
### Step 13: Setup the tmux sessions:

Detach from tmux.


```sh
alias | grep 'tmux a'

# -- ----------------------------- 
tmux new -s front-end
# Detach
tmux new -s go
# Detach
tmux new -s intsights
# Detach
tmux new -s vc
# Detach
tmux new -s yi
# Detach
```

- Ensure tmux-resurrect is working. It should work without any further tweaks B"H.




--- --- --- --- --- --- --- --- --- --- ---
### Step 14: Install `tree` 

```sh
snap install tree
tree --version
```


--- --- --- --- --- --- --- --- --- --- ---
### Step 15:
- Install `htop`


--- --- --- --- --- --- --- --- --- --- ---
### Step 16: NOT DONE YET - THINK ABOUT IT ......
    - Install Shutter using the Ubuntu GUI installation from software center
    - Set keyboard-shortcut [](img/shutter-keyboard-shortcut.png)
    - Enable edit option in Shutter in Ubuntu:
        - https://itsfoss.com/shutter-edit-button-disabled/



--- --- --- --- --- --- --- --- --- --- ---
### Step 17
Install Docker:
- https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
- Follow steps:
    - Step 1 - Installing Docker
    - Step 2 - Executing the Docker Command Without Sudo (Optional)


--- --- --- --- --- --- --- --- --- --- ---
### Step 18
Install `jq`


--- --- --- --- --- --- --- --- --- --- ---
### Step 19 
Install `netstat`


--- --- --- --- --- --- --- --- --- --- ---
### Step 20 - Hide side-panel

https://www.maketecheasier.com/hide-top-bar-ubuntu/

Ignore section on hiding top bar for now.



--- --- --- --- --- --- --- --- --- --- ---
### Step 21 - Install Signal 

```
sudo snap install signal-desktop
```






--- --- --- --- --- --- --- --- --- --- ---
--- --- --- --- --- --- --- --- --- --- ---
--- --- --- --- --- --- --- --- --- --- ---










--- --- --- --- --- --- --- --- --- --- ---
               NOT DONE YET
--- --- --- --- --- --- --- --- --- --- ---
### Step 22:
- Install Node.js
- https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-18-04



### Step 23:
- Bring down, from GCS, all the `x-large-files` etc.


### Step 24
- Using Ubuntu Software tool install Postman
- Sign-in using Google


### Step 25 - Install Prince
- https://www.princexml.com/download/
- Install using Red-Hat `rpm` version



### Step 26 - Install MongoDB





