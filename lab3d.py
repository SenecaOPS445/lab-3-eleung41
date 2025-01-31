#!/usr/bin/env python3
'''Lab 3 Disk Space script using df and awk'''
# Author ID: 147724231

import os

def free_space():
    # Run the shell command to get the free space on the root directory
    result = os.popen("df -h | grep '/$' | awk '{print $4}'").read().strip()
    
    # Return the result as a string in utf-8 format
    return result.encode('utf-8').decode('utf-8')

if __name__ == '__main__':
    # Output the free space in root directory
    print(free_space())

