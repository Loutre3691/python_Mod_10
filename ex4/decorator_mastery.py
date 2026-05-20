from typing import Callable
from functools import wraps
import time


# Decorator function that measures and logs execution time
def spell_timer(func: Callable) -> Callable:
    if not callable(func):
        raise TypeError(f"{func} must be a function")

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


# p1. THE FACTORY: It accepts the custom arguments for the decorator (e.g., min_power)
def power_validator(min_power: int) -> Callable:
    # 2. THE DECORATOR: This is created by the factory and receives the function to modify
    def decorator(func: Callable) -> Callable:
        # @wraps preserves the original function's name and documentation (metadata)
        @wraps(func)
        # 3. THE WRAPPER: This is the actual container that replaces the original function
        def wrapper(*args) -> str:
            # Extract the first argument passed to the function (the spell's power)
            power = args[0]
            if power >= min_power:
                return func(*args)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


@power_validator(min_power=50)
def frezzball(power: int) -> str:
    return "Frezzball cast"
        

def retry_spell(max_attempts: int) -> Callable:

    def decorator(func: int) -> Callable:

        @wraps(func)
        def wrapper(*args) -> str:
            if 

            return ""

        return wrapper

    return decorator


@power_validator(min_power=3)
def fireball() -> str:
    return "Fireball cast"

@power_validator(min_power=3)
def frezzball() -> str:
    return "Frezzball cast"


# relancer le decorator:
# - creer un decorator qui relance les sort qui ont ehcoues
# - si la fonction leve une exception, reesayer jusqu'a max_attemps fois
# - print "Spell failed, retrying... (attempt n/max_attempts)"
# - si tous les tentatives echouent, return "Spell casting failed after max_attempts attempts"
# - si une tentative reussi, return son resultat normalement




# class MageGuild:
# @staticmethod
# def validate_mage_name(name: str) -> bool:
# def cast_spell(self, spell_name: str, power: int) -> str:


if __name__ == "__main__":
    print("\n\033[1;34mTesting spell timer...\033[0m")
    print(fireball(0.1))

    print("\n\033[1;34mTesting power validator...\033[0m")
    print(f"test with power 40: {frezzball(40)}")
    print(f"test with power 60: {frezzball(60)}")

    print("\n\033[1;34mTesting retrying spell...\033[0m")
    retry_spell()


    # print("\n\033[1;34mTesting MageGuild...\033[0m")
