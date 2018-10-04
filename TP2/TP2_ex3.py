#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:27:17 2018

@author: LouiseP
"""

import random
import time
from threading import Thread, Event
from datetime import datetime

liste_verrou=[]
for i in range(11):
    verrou=Event()
    liste_verrou.append(verrou)
liste=[]

class Producteur(Thread):
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
         for i in range(1,11): 
            while not liste_verrou[i-1].isSet():
                liste_verrou[i-1].wait(1)
                attente = 1.0
                attente+= random.randint(0, 200) / 100
                time.sleep(attente)
                #print("{} ajouté à {}".format(i,liste))
                liste.append(i)
                liste_verrou[i-1].set()
                
class Consommateur(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        for i in range(1,11):
            a=datetime.now()
            while not liste_verrou[i-1].isSet():
                liste_verrou[i-1].wait(4)
                if len(liste)>0:
                    liste_verrou[i-1].set()
                    attente = 1.0
                    attente+= random.randint(0, 200) / 100
                    time.sleep(attente)
                    print(liste[0])
                    liste.pop(0)
                    b=datetime.now()
                    #display time taken
                    print(b-a)

thread_1=Producteur()
thread_2=Consommateur()
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()