import json

def liste_binaire(c):
  Liste = []
  for n in c:
    test = bin(n)
    test=test.replace("0b", "")
    liste_reponse=[]
    longueur=16-len(test)
    for i in range(longueur):
      liste_reponse+=[0]
    for i in str(test):
     liste_reponse=liste_reponse+[i]
    Liste += liste_reponse    
  return(Liste)
  

#NB : Trouver autre nom pour tester et variable  
#Ici : convertir Binaire en Decimal





def convertisseur_binaire_decimal(p):
  L = []
  i = -1
  l = len(p)
  N = int(l/16)
  for t in range(N):
    i = i + 1
    coupe = p[0+i*16:16+i*16]
    coupe = "".join(str(x) for x in coupe)
    v =  "0b" + coupe
    v = int(v, 0)
    L.append(v)
  return(L)
  



#test = int(test.replace("0b", ""), 2)
#print(test)
  
listeTest = [35,122,460]

fichier = open("rien.txt","r")
liste1 = fichier.read()
liste1 = liste1.replace(",", ".")
liste1 = liste1.replace("	 ",",")
liste1 = liste1.replace(" ",",")
liste1 = liste1.replace("?","")
liste1 = liste1.replace("Brute_E","")
liste1 = liste1.replace("nm","")
liste1 = liste1.replace("s.u","")
liste1= liste1.replace("	","")
liste1= liste1.replace('\n', '')
liste1= liste1[1:]
datboi = liste1.split(',')
datboi = datboi[:-2]


liste3 = []
def liste_int(t):
  for x in t:
    #print(x)
    if "x" not in x:    
      liste3.append(round(float(x)))
    else: 
     pass
  print(liste3)  
  return(liste3)  


ints = liste_int(datboi)


final = liste_binaire(ints)
resultat = convertisseur_binaire_decimal(final)




dico =  {}
compte = -1
for x in resultat:
  compte = compte + 1
  if compte%2 == 0:
    dico[int(x)] = int(resultat[compte+1])
  else:
    pass


def separateur_abs(r):
  i = 0
  absc = []
  for x in r:
    if i % 2 == 0:
      absc.append(r[i])
    else:
      pass
    i = i + 1
  return(absc) 

def separateur_ord(r):
  i = 0
  ordo = []
  for x in r:
    if i % 2 != 0:
      ordo.append(r[i])
    else:
      pass
    i = i + 1
  return(ordo)

#print(separateur_abs(resultat))
print(separateur_ord(resultat))


#print(dico)
"""
with open('datap.json', 'w') as fp:
    json.dump(dico, fp)
"""
