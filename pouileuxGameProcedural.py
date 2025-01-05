# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''

     #initialisation de deux listes vides
     donneur=[]
     autre=[]

     for i in range (0,len(p)-1,2):  #parcours de la liste sur sa longueur à pas de 2
         donneur.append(p[i+1])    #distribution des éléments de la liste en alternant entre donneur et autre en commençant par autre
         autre.append(p[i])
     
     return (donneur, autre)    #retour de la fonction


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]
    l.sort()  #ordonnement de la liste

    i = 0   #initialisation d'un compteur
    while i < len(l)-1:
        #si la longueur de l'élément de la liste est paire, c-à-d que la carte est de deux caractères sa lettre ou son chiffre et sa fleur
        if len(l[i]) == 2 :
            if l[i][0] == l[i+1][0]:    #si l'élément et celui qui le suit sont égaux
                i+=1   #incrémentation du compteur
            else :
                resultat.append(l[i])   #sinon ajout de l'élément à la liste resultat

        else :   #si l'élément de la liste a trois caratères (longueur 3), soit la carte 10 qui, en plus de deux caratères du nombres, compte un troisième caractère pour la fleur
            if l[i][0:2:1] == l[i+1][0:2:1] == '10':    #si l'élément et celui qui le suit sont égaux 
                i+=1   #incrémentation du compteur

            else :
                resultat.append(l[i])  #sinon ajout de l'élément à la liste resultat
        i+=1  #incrémentation du compteur 
        
    if i == len(l)-1 :  #si l[i] correspond au dernier élément de la liste
        resultat.append(l[i])  #ajout de l'élément dans la liste resultat
 

    random.shuffle(resultat)  #mélange des éléments de la liste
    return resultat   #retour de la liste


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''
    
    for i in p :    #parcours de la liste
        print(i,end=' ')  #affichage de chaque élément séparé par des espaces
    
def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     position = int(input("SVP, entrez un entier entre 1 et " + str(n) + " inclus : "))  #l'utilisateur entre la carte choisie

     #Tant que l'entrée utilisateur n'est pas dans l'intervalle souhaité, soit n >= position >= 1, on lui demande de renter une nouvelle entrée
     while not(n >= position >= 1):
         position = int(input("SVP, entrez un entier entre 1 et " + str(n) + " inclus : "))

     #retour de la fonction
     return position

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)   #la main de Humain avant le défaussage des paires
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()  #robot attend le tour de Humain
     
     donneur=elimine_paires(donneur)  #Robot élimine ses paires
     humain=elimine_paires(humain)      #Humain élimine ses paires

     tour = 0
     while len(donneur) > 0 and len(humain) > 0:
         if tour % 2 == 0:      #tour de Humain
             print("Votre main est : ")
             affiche_cartes(humain)  #affichage des cartes de humain après elimination de ses paires
             print(end='\n')
             print("J'ai " + str(len(donneur)) + " cartes.","Si 1 est la position de ma première carte et " + str(len(donneur)) + " la position de ma dernière carte,laquelle de mes cartes voulez-vous ?")    #Robot demande à Humain la carte qu'il veut
             card= entrez_position_valide(len(donneur))   #Humain choisit une carte 
             print("Vous m'avez demandé ma " + str(card) + "ième carte")
             print("Là voilà. C'est un " + donneur[card-1])   #affichage de la carte choisie par Humain
             print("Avec " + donneur[card-1] + " ajouté, votre main est : ")
             humain.append(donneur[card-1])   #la carte choisie par Humain est ajoutée aux siennes
             donneur.remove(donneur[card-1])  #et est enlevée aux cartes de Robot
             affiche_cartes(humain)   #la nouvelle main de Humain avant défaussage des paires
             humain = elimine_paires(humain)   #éliminationi des paires
             print(end='\n')
             print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est : ")
             affiche_cartes(humain)  #la nouvelle main de Humain après défaussage des paires
             print(end='\n')
             attend_le_joueur()   #humain attend le tour de robot
             print("*****************************************************************************************")
             
         else :     #tour de Robot
             print("Mon tour.")
             card2 = random.randint(0, len(humain) - 1)  #Robot choisit une carte parmi celles de Humain
             donneur.append(humain[card2])    #et ajoute cette carte aux siennes
             humain.remove(humain[card2])       #la carte choisie par Robot est retirée de chez humain
             print("J'ai pris votre " + str(card2 + 1) + "ème carte")   #affichage de la carte prise par Robot
             donneur = elimine_paires(donneur)      #Robot élimine ses paires
             attend_le_joueur()   #Robot attend le tour de Humain
             print("*****************************************************************************************")

         tour +=1

     #détermination du vainqueur
     if len(humain) == 0 :
         print("Vous avez terminé toutes les cartes")
         print("FELICITATIONS ! VOUS, HUMAIN, AVEZ GAGNE.")
             
     else :
         print("J'ai terminé toutes les cartes.")
         print("VOUS AVEZ PERDU ! MOI, ROBOT, J'AI GAGNE.")
 

# programme principale
joue()

