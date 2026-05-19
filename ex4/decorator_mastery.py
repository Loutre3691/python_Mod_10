from typing import Callable
from functools import wraps

def fireball(time: int) -> int:
    return 10


def spell_timer(func: Callable) -> Callable:
    if not callable(func):
        raise TypeError("func must be a function")
    
    print(f"Casting {fireball.__name__}..." )
    @wraps
    def time() -> int:
        print ("Spell completed in seconds")
    

    return time
# decorator d'execution temporel:
# - creer un decorator qui mesure le temps d'execution de la fonction
# - Print "Casting function_name..." avant l execution
# - print "Spell completed in X.XXX seconds" apres l execution ( 3 decimal places)
# _ utilise funtools.wraps pour preserver les metadata de la fonction original



# def power_validator(min_power: int) -> Callable:



# def retry_spell(max_attempts: int) -> Callable:



# class MageGuild:
# @staticmethod
# def validate_mage_name(name: str) -> bool:


# def cast_spell(self, spell_name: str, power: int) -> str:


if __name__ == "__main__":
    print("\n\033[1;34mTesting spell timer...\033[0m")
    spell_timer(fireball)


    print("\n\033[1;34mTesting retrying spell...\033[0m")
    
    print("\n\033[1;34mTesting MageGuild...\033[0m")
