
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

    print("\n\033[1;34mTesting memory vault...\033[0m")
    vault = memory_vault()
    vault["store"]("secret", "42")
    vault["store"]("hero", "WonderWOman")

    print(f"store 'secret' = {vault['recall']('secret')}")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Store 'hero' = {vault['recall']('hero')}")
    print(f"Recall 'hero': {vault['recall']('hero')}")
    print(f"Recall 'unknown': {vault['recall']('inconnu')}")
