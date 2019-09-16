''' L'objectif de ce programme est de transferer un ensemble d'une pile de x jusqu'à la dernier pile en utilisant n silos différents et en respectant les règles de la tour de hanoi''' 

def accidentnucleaire(x,n):
    if (n<3):
        return("impossible avec 2 silos ou moins")
    #On initialise la liste des silos 
    silos=[]
    for i in range (n):
        silos.append([])
    #On vide le premier silo fictif dans deux silos en séparant éléments pairs et impairs
    for i in range (x): 
        if (i%2==0):
            silos[0].append(x-i)
        else:
            silos[1].append(x-i)

    #On définit la fonction hanoi de manière récursive qui sera utile dans la suite du programme
    def hanoi(l,a,b,c):
        if l>0:
            hanoi(l-1,a,c,b)
            silos[c].append(silos[a][-1])
            del silos[a][-1]
            print(silos)
            hanoi(l-1,b,a,c)

    #On distingue deux cas, si le nombre de conteneurs est pairs ou impairs 
    if (x%2==0):

        for i in range (1,x//2):
            hanoi(1,0,1,2)
            print(silos)
            hanoi(2*i-1,1,0,2)
            print(silos)
            hanoi(2*i,2,0,1)
            print(silos)
            print("fin de l'étape" + str(i))
            
        hanoi(1,0,1,2)
        print(silos)
        hanoi(x-1,1,0,2)
        print(silos)
    
    if (x%2==1):
        for i in range (1,x//2+1):
            hanoi(1,1,0,2)
            print(silos)
            hanoi(2*i-1,0,1,2)
            print(silos)
            hanoi(2*i,2,1,0)
            print(silos)
            print("fin de l'étape" + str(i))
        
        hanoi(x,0,1,2)
        print(silos)
    #Les conteneurs sont rangés dans le bon ordre dans le silo numéro 3
    #Finalement comme voulu, on transfère tous les conteneurs dans le dernier silo
    if (n>3):
        hanoi(x,2,0,n-1)
        print(silos)

#On appelle la fonction avec les arguments pour éssayer        
accidentnucleaire(17,4) 

