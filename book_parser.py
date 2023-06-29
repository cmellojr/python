#!/usr/bin/python3

with open("txt/dracula.txt") as f:
    contents = f.readlines()
    for item in contents:
        print(item.rstrip())
