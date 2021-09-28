#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 06:32:48 2020

@author: uttkarshchaurasia
"""

#Importing the Libraries
import os, io
from google.cloud import vision
import tkinter as tk
from tkinter import filedialog

#Creating local environment
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] ="UttkarshChaurasiaVision.json"

client = vision.ImageAnnotatorClient()

#Image to Text Conversion
def image_to_text(FILE, FINAL):
    with io.open(FILE, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image)
    docText = response.full_text_annotation.text
    f = open(FINAL + '/' + FILE.split('/')[-1].split('.')[0] +".txt", "x")
    f.write(docText)
    f.close()
    

#Reading from the User Defined Directory
root = tk.Tk()    
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
files = filedialog.askopenfilename(multiple=True) 
var = root.tk.splitlist(files)
filePaths = []
for f in var:
    filePaths.append(f)
filePaths

#Reading the Final Directory from user
final_folder = filedialog.askdirectory()

for file in filePaths:
    image_to_text(file, final_folder)
    





