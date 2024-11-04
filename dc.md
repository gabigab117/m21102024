# Les dataclasses en Python

## 1. Introduction

Les dataclasses, introduites dans Python 3.7, sont un moyen simplifié de créer des classes destinées principalement à
stocker des données. Elles réduisent la quantité de code boilerplate nécessaire pour créer des classes simples.

## 2. Importation et utilisation de base

Pour utiliser les dataclasses, vous devez d'abord les importer :

```python
from dataclasses import dataclass


@dataclass
class Point:
    # Attributs d'instance
    x: int
    y: int
```

- Génération automatique de méthodes comme __init__, __repr__, et __eq__
```python
@dataclass
class Person:
    name: str
    age: int

# Équivalent à :
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p)  # Affiche : Person(name='Alice', age=30)

# eq pour comparer les objets de la meme classe
# Avec une classe standard, on compare l'emplacement mémoire
# avec une dataclasses on compare les champs
p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(p1 == p2)  # True
print(p1 == p3)  # False
```
- Syntaxe concise

## Champs par défaut

```python
@dataclass
class Rectangle:
    width: int
    height: int = 10
```

## Champs calculé

```python
from dataclasses import dataclass, field

@dataclass
class Circle:
    radius: float
    area: float = field(init=False) # area ne sera pas un paramètre dans le constructeur init

    def __post_init__(self):
        self.area = 3.14 * self.radius ** 2
```

## Ordre

```python
@dataclass(order=True)
class Person:
    name: str
    age: int
```

```python
from dataclasses import dataclass


@dataclass(order=True)
class Person:
    name: str # En premier
    age: int # en deuxieme si les premiers sont égaux

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(p1 == p2)  # Fonctionne
print(p1 < p2)   # Fonctionne maintenant!
print(p1 > p2)   # Fonctionne aussi!

# On peut maintenant trier
people = [Person("Charlie", 35), Person("Alice", 30), Person("Bob", 25)]
sorted_people = sorted(people)  # Possible seulement avec order=True
```


## Immutablité

```python
@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int
```

## Attribut de classe

```python
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class MyClass:
    instance_attr: int
    class_attr: ClassVar[int] = 0
```