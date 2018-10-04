#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 14:15:26 2018

@author: LouiseP
"""

## Version améliorée 2

import random
from threading import Thread,BoundedSemaphore
import time

# possible d'imprimer 2  docs a la fois
verrou = BoundedSemaphore(2)

class Imprimante(Thread):
    _counter=0
    def __init__(self):
        Thread.__init__(self)
        self.id=Imprimante._counter
        Imprimante._counter+=1

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        nb_page=random.randrange(1,10)
        with verrou:
            for i in range(1,nb_page+1):
                print("Thread <#{0}> : page <#{1}>      ".format(self.id,i))
                attente = 0.5
                time.sleep(attente)


        
liste=[]
# Création des threads
for i in range(1,11):
    thread=Imprimante()
    thread.start()    
    liste.append(thread)
    
for el in liste:
    el.join()
    

    



