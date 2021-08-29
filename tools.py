import sys, os
import platform
from pathlib import Path
from config import r_config, w_config, OCR_CONFIG, PATHS_CONFIG
from tkinter import *
from tkinter.filedialog import askopenfile

try:
    is_compiled_with_pyinstaller = (sys._MEIPASS is not None)
    if is_compiled_with_pyinstaller:
        bundle_dir = sys._MEIPASS
except AttributeError:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
    
OSX_TESSERACT_VERSION = "4.1.1"
WIN_TESSERACT_DIR = Path(bundle_dir, "resources", "bin", "win", "tesseract")
OSX_TESSERACT_DIR = Path(bundle_dir, "resources", "bin", "mac", "tesseract", OSX_TESSERACT_VERSION)

def path_to_ffmpeg():
    platform_name = platform.system()
    if platform_name == 'Windows':
        return str(Path(bundle_dir, "resources", "bin", "win", "ffmpeg", "ffmpeg.exe"))
    elif platform_name == 'Darwin':
        return str(Path(bundle_dir, "resources", "bin", "mac", "ffmpeg", "ffmpeg"))
    return ''

def path_to_ffmpeg_folder():
    return str(Path(path_to_ffmpeg()).parent)

def path_to_tesseract():
    exec_data = {"Windows": str(Path(WIN_TESSERACT_DIR, "tesseract.exe")),
                    "Darwin": str(Path(OSX_TESSERACT_DIR, "bin", "tesseract")),
                    "Linux": "/usr/local/bin/tesseract"}
    platform_name = platform.system()  # E.g. 'Windows'
    return exec_data[platform_name], platform_name

def get_tessdata_dir_cmdline_arg():
    platform_name = platform.system()
    if platform_name == 'Darwin':
        return '--tessdata-dir {}'.format(str(Path(OSX_TESSERACT_DIR, "share", "tessdata")))
    # Since we store the tessdata right by the executable on win, we don't need to pass in a string.
    return ''

def path_to_textractor():
    path = r_config('PATHS', 'textractor')
    return path if path != 'default' else str(Path(bundle_dir, 'resources', 'bin', 'win', 'textractor', 'TextractorCLI.exe'))

def path_to_wexpect():
    return str(Path(bundle_dir, 'resources', 'bin', 'win', 'wexpect', 'wexpect.exe'))

def open_folder_textractor_path():
    root = Tk()
    root.withdraw()
    file = askopenfile(filetypes = (("EXE files","*.exe"),("all files","*.*")), defaultextension=".exe")
    if not file:
        return
    try:
        w_config(PATHS_CONFIG, {'textractor': file.name})
    except:
        print('File not selected')
    file.close()
    root.destroy()
    return file.name