# Game2Text

![image](https://user-images.githubusercontent.com/13146030/117099796-b3efa180-ada4-11eb-8c68-431dfa0acdb5.png)

[Game2Text](https://www.game2text.com) is an all-in-one application that helps you learn languages from the games you play.

## Platforms
- Windows 10
- Mac OSX Mojave, Catalina

## Text Extraction Modes
- Classic OCR with Tesseract, Tesseract Legacy, or OCR Space.
- OCR-assisted game script matching
- Text hooking (for Visual Novels)
- Clipboard to Game2Text

## Features
- Dictionary lookup with browser dictionaries like Yomichan and Rikaichan
- Translation tools including DeepL, Papago, and Google Translate.
- Create game flashcards with screenshot and game audio via Anki and AnkiConnect

## Download 
[Download Game2Text](https://game2text.com/download/) 

## User Guide
[Read User Guide](https://game2text.com/user-guide/quick-start/)

## FAQ
[Read FAQ](https://game2text.com/faq/switch-browser/)

## Development

Create a venv and activate it.

```bash
virtualenv venv --python=python3.7
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
python game2text.py
```

## Extra Packages for Windows Development

1. Install [C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

2. Install *pyaudio_portaudio* through wheel. This package includes **as_loopback** as an option to record system audio through *Windows WASAPI*. 
```
pip uninstall pyaudio
pip install https://github.com/intxcc/pyaudio_portaudio/releases/download/1.1.1/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
```

3. Install the wexpect library for running the text hooker program.
```
pip install wexpect==4.0.0
```

## Extra Packages for Linux Development

Install Tesseract by following the installation instructions [here](https://tesseract-ocr.github.io/tessdoc/Home.html).

## Distribution

Unzip *resources/sudachidict_small.zip* into the same directory.

Windows: 

```build.bat```

Mac:

```sh build.sh```

Temporary fix for all read/write operations using *os.path* on Mac builds with pyinstaller: create a wrapper file that runs the Game2Text executable inside the package

## Acknowledgement

#### Tools

| Tool | Description | Version |
| :---: | :---: | :---: |
| [Python Eel](https://github.com/ChrisKnott/Eel)  | Electron-like Library for Python | 0.14.0 |
| [Tesseract](https://github.com/tesseract-ocr/tesseract)  | OCR Tool | 4.1.1 |
| [AnkiConnect](https://github.com/FooSoft/anki-connect) |  Anki Remote API Extension | / |
| [SudachiPy](https://github.com/WorksApplications/SudachiPy)  |  Japanese Morphological Analyzer | 0.5.2 |
| [Textractor](https://github.com/Artikash/Textractor) |  Texthooker | 4.16.1 |
| [FFmpeg](https://www.ffmpeg.org/) |  Audio Converter | 4.4 |



#### Resources

Jun Mako (Game Scripts)

Unboxious (Game Scripts)

