#! /usr/bin/env python3

import os, requests

directory = r'file-directory'
URL = r'http://XXX/'
dictionary = {}
objects = ["title","name","date","feedback"]

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory,filename)) as file:
            ref = 0
            for line in file:
                dictionary[objects[ref]] = line.rstrip('\n)
                 ref += 1
            res = requests.post(URL, json = dictionary)
