#Importation des modules
import itertools

#Définition des fonctions
def getPermutationsPythonList(list1):
    '''Cette fonction permet de trouver toutes les combinaisons possibles d'une liste
    '''
    list2 =range(len(list1))
    return list(itertools.combinations(list2,2))

def popList(consideredList, index1, index2):
    '''Cette fonction permet de supprimer d'une liste 2 éléments en fonction de leurs indexes
    '''
    if index1 < index2:
        temp_index = index1
        index1 = index2
        index2 = temp_index
    del consideredList[index1]
    del consideredList[index2]
    return consideredList

def runAddition(liste, solution, index):
    '''Cette fonction permet d'additionner deux termes d'une liste, d'ajouter
    le calcul dans une chaine de caractère et de modifier la liste initiale
    '''
    lst_addition = list(liste)
    elem1 = liste[index[0]]
    elem2 = liste[index[1]]
    addition = elem1 + elem2
    solution += str(elem1) +' + '+str(elem2)+' = '+str(addition)+'; '
    lst_addition.append(addition)
    popList(lst_addition, index[0], index[1])
    return lst_addition,solution, addition

def runSoustraction(liste, solution, index):
    '''Cette fonction permet de soustraire deux termes d'une liste, d'ajouter
    le calcul dans une chaine de caractère et de modifier la liste initiale
    '''
    lst_soustraction = list(liste)
    if liste[index[0]] > liste[index[1]]:
        elem1 = liste[index[0]]
        elem2 = liste[index[1]]
    else:
        elem2 = liste[index[0]]
        elem1 = liste[index[1]]        
    soustraction = elem1 - elem2
    solution += str(elem1) +' - '+str(elem2)+' = '+str(soustraction)+'; '
    lst_soustraction.append(soustraction)
    popList(lst_soustraction, index[0], index[1])
    return lst_soustraction,solution, soustraction

def runMultiplication(liste, solution, index):
    '''Cette fonction permet de multiplier deux termes d'une liste, d'ajouter
    le calcul dans une chaine de caractère et de modifier la liste initiale
    '''
    lst_multiplication = list(liste)
    elem1 = liste[index[0]]
    elem2 = liste[index[1]]
    multiplication = elem1 * elem2
    solution += str(elem1) +' * '+str(elem2)+' = '+str(multiplication)+'; '
    lst_multiplication.append(multiplication)
    popList(lst_multiplication, index[0], index[1])
    return lst_multiplication,solution, multiplication

def runDivision(liste, solution, index):
    '''Cette fonction permet de diviser deux termes d'une liste, d'ajouter
    le calcul dans une chaine de caractère et de modifier la liste initiale
    '''
    lst_division = list(liste)
    if liste[index[0]] > liste[index[1]]:
        elem1 = liste[index[0]]
        elem2 = liste[index[1]]
    else:
        elem2 = liste[index[0]]
        elem1 = liste[index[1]]
    if elem2 == 0 or elem1%elem2 != 0:
        division = -1
        return lst_division,solution, division
    else:
        division = elem1 // elem2
        solution += str(elem1) +' / '+str(elem2)+' = '+str(division)+'; '
        lst_division.append(division)
        popList(lst_division, index[0], index[1])
        return lst_division,solution, division

def leCompteEstBon(liste, objectif, solutions, start_calcul):
    '''Cette fonction permet d'effectuer tous les calculs possibles, et ainsi les réponses
    répondant à l'objectif.
    Pour cela, pour chaque combinaison (de deux termes) possibles (à partir d'une liste), on effectue
    les 4 opérations possibles (+, -, *, /), et on répète cette fonction autant de fois que necessaire.
    '''
    liste_calcul = list(liste)
    calcul = start_calcul
    for i in range(len(getPermutationsPythonList(liste))):
        #Addition
        lst_addition, calcul, addition = runAddition(liste_calcul, start_calcul, getPermutationsPythonList(liste)[i])
        if addition == objectif:
            solutions+= str(calcul)+'\n'
            lst_addition = []
        if len(getPermutationsPythonList(liste)) < 2:
            calcul = ''
        solutions = leCompteEstBon(lst_addition, objectif, solutions, calcul)
        #Soustraction
        lst_soustraction, calcul, soustraction = runSoustraction(liste_calcul, start_calcul, getPermutationsPythonList(liste)[i])
        if soustraction == objectif:
            solutions+= str(calcul)+'\n'
            lst_soustraction = []
        if len(getPermutationsPythonList(liste)) < 2:
            calcul = ''
        solutions = leCompteEstBon(lst_soustraction, objectif, solutions, calcul)
        #Multiplication
        lst_multiplication, calcul, multiplication = runMultiplication(liste_calcul, start_calcul, getPermutationsPythonList(liste)[i])
        if multiplication == objectif:
            solutions+= str(calcul)+'\n'
            lst_multiplication = []
        if len(getPermutationsPythonList(liste)) < 2:
            calcul = ''
        solutions = leCompteEstBon(lst_multiplication, objectif, solutions, calcul)
        #Division
        lst_division, calcul, division = runDivision(liste_calcul, start_calcul, getPermutationsPythonList(liste)[i])        
        if division == -1:
            lst_division = []
        elif division == objectif:
            solutions+= str(calcul)+'\n'
            lst_division = []
        if len(getPermutationsPythonList(liste)) < 2:
            calcul = ''
        solutions = leCompteEstBon(lst_division, objectif, solutions, calcul)
    return solutions

#Programme principale  
testList = [8, 2, 50, 1, 10, 5]

solutions = leCompteEstBon(testList, 902, "", "")
if solutions == "":
    print("Il n'y a pas de solution")
else:
    print("Il y a : "+str(solutions.count('\n'))+" solution(s) possible ! \n") 
    print(solutions)   


''' Pour une liste de 6 nombres, il y a 3 516 060 possibilités car :
Pour le 1e niveau (liste de 6 nombres), il y a 15 combinaisons et 4 opérations soit : 60 possibilités.
Pour le 2e niveau (liste de 5 nombres (6-4+1)), il y a 10 combinaisons et 4 opérations, 
multiplié par les possibilités précédentes soit : 2400 possibilités.
Pour le 3e niveau (liste de 4 nombres), il y a 6 combinaisons et 4 opérations, 
multiplié par les possibilités précédentes soit : 57600 possibilités.
Pour le 4e niveau (liste de 3 nombres), il y a 3 combinaisons et 4 opérations, 
multiplié par les possibilités précédentes soit : 691200 possibilités.
Pour le 5e niveau (liste de 2 nombres), il y a 1 combinaisons et 4 opérations, 
multiplié par les possibilités précédentes soit : 2764800 possibilités.
Or le nombres de solutions recherchées par la fonction leCompteEstBon est la somme de toutes ces possibilités.

En réalité le nombre de calcul est inférieur car si une division donne un chiffre decimal, on ne calcul pas les
"couches" inférieurs.
'''
