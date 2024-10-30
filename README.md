# PyBowling

## Utilisation Docker

```shell
docker build -t mon-bowling .
docker run -it mon-bowling
```

## Utilisation via Shell

```shell
python main.py
```

## Tests

Listes des différents tests effectués : 
- Test du score maximum : Tous les lancés sont des Strike, le résulat final est 300
- Test du score minimal : Que des 0, pas de lancé bonus, le résultat est 0
- Test des bonus - Spare au dernier tour: Terminer par un spare, un lancé supplémentaire
    exemple : dernierTour = lancé1 : 8 lancé2 : 2, tourBonus = lancé1 : 5  -> le score du dernier tour est 15
    exemple2 : dernierTour = lancé1 : 10, tourBonus = lancé1 : 10, , -> le score du dernier tour est 20
- Test des bonus - Strike au dernier tour: Terminer par un strike, deux lancés supplémentaires
    exemple : dernierTour = lancé1 : 10, tourBonus = lancé1 : 5 lancé 2 : 2 -> le score du dernier tour est 17
    exemple2 : dernierTour = lancé1 : 10, tourBonus1 = lancé1 : 10, , tourBonus2 = lancé1 : 3 -> le score du dernier tour est 23
- Test du calcul de score pour un strike : on prend les deux prochains lancés
    exemple : tour1 = lancé1 : 10, tour2 = lancé1 : 5 lancé 2 : 2 -> le score du tour 1 est 17
    exemple2 : tour1 = lancé1 : 10, tour2 = lancé1 : 10, , tour3 = lancé1 : 3 lancé2 : 4 -> le score du tour 1 est 23
- Test du calcul de score pour un spare : on prend le prochain lancé
    exemple : tour1 = lancé1 : 6 lancé : 4, tour2 = lancé1 : 5 lancé 2 : 2 -> le score du tour 1 est 15