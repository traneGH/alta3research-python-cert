#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game using a while True loop."""
 
# standard library import
# allows us to generate UUIDs
import uuid
import os

# from python std library
import csv
from subprocess import call
import netifaces

# python3 -m pip install np
import numpy as np
# python3 -m pip install matplotlib
import matplotlib
 
# sudo apt install python3-tk
import matplotlib.pyplot as plt


def main(): # all code should appear ...
    ''' all functions have multiline comments '''
    my_string = "you code" # vars
    print(my_string)  # print to stand-out
    currentDir = os.getcwd()
    print("####currentDir: " + currentDir)
    matplotlib.use('Agg')

# calling main() using this technique
#if __name == "__main__":
main()
