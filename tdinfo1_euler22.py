f=open('p022_names.txt','r')
txt=f.read()
f.close()

noms=txt.split(",")#on transforme le texte en liste avec pour critère de séparation la virgule
noms.sort()
print(noms)

def valeur_lettre(lettre):
    return ord(lettre)-ord("A")+1  #les valeurs des lettres se suivent sur python

# attetion ce texte rajoute des guillemets à chaque mot

def comptage(x):
    L=[]
    for i in range(len(x)):
        m=0
        for lettre in x[i]:
            m+=valeur_lettre(lettre)
        m+=60 #valeur des guillemets à enlever
        L.append(m*(i+1))
    return (sum(L))

print(comptage(['"AAA"']))#on obtient -57 au lieu de 3 donc il faut rajouter 60 a chaque fois
print(comptage(noms))



    