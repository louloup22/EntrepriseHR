#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:51:53 2018

@author: LouiseP
"""
import socket
from threading import Thread

class Client(Thread):
    def __init__(self,host,port):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.liste_command=["ADD", "MIN", "TIM","DIV"]
        
    def run(self):
        connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_avec_serveur.connect((self.host, self.port))
        print("Connexion établie avec le serveur sur le port {}".format(self.host))
        print("HELLO")
        
        msg_a_envoyer = b""
        while msg_a_envoyer != b"QHT":
            msg_a_envoyer = input("> ")
            # Peut planter si vous tapez des caractères spéciaux
            msg_a_envoyer = msg_a_envoyer.encode()
            # On envoie le message
            connexion_avec_serveur.send(msg_a_envoyer)
            msg_recu = connexion_avec_serveur.recv(1024)
            print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents
        
        print("Fermeture de la connexion")
        connexion_avec_serveur.close()

host = "localhost"
port = 13000
client_thread=Client(host,port)
client_thread.start()