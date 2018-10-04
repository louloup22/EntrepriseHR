#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 10:53:28 2018

@author: LouiseP
"""

import socket
import select
import re
from threading import Thread

#EXERCICE 1 

class Serveur(Thread):
    def __init__(self,host,port):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.liste_command=["ADD", "MIN", "TIM","DIV"]

        
    def run(self):
        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_principale.bind((self.host, self.port))
        connexion_principale.listen(5)
        print("Le serveur écoute à présent sur le port {}".format(self.port))         
        serveur_lance = True
        clients_connectes = []
        while serveur_lance:
            #On va vérifier que de nouveaux clients ne demandent pas à se connecter
            #Pour cela, on écoute la connexion_principale en lecture
            #On attend maximum 50ms
            connexions_demandees, wlist, xlist = select.select([connexion_principale],
                [], [], 0.05)
            
            for connexion in connexions_demandees:
                connexion_avec_client, infos_connexion = connexion.accept()
                
                # On ajoute le socket connecté à la liste des clients
                clients_connectes.append(connexion_avec_client)
            
            # Maintenant, on écoute la liste des clients connectés
            # Les clients renvoyés par select sont ceux devant être lus (recv)
            # On attend là encore 50ms maximum
            # On enferme l'appel à select.select dans un bloc try
            # En effet, si la liste de clients connectés est vide, une exception
            # Peut être levée
            clients_a_lire = []
            try:
                clients_a_lire, wlist, xlist = select.select(clients_connectes,
                        [], [], 0.05)
            except select.error:
                pass
            else:
                #On parcourt la liste des clients à lire
                for client in clients_a_lire:
                    # Client est de type socket
                    #client.send(b"HELLO")
                    msg_recu = client.recv(1024)
                    # Peut planter si le message contient des caractères spéciaux
                    msg_recu = msg_recu.decode()
                    print("Reçu {}".format(msg_recu))
                    #client.send(b"5 / 5")
                    if msg_recu == "HLO":
                        client.send(b"Ready to calculate:write ADD, MIN ,TIM ,DIV. Waiting for yout command with 2 floats (no space after last float)")
                    if msg_recu == "QHT":
                        serveur_lance = False
                    else: 
                        if msg_recu.startswith("ADD"):
                            liste=re.findall(r"[-+]?\d*\.\d+|\d+",msg_recu)
                            msg_recu=msg_recu.replace("ADD ","")
                            if len(liste)==2:
                                msg_recu=msg_recu.replace(liste[0]+" ","")
                                msg_recu=msg_recu.replace(liste[1],"o")
                                print(msg_recu)
                                if msg_recu!="o":
                                    client.send(b"Commande incomprise")
                                else:
                                    a=float(liste[0])+float(liste[1])
                                    resultat="{}".format(a)
                                    client.send(resultat.encode())
                            else:
                                client.send(b"ERROR")
                        elif msg_recu.startswith("MIN"):
                            liste=re.findall(r"[-+]?\d*\.\d+|\d+",msg_recu)
                            msg_recu=msg_recu.replace("MIN ","")
                            if len(liste)==2:
                                msg_recu=msg_recu.replace(liste[0]+" ","")
                                msg_recu=msg_recu.replace(liste[1],"o")
                                print(msg_recu)
                                if msg_recu!="o":
                                    client.send(b"Commande incomprise")
                                else:
                                    a=float(liste[0])-float(liste[1])
                                    resultat="{}".format(a)
                                    client.send(resultat.encode())
                            else:
                                client.send(b"ERROR")
                        elif "TIM" in msg_recu:
                            liste=re.findall(r"[-+]?\d*\.\d+|\d+",msg_recu)
                            msg_recu=msg_recu.replace("TIM ","")
                            if len(liste)==2:
                                msg_recu=msg_recu.replace(liste[0]+" ","")
                                msg_recu=msg_recu.replace(liste[1],"o")
                                print(msg_recu)
                                if msg_recu!="o":
                                    client.send(b"Commande incomprise")
                                else:
                                    a=float(liste[0])*float(liste[1])
                                    resultat="{}".format(a)
                                    client.send(resultat.encode())
                            else:
                                client.send(b"ERROR")
                        elif "DIV" in msg_recu:
                            liste=re.findall(r"[-+]?\d*\.\d+|\d+",msg_recu)
                            msg_recu=msg_recu.replace("DIV ","")
                            if len(liste)==2:
                                msg_recu=msg_recu.replace(liste[0]+" ","")
                                msg_recu=msg_recu.replace(liste[1],"o")
                                print(msg_recu)
                                if msg_recu!="o":
                                    client.send(b"Commande incomprise")
                                else:
                                    a=float(liste[0])/float(liste[1])
                                    resultat="{}".format(a)
                                    client.send(resultat.encode())
                            else:
                                client.send(b"ERROR")
                        else:
                            client.send(b"Commande incomprise")
        print("Fermeture des connexions")
        for client in clients_connectes:
            client.close()
        connexion_principale.close()

#A décommenter si utilisation du serveur normal
"""
host = ''
port = 13000
newthread = Serveur(host,port)
newthread.start()
"""


# EXERCICE 2

class Serveur_polonais(Thread):
    def __init__(self,host,port):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.liste_command=["ADD", "MIN", "TIM","DIV"]
        
    def run(self):
        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_principale.bind((self.host, self.port))
        connexion_principale.listen(5)
        print("Le serveur écoute à présent sur le port {}".format(self.port))         
        serveur_lance = True
        clients_connectes = []
        while serveur_lance:
            #On va vérifier que de nouveaux clients ne demandent pas à se connecter
            #Pour cela, on écoute la connexion_principale en lecture
            #On attend maximum 50ms
            connexions_demandees, wlist, xlist = select.select([connexion_principale],
                [], [], 0.05)
            
            for connexion in connexions_demandees:
                connexion_avec_client, infos_connexion = connexion.accept()
                
                # On ajoute le socket connecté à la liste des clients
                clients_connectes.append(connexion_avec_client)
                #connexion_avec_client.send(b"HELLO")
            
            # Maintenant, on écoute la liste des clients connectés
            # Les clients renvoyés par select sont ceux devant être lus (recv)
            # On attend là encore 50ms maximum
            # On enferme l'appel à select.select dans un bloc try
            # En effet, si la liste de clients connectés est vide, une exception
            # Peut être levée
            clients_a_lire = []
            try:
                clients_a_lire, wlist, xlist = select.select(clients_connectes,
                        [], [], 0.05)
            except select.error:
                pass
            else:
                #On parcourt la liste des clients à lire
                for client in clients_a_lire:
                    msg_recu = client.recv(1024)
                    # Peut planter si le message contient des caractères spéciaux
                    msg_recu = msg_recu.decode()
                    print("Reçu {}".format(msg_recu))
                    if msg_recu == "HLO":
                        client.send(b"Ready to calculate:write ADD,MIN,TIM,DIV")
                    if msg_recu == "QHT":
                        serveur_lance = False
                    else: 
                        split=msg_recu.split(" ")
                        for i in range(len(split)):
                            #return a list should be only with 1 element
                            match=re.findall(r"[-+]?\d*\.\d+|\d+",split[i])
                            if len(match)>0:
                                split.pop(i)
                                match=float(match[0])
                                split.insert(i,match)    
                        #STEP 1 : CHECK COMMANDS ARE NOT WRONG ! AND STORE INDEX         
                        while len(split)>1:
                            for el in split:
                                print(split.index(el))
                                if el=="ADD":
                                    i=split.index(el)
                                    if len(split[:i])<2:
                                        split.clear()
                                        client.send(b"Missing float parameters, cannot calculate")
                                    elif type(split[i-2])!=float or type(split[i-2])!=float:
                                        client.send(b"Wrong type, should be float ! This is not a proper expression")
                                    else:
                                        result=split[i-2]+split[i-1]
                                        list_index=[i-2,i-1,i]
                                        for index in sorted(list_index, reverse=True):
                                            del split[index]
                                        split.insert(i-2,result)
                                        print(split)
                                        if len(split)==1:
                                            client.send(str(split[0]).encode())
                                        #to restart loop at the beginning
                                        break
                                        
                                elif el=="MIN":
                                    i=split.index(el)
                                    if len(split[:i])<2:
                                        split.clear()
                                        client.send(b"Missing float parameters, cannot calculate")
                                    elif type(split[i-2])!=float or type(split[i-2])!=float:
                                        client.send(b"Wrong type, should be float ! This is not a proper expression")
                                    else:
                                        result=split[i-2]-split[i-1]
                                        list_index=[i-2,i-1,i]
                                        for index in sorted(list_index, reverse=True):
                                            del split[index]
                                        split.insert(i-2,result)
                                        if len(split)==1:
                                            client.send(str(split[0]).encode())
                                        #to restart loop at the beginning
                                        break
                                                        
                                elif el=="TIM":
                                    i=split.index(el)
                                    if len(split[:i])<2:
                                        split.clear()
                                        client.send(b"Missing float parameters, cannot calculate")
                                    elif type(split[i-2])!=float or type(split[i-2])!=float:
                                        client.send(b"Wrong type, should be float ! This is not a proper expression")
                                    else:
                                        result=split[i-2]*split[i-1]
                                        list_index=[i-2,i-1,i]
                                        for index in sorted(list_index, reverse=True):
                                            del split[index]
                                        split.insert(i-2,result)
                                        if len(split)==1:
                                            client.send(str(split[0]).encode())
                                        #to restart loop at the beginning
                                        break
                                                        
                                elif el=="DIV":
                                    i=split.index(el)
                                    if len(split[:i])<2:
                                        split.clear()
                                        client.send(b"Missing float parameters, cannot calculate")
                                    elif type(split[i-2])!=float or type(split[i-2])!=float:
                                        client.send(b"Wrong type, should be float ! This is not a proper expression")
                                    else:
                                        result=split[i-2]/split[i-1]
                                        list_index=[i-2,i-1,i]
                                        for index in sorted(list_index, reverse=True):
                                            del split[index]
                                        split.insert(i-2,result)
                                        if len(split)==1:
                                            client.send(str(split[0]).encode())
                                        #to restart loop at the beginning
                                        break
                                    
                                elif type(el)==str and el not in self.liste_command:
                                    split.clear()
                                    client.send(b"{} is not a proper command !".format(el))                                    
                                    
        print("Fermeture des connexions")
        for client in clients_connectes:
            client.close()
        connexion_principale.close()

        
        
host = ''
port = 13000
newthread = Serveur_polonais(host,port)
newthread.start()

