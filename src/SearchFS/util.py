#!/usr/bin/env python

import os

ORIGINAL_DIR="/.searchfs_original_dir"

def filenamepart(path):
    return path.rsplit('/', 1)[-1]

def pathpart(path):
    return path.rsplit('/', 1)[-1]

def pathparts(path):
    return path.split('/')[1:]

def flag2mode(flags):
    md = {os.O_RDONLY: 'r', os.O_WRONLY: 'w', os.O_RDWR: 'w+'}
    m = md[flags & (os.O_RDONLY | os.O_WRONLY | os.O_RDWR)]
    if flags | os.O_APPEND:
        m = m.replace('w', 'a', 1)
    return m

def increasefilename(filename):
    # FIXME make this function better
    return filename + '(1)';

def addtrailingslash(path):
    return '/' + path;

def getbasefilelist():
    return getbasefilemap().keys()

def getbasefilemap():
    return { '/..': '..', '/.': '.' }
