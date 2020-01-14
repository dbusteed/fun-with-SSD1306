# fun times with SSD1306

random collection of programs I wrote to work with the SSD1306 (128 x 32) LED screen for Raspberry Pi

uses Adafruit CircuitPython driver found [here](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306)

## setup

1. plug in your SSD1306 to RPi

2. get the code
  ```
  git clone https://github.com/dbusteed/fun-with-SSD1306
  cd fun-with-SSD1306
  pip3 install adafruit-circuitpython-ssd1306
  ```

3a. run each script with
  ```
  python3 SCRIPT_NAME.py
  ```

3b. or run them as executables
  ```
  chmod +x *.py
  ./SCRIPT_NAME.py
  ```

## contents

**`clear.py`**

* clears the LED screen

**`game.py`**

* a "dino-runner" game.
* hit any key on the keyboard to hop over the incoming obstacles. 
* **NOTE**: the `pynput` module doesn't like it when you run this thru SSH, so you gotta use VNC or run on the RPi directly

**`logger.py`**

* prints out messages from a log file.
* updated in "real-time". 
* you can set the log file in the script, then display cool log info automatically

**`message.py`**

* write a custom message to the screen. 
* pass in the parameter as a script argument:
  * `python3 message.py "hello everyone!"`
