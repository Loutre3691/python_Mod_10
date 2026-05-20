
from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Callable, Any


def fireball(power: int, element: str, target: str) -> str:
    return f"Power: {power}, element: {element}, target: {target}"


def iceball(power: int, element: str, target: str) -> str:
    return f"Power: {power}, element: {element}, target: {target}"


def lightball(power: int, element: str, target: str) -> str:
    return f"Power: {power}, element: {element}, target: {target}"


#  Returns a single final value after processing all elements,
# depending on the operation.
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
    result = reduce(funct, spells)  # type: ignore
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    if not callable(base_enchantment):
        raise TypeError("base_enchantment must be function")

    fire = partial(base_enchantment, power=50, element="fire")
    freeze = partial(base_enchantment, power=50, element="ice")
    electricity = partial(base_enchantment, power=50, element="elec")
    return {
        "fire": fire,
        "ice": freeze,
        "elec": electricity
        }


# Infinite cache size ensures previously calculated Fibonacci numbers
# are never evicted.
@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# Uses singledispatch to dynamically route the spell effect
# based on the argument's data type (int, str, or list).
def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(arg) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _damage_sort(arg) -> str:
        return f"{arg} damage"

    @dispatch.register(str)
    def _enchentment(arg) -> str:
        return arg

    @dispatch.register(list)
    def _multicast(arg) -> str:
        return f"{len(arg)} spells"

    return dispatch


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

    print("\n\033[1;34mTesting memoized fibonacci...\033[0m")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\n\033[1;34mTesting spell dispatcher...\033[0m")
    spells = [
        "spell1",
        "spell2",
        "spell3"
    ]
    test = spell_dispatcher()
    print(f"Damage spell: {test(42)}")
    print(f"Enchantment: {test('fireball')}")
    print(f"Multi-cast: {test(spells)}")
    print(test(None))
