# offkeyboard

This project allows operating a computer using a guitar, or bass guitar, or other instrument. Notes on the instrument can be mapped to 
key presses, key combos, or mouse movements/clicks. Check out [this tweet](https://twitter.com/phillipten/status/1124067445604483074?s=20) for a demo.

This software was used in the creation of these _epic_ YouTube videos:

[I Played Minecraft Using ONLY A Bass](https://www.youtube.com/watch?v=35My8fssgVw)

The project works by running fundamental-frequency estimation on microphone input, and mapping these to keyboard/mouse inputs. 
State is kept to ensure each played note is pressed only once (rather than the full note duration), to allow certain keys to be "held down" as long as the note is played,
to allow chorded keys/key combos to be entered, to detect when a note is stopped, etc.

## Configuration

Modify the note-mappings in [config.py](./offkeyboard/config.py) to configure what note maps to what keyboard or mouse action.
For more complicated configuration, you might need to modify the code in [keymaps.py](./offkeyboard/keymaps.py).

## Installation

1) Ensure you have Python 3 available on your system

2) Run the following shell commands (macOS):

```shell script
brew install portaudio
pipenv shell
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
pipenv install
```

3) Run offkeyboard:

```shell script
python offkeyboard/__init__.py
```

As long as the script is active, playing notes defined in the configuration will send the associated keyboard/mouse events to the OS.

Press CTRL+C to exit.

## Mouse Support

 changed out foohid library for some other libraries.  Will update the requirements for libraries later. to be clear. I'm not the original maker, of this program. I'm just someone who was frustrated with trying to get foohid on a Linux environment.

## License

MIT License
