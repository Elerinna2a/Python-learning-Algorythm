alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"
,"s","t","u","v","w","x","y","z"]
clef = 6

def trouverIndiceLettre(lettre):
    cpt=0
    for i in alphabet:
        if i==lettre:
            return cpt
        cpt+=1
    print("error, this letter is not in the alphabet")

print(trouverIndiceLettre("e"))

def chiffrementCesar(phrase,clef):
    phraseChiffre = []
    for i in phrase:
        indiceActuel = trouverIndiceLettre(i)
        indiceNouveau_temp = indiceActuel+clef
        indiceNouveau = indiceNouveau_temp % len(alphabet)
        lettreNouveau = alphabet[indiceNouveau]
        phraseChiffre.append(lettreNouveau)
    return phraseChiffre

def dechiffrementCesor(phraseChiffre, clef):
    phraseClaire = []
    for i in phraseChiffre:
        indiceActuel = trouverIndiceLettre(i)
        indiceNouveau_temp = indiceActuel-clef
        indiceNouveau = indiceNouveau_temp % len(alphabet)
        lettreNouveau = alphabet[indiceNouveau]
        phraseClaire.append(lettreNouveau)
    return phraseClaire
phrasechiffre = chiffrementCesar("le chiffrement de cesar",6)

print(phrasechiffre)
print(dechiffrementCesor(phrasechiffre,6))
    
