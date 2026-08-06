## Installation
Download the `MetalPipe.py` and audio file `ThePipe.ogg`

**You can use your own audio file** but make sure the filename is the same as "ThePipe.ogg" or change it directly in the code before executing it!
```bash
git clone https://github.com/finnhp01/SmallProyects/MetalPipe
```
Or just directly download the `MetalPipe.py` and `ThePipe.ogg` from [MetalPipe](MetalPipe)

Make sure you have **Python 3** (or newer) installed
---
### Linux/Windows/Powershell

```bash
python3 --version
```

```powershell
python --version
```

```powershell
py --version
```

## Installing python
#### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Windows

Download and install the latest version of Python from:

https://www.python.org/downloads/windows/

**Important:** During installation, check the box labeled **"Add Python to PATH"** before clicking **Install Now**.

---

### Install the required Python packages

**Linux**

```bash
python3 -m pip install pynput pygame
```

**Windows**

```powershell
python -m pip install pynput pygame
```

or, if you're using the Python launcher:

```powershell
py -m pip install pynput pygame
```
## PIPE!
Open a **terminal/command line** and make sure you are on the folder location of ```MetalPipe.py``` and run it with ```python3 MetalPipe.py```  make sure the audio file [ThePipe.ogg](MetalPipe/ThePipe.ogg) are in the same folder as the main python file and you properly installed the pynput and pygame libraries.


That's it, have fun :D!


### Extras:
On line `16` you can add this `3` lines to the on_press function:
```py
def on_press(key):
    global listener
    if key:
        print("Keyboard!")
        pipe.play()
    else:
        print("PIPE!")
    if key == keyboard.Key.esc:
        listener.stop()
        return False
```
This will basically make every single key in your keyboard play the sound. **PIPE CHAOS**
