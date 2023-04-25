#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi, cgitb, os, sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import pandas as pd

TESTS_DIR = "./tests"
SUBMITS_DIR = "./submits"
MAIN_PAGE = "../main.html"

def load_file():
    form = cgi.FieldStorage()

    form_file = form['file']

    if not form_file.file:
        return pd.DataFrame(), False

    if not form_file.filename:
        return pd.DataFrame(), False

    file_name = os.path.basename(form_file.filename)
    uploaded_file_path = os.path.join(TESTS_DIR, file_name)
    with open(uploaded_file_path, 'wb') as fout:
        while True:
            chunk = form_file.file.read(100000)
            if not chunk:
                break
            fout.write(chunk)
    
    return pd.read_parquet(uploaded_file_path), True

def analyse(test):
    #TODO: link model
    return pd.read_csv(os.path.join(SUBMITS_DIR,"test_submit_example.csv"))

print('Content-Type: text/html; charset=UTF-8')
print()
print('<html>')
print('<head><title>Upload File</title><meta charset="utf-8"></head>')
print('<body><center>')

cgitb.enable()
test, loaded = load_file()

if not loaded:   
    print('<div><label>Файл не был загружен/lable></div>')
else:
    if test.columns.size == 0 or test[test.columns[0]].count() == 0:
        print('<div><label>Файл пуст</lable></div>')
    else:
        submit = analyse(test)
        print('<div><label>В файле ',test[test.columns[0]].count(),' строк</lable></div>')

print('<div><a href="',MAIN_PAGE,'">Назад</a></div>')
print('</center></body></html>')