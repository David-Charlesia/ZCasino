# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 12:48:59 2019

@author: David-Charlesia
"""

from random import randint

def choix_nombre():
    nombre=int(input("\nChoississez votre nombre (entre 0 et 49) : "))
    return nombre

def mise_joueur():
    mise=int(input("\nEntrez le montant de votre mise : "))
    return mise

def nombre_jeu():
    return randint(0,49)

def gagner(nombre,choix_nb):
    if nombre==choix_nb:
        return True
    
def gagner2(nombre,choix_nb):
    if nombre%2==0:
        if choix_nb%2==0:
            return True
        else:
            return False
    else:
        if choix_nb%2!=0:
            return True
        else:
            return False

def jouer():
    argent=int(input("\nVous avez combien d'argent ? "))
    
    while argent>0:
        nombre=nombre_jeu()
        #print("CHEAT : nb=",nombre)
        choix_nb=choix_nombre()
        mise=mise_joueur()
        
        argent-=mise
    
        if gagner(nombre,choix_nb):
            print(nombre,"=",choix_nb)
            print("\nBravo, vous avez gagner ! Vous récupérez 3 fois votre mise, c'est à dire ",round(mise*3,2),"$")
            argent+=round(mise*3,2)
            print("\nVous avez maintenant ",argent,"$")
        elif gagner2(nombre,choix_nb):
            print("\n",nombre,"!=",choix_nb)
            print("\nVotre nombre est de la même couleur que le nombre tiré, vous perdez seulement la moitié de votre mise")
            argent+=round(mise/2,2)
            print("\nVous avez maintenant ",argent,"$")
        else:
            print("\n",nombre,"!=",choix_nb)
            print("\nDommage, vous avez perdu !")
            print("\nVous avez maintenant ",argent,"$")