#Le programme fonctionne SEULEMENT s'il y a un fichier a convertir; ici nommé 'rien.txt'

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
step = liste1.split(',')
step = step[:-2]


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


ints = liste_int(step)


final = liste_binaire(ints)
resultat = convertisseur_binaire_decimal(final)
