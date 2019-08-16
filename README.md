# iterm-statusbar-components

This repository contains status bar indicators for:

* Days until Christmas
* Days of employment

## Configuration

To configure the days of employment statusbar indicator's date, open `components/iterm-captains-log.py` and modify `employed_at` to your start-date.

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
