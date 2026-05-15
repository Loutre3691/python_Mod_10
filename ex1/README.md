# ceci est un tire
```bash
cd /home
```
## cecci est soustritre
```python
from typing import Callable


class Spells:
    def fireball(self, target, power=5):
        return f"🔥 Fireball hits {target}, the power is {power}."
    
    def heals(self, target, power=10):
        return f"🍃 Heals hits {target}, the power is {power}."


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    print("\n\033[1;34mTesting power combiner...\033[0m")
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both spells must be functions!!")

    def combined(target: str) -> tuple: 
        return(spell1(target), spell2(target))      

    return combined
# spell_combiner check that spell1 and spell2 it's a function with callable
# return tupple


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    print("\n\033[1;34mTesting power amplifer...\033[0m")
    if not callable(base_spell):
        raise TypeError("Base spell must be function")
    
    def amplified(target: str, power: int) -> Callable:
        return base_spell(target, power * multiplier)

    return amplified

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    print("\n\033[1;34mTesting conditional caster...\033[0m]")
    if not callable(condition):
        raise TypeError("Base spell must be function")
    
    def caster()

    return caster

# conditional_caster(condition, spell) Lance un sort avec condition: 
# - Renvoie un nouveau sort qui ne se lance que si une condition est vraie. 
# - Si la condition échoue, renvoie « Sort échoué ».
# - La condition et le sort reçoivent les mêmes arguments.


if __name__ == "__main__":
        
    spells = Spells()
    combo = spell_combiner(spells.fireball, spells.heals)
    spell1, spell2 = combo("Dragon")
    print(spell1, spell2)
    
    fireball = power_amplifier(spells.fireball, 3)
    print(f"Original: {spells.fireball('Dragon', 5)}")
    print(f"Amplified: {fireball('Dragon', 5)}")
    
    heal = power_amplifier(spells.heals, 3)
    print(f"Original: {spells.heals('Dragon', 10)}")
    print(f"Amplified: {heal('Dragon', 10)}")
    






# def spell_sequence(spells: list[Callable]) -> Callable:
#     print("\n\033[1;34mTesting spell sequence...\033[0m]")
#     sequence = callable()
#     return sequence
# Vérifier que chaque élément de la liste est une fonction
```

>[!TIPS]
 jkljklhflkdjgflkhgljhdjflghjkldfh



### ceci est chapitre
jgjhgjhgjhgjg `kjhjkhjkhkj` ;kjlkjlkj

>ghfghfhgfh
jhghkhk

