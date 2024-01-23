import asyncio
import time


# Définition de la fonction nom qui en retour affiche le prénom donné en argument après 10 secondes d'attente

def nom(prenom):
    name = prenom
    time.sleep(2)
    print(name)

# Définition de la fonction main qui affiche le temps de complétion de l'exécution
# de la fonction nom pour trois arguments différents

def main():
    print("Subroutine :")
    start_time = time.time()
    nom('Daniel')
    nom('Donna')
    nom('Diane')
    end_time = time.time()
    print("Durée totale d'exécution: %.2f secondes" % (end_time - start_time))


main()


# Définition de la coroutine nom qui en retour affiche le prénom donné en argument après 10 secondes d'attente

async def nom_async(prenom):
    name = prenom
    await asyncio.sleep(2)
    print(name)

# Définition de la coroutine main qui affiche le temps de complétion de l'exécution
# de la fonction nom pour trois arguments différents

async def main():
    print("\nCoroutine :")
    start_time = time.time()
    await asyncio.gather(nom_async('Daniel'), nom_async('Donna'), nom_async('Diane'))
    end_time = time.time()
    print("Durée totale d'exécution: %.2f secondes" % (end_time - start_time))

asyncio.run(main())
