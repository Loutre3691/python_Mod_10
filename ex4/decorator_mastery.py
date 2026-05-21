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
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, ** kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {attempt} attempts"

        return wrapper

    return decorator


attempt_count = 0 
@retry_spell(max_attempts=3)
def spell(power: int) -> str:
    global attempt_count
    attempt_count += 1
    if attempt_count <= 3:
        raise ValueError("Spell failed!")
    return "Waaaaaaagh spelled !"



def power_validator(min_power: int):
    def decorator(func):  

        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power', args[2] if len(args) > 2 else 0)
            if power < min_power:
                    return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator   

class MagiGuild():

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str):
            return False
        if len(name) < 3:
            return False
        if not all(char.isalpha() or char.isspace() for char in name):
            return False
        return True


    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    print("\n\033[1;34mTesting spell timer...\033[0m")
    print(fireball(0.1))

    print("\n\033[1;34mTesting power validator...\033[0m")
    print(f"test with power 40: {frezzball(40)}")
    print(f"test with power 60: {frezzball(60)}")

    print("\n\033[1;34mTesting retrying spell...\033[0m")
    print(spell(5))
    print(spell(5))

    print("\n\033[1;34mTesting MageGuild...\033[0m")
    result_valid = MagiGuild.validate_mage_name("Paco la frite")
    print(result_valid)
    result_false = MagiGuild.validate_mage_name("Paco_la_frite")
    print(result_false)

    guild = MagiGuild()
    print(guild.cast_spell("POOPBALL", 55))
    print(guild.cast_spell("POOPBALL", 5))
    






