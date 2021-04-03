#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

class fileListCreator(object):
    
    def __init__(self):
        self.__fileDict={}
        self.__fileTypesDict={
            'Pics' : ['png', 'jpg', 'jpeg', 'tif', 'cdr'],
            'Videos' : ['mp4'],
            'Docs' : ['pdf', 'docx', 'doc'], 
            'Data' : ['xslm', 'out', 'dat', 'txt', 'csv'],
            'Python' : ['py'], 
            'Arburg' : ['bpprof', 'afm'], 
            'FFF' : ['gcode', 'fff', 'factory']}
        
    def findFiles(self, path):
        pass