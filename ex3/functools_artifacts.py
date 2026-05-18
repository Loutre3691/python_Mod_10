
from functools import reduce, partial
import operator
from typing import Callable

def fireball(power: int, element: str, target: str) -> str:
    return f"Power: {power}, element: {element}, target: {target}"

def iceball(power: int, element: str, target: str) -> str:
    return f"Power: {power}, element: {element}, target: {target}"

def lightball(power: int, element: str, target: str) -> str:
    return f"Power: {power}, element: {element}, target: {target}"

#  Returns a single final value after processing all elements, depending on the operation.
def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if not spells:
        return 0
    if operation not in operations:
        raise ValueError("Operation unknow") 
    
    funct = operations[operation]
    result = reduce(funct, spells) # type: ignore
  
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    if not callable(base_enchantment):
        raise TypeError ("base_enchantment must be function")
  
    fire = partial(base_enchantment, power=50, element="fire")
    freeze = partial(base_enchantment, power=50, element="ice")
    electricity = partial(base_enchantment, power=50, element="elec")
    return {
        "fire": fire,
        "ice": freeze,
        "elec": electricity
        }


def memoized_fibonacci(n: int) -> int:




if __name__ == "__main__":
    print("\n\033[1;34mTesting spell reducer...\033[0m")
    spells_list = [
        10,
        20,
        30,
        40
    ]
    value = spell_reducer(spells_list, "add")
    print(f"Sum: {value}")
    value = spell_reducer(spells_list, "multiply")
    print(f"Product: {value}")
    value = spell_reducer(spells_list, "max")
    print(f"Max: {value}\n")

    print("\n\033[1;34mTesting spell partial...\033[0m")
    enchantment_fire = partial_enchanter(fireball)
    enchantment_ice = partial_enchanter(iceball)
    enchantment_elec = partial_enchanter(lightball)

    print(enchantment_fire["fire"](target="Witch"))
    print(enchantment_ice["ice"](target="Dragon"))
    print(enchantment_elec["elec"](target="Trump"))




# def spell_dispatcher() -> Callable[[Any], str]:

