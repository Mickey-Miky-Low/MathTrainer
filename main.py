import operations_basiques
import conversions_bases

isLearning = True

while isLearning:
    print('='*50)
    print(' ')
    print("\033[35mMathTrainer 1.0 Main Menu\033[37:0m")
    print(' ')
    print('='*50)
    print(' ')
    print("1...................Additions")
    print("2...................Soustractions")
    print("3...................Multiplications")
    print("4...................Divisions")
    print("5...................Exercices Conversions base 2, 10, 16")
    print("6...................Conversions base 2, 10, 16")
    print("7...................Quitter")
    print(' ')
    print('='*50)
    choix = int(input(""))

    if choix==1:
        operations_basiques.SubMenuOp("addition")    #Appel du Sous Menu des Additions
    
    elif choix==2:
        operations_basiques.SubMenuOp("soustraction")    #Appel du Sous Menu des Soustractions

    elif choix==3:
        operations_basiques.SubMenuOp("multiplication")    #Appel du Sous Menu des Multiplications

    elif choix==4:
        operations_basiques.SubMenuOp("division")    #Appel du Sous Menu des Divisions

    elif choix==5:
        conversions_bases.SubMenuExercicesConv()     #Appel du Sous Menu des Exercices de Conversions

    elif choix==6:
        conversions_bases.SubMenuConv()     #Appel du Sous Menu des Conversions
    
    else:
        print("Bonne journée !")
        isLearning=False
    
