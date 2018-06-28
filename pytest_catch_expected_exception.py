def moyenne(*nombres):
    taille = len(nombres)
    if taille == 0:
        return None
    somme = 0
    for nombre in nombres:
        if not isinstance(nombre, int):
            raise TypeError("'%s' n'est pas un entier" % str(nombre))
        somme += nombre
    return somme / taille


# cas simples
assert moyenne(5) == 5
assert moyenne(5, 8, 9) == 7
assert moyenne(5, 8, 9, 78, 43) == 28

# aucun parametre en entree
assert moyenne() == None

# message d'erreur de type plus explicite
try:
    moyenne(5, 'u', 8)
except TypeError, e:
    assert str(e) == "'u' n'est pas un entier"

