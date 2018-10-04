#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 17:10:30 2018

@author: LouiseP
"""

##VERSION AMELIOREE 2

from threading import Thread, RLock


verrou = RLock()
class Compteur(Thread):
    _compteur=0
    def __init__(self):
        Thread.__init__(self)
        

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        for i in range(10000):
            with verrou:
                Compteur._compteur+=1
        
        for i in range(10000):        
            with verrou:
                Compteur._compteur-=1
        Compteur._compteur+=1
        
liste=[]
# Création des threads
#si erreur avec 10000 testez avec 1000 ou moins
for i in range(10000):
    thread=Compteur()
    thread.start()
    liste.append(thread)
    
for element in liste:
    element.join()

print(Compteur._compteur)


