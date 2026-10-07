import random 
import time


def mdp_generator():
    minuscule = "abcdefghijklmnopqrstuvwxyz"
    majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nombre = "0123456789"
    symbole = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    total = minuscule + majuscule + nombre + symbole
    longeur = 10
    mdp = "".join(random.sample(total, longeur))

    print("Mot de passe généré :", mdp)
    time.sleep(50)