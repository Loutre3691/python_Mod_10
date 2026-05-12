from typing import Callable


class Spells:
    
    def fireball(self, target):
        return f"🔥 Fireball hits {target},"
    
    def heals(self, target):
        return f"🏥 Heals hits {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    print("\n\033[1;34mTesting spell combiner...\033[0m]")
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both spells must be functions!!")

    def combined(*args) -> str:
        res1 = spell1(*args)
        res2 = spell2(*args)
        return f"{res1} {res2}"

    return combined

# spell_combiner check that spell1 and spell2 it's a function with callable
# return tupple

if __name__ == "__main__":
    s = Spells()

    combined = spell_combiner(s.fireball, s.heals)
    print(f"Combined spell result: {combined('Dragon')}")

# def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
#     print("\n\033[1;34mTesting power amplifer...\033[0m]")
#     amplifer = callable()
#     return amplifer
# Vérifier que base_spell est une fonction


# def conditional_caster(condition: Callable, spell: Callable) -> Callable:
#     print("\n\033[1;34mTesting conditional caster...\033[0m]")
#     caster = callable()
#     return caster
# Vérifier que condition et spell sont des fonctions

# def spell_sequence(spells: list[Callable]) -> Callable:
#     print("\n\033[1;34mTesting spell sequence...\033[0m]")
#     sequence = callable()
#     return sequence
# Vérifier que chaque élément de la liste est une fonction
