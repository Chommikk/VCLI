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
                text = text + f"|||{filename}|||" + content
            except:
                text= text
        if os.path.isdir(filename):
            text = text + get_all_files(filename)
    return text


def recreate_files(text):
    pattern = re.compile(r"\|\|\|(.*?)\|\|\|")
    parts = pattern.split(text)

    for i in range(1, len(parts), 2):
        filename = parts[i].strip()
        content = parts[i + 1] if i + 1 < len(parts) else ""

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content.strip())

#add reading from subdirectories and recreating subdirectories
