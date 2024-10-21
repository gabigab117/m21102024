Cas de base : C'est la condition qui arrête la récursion.
Cas récursif avec argument modifié : C'est la partie où la fonction s'appelle elle-même.

```python
def factorielle(n):
    # Cas de base
    if n == 0 or n == 1:
        return 1
    # Cas récursif
    else:
        return n * factorielle(n - 1)

# Exemple d'utilisation
print(factorielle(5))  # Affiche 120
```

Une descente puis une remontée. Quand le cas de base est atteint dans le dernier appel, remonte la pile d'appels.
les appels récursifs les plus profonds sont les premiers à retourner un résultat

Toujours penser au cas de base, pour éviter un stack overflow.
Recursion Error, limite par Python