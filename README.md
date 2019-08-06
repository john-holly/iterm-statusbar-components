# iterm-xmax-counter

A days until christmas counter for iTerm.

Ryan, you can make it account for all future years :)

## Install

- Enable iTerm2's Python API
- Install iTerm2's Python Runtime
- Install packages using **iTerm's pip**
- Run `make install`

### Enable iTerm2's Python API

Preference Panel: **General > Magic > Enable Python API**

### Install iTerm2's Python Runtime

Menubar: **Scripts > Manage > Install Python Runtime**

### Install packages using **iTerm2's pip**

Use **iTerm2's pip** to install required packages.

```bash
~/Library/Application Support/iTerm2/iterm2env/versions/3.7.2/bin/pip install -r requirements.txt
```

### Install using make

```bash
make install
```

### Uninstall using make

```bash
make uninstall
```
