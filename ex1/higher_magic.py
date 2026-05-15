from typing import Callable, Optional

def fireball(target: str, power: int = 5) -> str:
    return f"{target} hits Fireball 🔥, the power is {power}."


def heals(target: str, power: int = 10) -> str:
    return f"{target} hits Heals 🍃, the power is {power}."


def is_dragon(target: str, power: int) -> bool:
    return target == "Dragon"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    print("\n\033[1;34mTesting power combiner...\033[0m")
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both spells must be functions!!")

    def combined(target: str, power: Optional[int] = None) -> tuple: 
        if power is None:
            return (spell1(target), spell2(target))
        return (spell1(target, power), spell2(target, power))
    
    return combined
# spell_combiner check that spell1 and spell2 it's a function with callable
# return tupple


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    print(f"\n\033[1;34mTesting power {base_spell.__name__}...\033[0m")
    if not callable(base_spell):
        raise TypeError("Base spell must be function")
    
    def amplified(target: str, power: int) -> Callable:
        return base_spell(target, power * multiplier)

    return amplified
# Returns a new spell function that amplifies the original power.
# The multiplier is applied to the power argument before the base spell is cast.


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    print("\n\033[1;34mTesting conditional caster...\033[0m")
    if not callable(spell):
        raise TypeError("Base spell must be function")
    
    def condition_caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled ❌❌❌"

    return condition_caster
# Returns a new spell function that only executes if a specific condition is met.
# If the condition (called with the same arguments) returns True, the spell is cast;
# otherwise, it returns a 'fizzled' message.


def spell_sequence(spells: list[Callable]) -> Callable:
    print("\n\033[1;34mTesting spell sequence...\033[0m]")
    if not callable(spells):
        raise TypeError("Base spell must be function")
    
    def sequence(target: str, power: int):
        spell_list = []
        spell_list.append(target)

        return spell_list
            
    return sequence
# retourne une fonction qui lance tous les sorts dans l ordre
#chaque sort recoiemt le meem argument
#retourn une list de tous les result sort

if __name__ == "__main__":

    combo = spell_combiner(fireball, heals)
    spell1, spell2 = combo("Dragon")
    print(spell1, spell2)
    
    fireball_amplifer = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 5)}")
    print(f"Amplified: {fireball_amplifer('Dragon', 5)}")
    
    heal_amplifer = power_amplifier(heals, 3)
    print(f"Original: {heals('Dragon', 10)}")
    print(f"Amplified: {heal_amplifer('Dragon', 10)}")

    fireball_conditional = conditional_caster(is_dragon, fireball)
    print(f"{fireball_conditional('Dragon', 5)}")
    print(f"{fireball_conditional('Witcher', 60)}")

    spell_list = [
        fireball,
        heals
    ]
    new_spell_list = spell_sequence()
    for spell in new_spell_list:
        print(spell)





    






