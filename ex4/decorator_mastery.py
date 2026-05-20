from typing import Callable
from functools import wraps
import time


# Decorator function that measures and logs execution time
def spell_timer(func: Callable) -> Callable:
    if not callable(func):
        raise TypeError("func must be a function")

    # Preserve the original function's metadata (name, docstring, etc.)
    @wraps(func)
    # Universal wrapper using *args and **kwargs to accept any parameters
    def wrapper(*args, **kwargs) -> str:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Spell completed in {duration:.3f} seconds")
        return result

    return wrapper

# Apply the decorator: fireball is now automatically timed whenever it 
# is called
@spell_timer
def fireball(duration: int) -> str:
    time.sleep(duration)
    return "Result: Fireball cast!"


def power_validator(min_power: int) -> Callable:

# decorator de validation de parametre:
# - creer une usine de decorator qui valide les niveaux de pouvoirs
# -  



# def retry_spell(max_attempts: int) -> Callable:



# class MageGuild:
# @staticmethod
# def validate_mage_name(name: str) -> bool:


# def cast_spell(self, spell_name: str, power: int) -> str:


if __name__ == "__main__":
    print("\n\033[1;34mTesting spell timer...\033[0m")
    print(fireball(2))

    print("\n\033[1;34mTesting retrying spell...\033[0m")
    
    print("\n\033[1;34mTesting MageGuild...\033[0m")
