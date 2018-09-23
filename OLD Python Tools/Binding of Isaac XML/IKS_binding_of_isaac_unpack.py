# -*- coding: utf-8 -*-

#Tested on Python 2.7.5
#Author of this code: Bartlomiej Duda
#Contact: https://www.facebook.com/ikskoks
#This code/python script is for personal use ONLY
#It was made for XENTAX users



import argparse
import os
import sys
import time
import struct
import binascii

lokalizacja_skryptu = os.path.dirname(os.path.abspath(__file__))
parser = argparse.ArgumentParser()
parser.add_argument("folder_CONFIG", help="Sciezka do folderu CONFIG")

args = parser.parse_args()
(sciezka_CONFIG, nazwa_CONFIG) = os.path.split(args.folder_CONFIG)
(Krotka_nazwa_CONFIG, extension) = os.path.splitext(nazwa_CONFIG) 
sciezka_do_CONFIG = args.folder_CONFIG

nazwa_skryptu = "corrossion_skrypt.txt"
pelna_sciezka_skryptu = os.path.join(os.path.abspath(lokalizacja_skryptu), nazwa_skryptu)
dane_skryptu = "dane_skryptu.txt"
pelna_sciezka_danych = os.path.join(os.path.abspath(lokalizacja_skryptu), dane_skryptu)

skrypt = open(pelna_sciezka_skryptu, 'wt')
dane = open(pelna_sciezka_danych, 'wt')

for root, subFolders, files in os.walk(sciezka_do_CONFIG): 
    for file in files:    
        (Krotka_nazwa_pliku, rozszerzenie_pliku) = os.path.splitext(file) 
        if rozszerzenie_pliku == '.xml':
            aktualny_plik = os.path.join(root,file)
            with open(aktualny_plik, "rt") as aktualny_plik:
                
                
                caption = "name"
                string = ""
                i = 0
                while 1:
                    i = i +1
                    line = aktualny_plik.readline()
                    if not line:break
                    string += line
                    if string.find(caption) != -1:
                        (czytany_caption, wlasciwy_tekst, koncowka_caption) = line.split("\"", 3)
                        if wlasciwy_tekst != "":
                            print wlasciwy_tekst
                            skrypt.write(wlasciwy_tekst)
                            skrypt.write('\n')
                            dane.write(os.path.join(root,file)), dane.write("\xFF"), dane.write(wlasciwy_tekst), dane.write("\xFF"), dane.write(str(i))
                            dane.write('\n')
                        
                    string = "" 
                aktualny_plik.close()
                    


