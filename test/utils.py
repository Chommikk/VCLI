import os
import re

def get_all_files(path = None):
    text = str()
    if (path == None):
        path = os.getcwd()
    for filename in os.listdir(path):
        if os.path.isfile(filename):
            try:
                f = open(filename, 'r')
                content = f.read()
                text = text + f"