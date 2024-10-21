def flat_list(liste):
    flat = []
    for e in liste:
        # récursif
        if isinstance(e, list):
            flat.extend(flat_list(e))
        else:
            # base
            flat.append(e)
    return flat

# Exemple d'utilisation
liste = [1, [2, [3, 4]]]
print(flat_list(liste))



# Premier appel : flat_list([1, [2, [3, 4]]])
# 1 est ajouté directement à flat
# Pour [2, [3, 4]], on fait un appel récursif

# Deuxième appel (récursif) : flat_list([2, [3, 4]])
# 2 est ajouté directement
# Pour [3, 4], nouvel appel récursif

# Troisième appel (récursif) : flat_list([3, 4])
# 3 et 4 sont ajoutés directement

# Remontons la pile d'appels :
# Troisième appel retourne [3, 4]
# Deuxième appel ajoute 2 et étend avec [3, 4], retourne [2, 3, 4]
# Premier appel ajoute 1 et étend avec [2, 3, 4]

# Résultat final : [1, 2, 3, 4]


def sum_dict(element):
    resultat = 0
    for v in element.values():
        if isinstance(v, int):
            resultat += v
        else:
            resultat += sum_dict(v)
    return resultat

print(sum_dict({"a": 1, "b": {"a": 2}}))

# Chaque appel à sum_dict crée un nouveau cadre d'exécution (frame) avec sa propre variable resultat.
# resultat = 0 initialise une nouvelle variable locale pour chaque appel de la fonction.
# Les résultats sont "remontés" et accumulés niveau par niveau.
# L'initialisation resultat = 0 assure que chaque sous-calcul commence de zéro.