from typing import Callable


class Spells:
    
    def fireball(self, target, power=5):
        return f"🔥 Fireball hits {target}"
    
    def heals(self, target, power=10):
        return f"🏥 Heals hits {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both spells must be functions!!")

    def combined(target, power=5) -> str:  # ← les vrais arguments
        res1 = spell1(target, power)        # ← on APPELLE spell1
        res2 = spell2(target, power)        # ← on APPELLE spell2
        return f"{res1} , {res2}"

    return combined
# spell_combiner check that spell1 and spell2 it's a function with callable
# return tupple


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    print("\n\033[1;34mTesting power amplifer...\033[0m")
    if not callable(base_spell):
        raise TypeError("Base spell must be function")
    
    def amplifer(value) -> int:
        before_amplif = value
        after_amplif = before_amplif * multiplier
        return before_amplif, after_amplif
    

    return amplifer

# Vérifier que base_spell est une fonction


if __name__ == "__main__":
        
    spells = Spells()
    combo = spell_combiner(spells.fireball, spells.heals)
    print(combo("Dragon"))


    power = power_amplifier(spells.fireball, 3)
    print(spells.fireball('dragon'))
    print(power(10))
    heal = power_amplifier(spells.heals, 3)
    print(heal(5))




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
