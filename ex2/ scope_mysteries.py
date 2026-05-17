from typing import Callable

# Creates a couner that increases by 1 each time it is called.
def mage_counter() -> Callable:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


# adds the new power to the old power and adds them together.
def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def increment_power(added_power: int) -> int:
        nonlocal power
        power += added_power
        return power

    return increment_power

# Returns a function that applies a specific enchantment prefix to any item.
def enchantment_factory(enchantment_type: str) -> Callable:
    print("\n\033[1;34mTesting enchantment factory...\033[0m")

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant

# Returns a dictionary of two functions to store and recall key-value pairs 
# in an isolated memory dictionary.
def memory_vault() -> dict[str, Callable]:
    memory = {}
    
    def store(key: str, value: str) -> None:
        memory.update({key: value})

    def recall(key) -> str:
        if key in memory:
            return memory[key]
        return "Memory not found"
    
    return {"store": store, "recall": recall} 


if __name__ == "__main__":
    print("\n\033[1;34mTesting mage counter...\033[0m")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1 : {counter_a()}")
    print(f"counter_a call 2 : {counter_a()}")
    print(f"counter_a call 3 : {counter_a()}")
    print(f"counter_b call 1 : {counter_b()}")

    print("\n\033[1;34mTesting spell accumulator...\033[0m")
    
    power_1 = 100
    power_2 = 20
    power_3 = 30
    total_power = spell_accumulator(power_1)
    print(f"Start base: {power_1}")
    print(f"Base {power_1} add {power_2}: {total_power(power_2)}")
    print(f"Base {power_1} add {power_3}: {total_power(power_3)}")


    print("\n\033[1;34mTesting enchantment factory...\033[0m")
    flaming_enchant = enchantment_factory("Flaming")
    frozen_enchant = enchantment_factory("Frozen")
    print(flaming_enchant("Sword"))
    print(frozen_enchant("Shield"))

    print("\n\033[1;34mTesting memory vaulr...\033[0m")
    vault = memory_vault()
    vault["store"]("secret", "42")
    vault["store"]("hero", "WonderWOman")

    print(f"store 'secret' = {vault['recall']('secret')}")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"store 'hero' = {vault['recall']('hero')}")
    print(f"Recall 'hero': {vault['recall']('hero')}")
    print(f"Recall 'unknown': {vault['recall']('inconnu')}")


# =============================================================================
# SCOPE MYSTERIES — LEXICAL SCOPING ET CLOSURES
# =============================================================================
#
# Le concept central de cet exercice : la CLOSURE
# Une closure c'est quand une fonction interne se souvient des variables
# de sa fonction parente, même après que le parent a fini de s'executer.
# La variable reste "gelée" en mémoire, comme dans un sac à dos.
#
# -----------------------------------------------------------------------------
# mage_counter()
# -----------------------------------------------------------------------------
# Crée un compteur indépendant grâce à une closure.
# count = 0 est gelé dans la fonction interne increment().
# nonlocal permet de modifier le count du parent (sans ça Python croirait
# qu'on veut créer un nouveau count local).
# Chaque appel à mage_counter() crée un nouveau compteur indépendant
# avec son propre count = 0 en mémoire — counter_a et counter_b
# ne se mélangent jamais.
#
# -----------------------------------------------------------------------------
# spell_accumulator(initial_power)
# -----------------------------------------------------------------------------
# Crée un accumulateur qui part d'une valeur de base et additionne
# chaque nouvelle valeur au total précédent.
# power = initial_power est gelé dans la closure.
# nonlocal permet de modifier ce power à chaque appel.
# Un seul accumulateur est créé, et on l'appelle plusieurs fois —
# il se souvient de son état entre chaque appel grâce à la closure.
#
# -----------------------------------------------------------------------------
# enchantment_factory(enchantment_type)
# -----------------------------------------------------------------------------
# Une "usine" qui fabrique des fonctions d'enchantement différentes.
# enchantment_type ("Flaming", "Frozen"...) est gelé dans la closure.
# La fonction interne enchant() reçoit item_name à l'appel
# et colle les deux : f"{enchantment_type} {item_name}" → "Flaming Sword".
# Une seule fonction, mais elle peut créer autant de types
# d'enchantements différents qu'on veut.
#
# -----------------------------------------------------------------------------
# memory_vault()
# -----------------------------------------------------------------------------
# Un coffre-fort privé partagé par deux fonctions via closure.
# memory = {} est le coffre, gelé et privé — inaccessible de l'extérieur.
# store(key, value) range une valeur dans le coffre avec une étiquette.
# recall(key) retrouve la valeur par son étiquette, ou retourne
# "Memory not found" si la clé n'existe pas.
# Les deux fonctions sont retournées dans un dict {"store": ..., "recall": ...}
# C'est une mini base de données privée — la closure garantit
# que personne ne peut toucher à memory directement.
#
# =============================================================================
# RÉSUMÉ GLOBAL
# =============================================================================
# Tous ces exercices partagent le même schéma :
#   1. La fonction parente crée une variable privée
#   2. La fonction interne y accède via la closure
#   3. La fonction parente retourne la fonction interne (son adresse)
#   4. La variable privée reste en mémoire entre les appels
#
# C'est ça le lexical scoping : une fonction se souvient de
# l'environnement dans lequel elle a été créée.
# =============================================================================