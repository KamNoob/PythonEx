#! python3
#   mapIt.py - Launches a map in the browserusing address from the command line or clipboard
#   For command line arguement use D:\PythonEx\myenv\mapIt.py in venv command line then the address.

import webbrowser
import sys
import pyperclip

#   Handle command line argument
if len(sys.argv) > 1:
    #   Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')
