# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

import shutil
import tempfile
import urllib.request
import time
import math
from datetime import datetime as dt
import sys
import greet

#1
with urllib.request.urlopen('https://en.wikipedia.org/wiki/Zen_of_Python') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass

#2
def wait(second):
    time.sleep(second)

#3
def my_sin(x):
    return math.sin(x)

#4
def iso_now():
    return dt.now().strftime("%Y-%m-%dT%H:%M")
#5
def platform():
    return sys.platform

#5
def supergreeting_wrapper(name):
    return greet.supergreeting(name)


if __name__== "__main__":
    print(wait(1))
    print(my_sin(5))
    print(iso_now())
    print(platform())
    print(supergreeting_wrapper("Frans"))