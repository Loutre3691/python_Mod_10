



def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    artifacts = sorted(artifacts, key=lambda x: x["power"])
    return artifacts

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result = list(filter(lambda x: x["power"] >= min_power, mages))
    return result

def spell_transformer(spells: list[str]) -> list[str]:


# def mage_stats(mages: list[dict]) -> dict:



if __name__ == "__main__":
    artifact_list = [
        {"name": "Fire Staff", 
         "power": 92, 
         "type": "Fire"},
         {"name": "Aqua Bumb", 
         "power": 24, 
         "type": "Water"},
         {"name": "Psycho tornado", 
         "power": 98, 
         "type": "psy"},
         
    ]

    power_filter_list = [
         {"name": "Marianis", 
         "power": 92, 
         "element": "Fire"},
         {"name": "Chlogenius", 
         "power": 5, 
         "element": "Water"},
         {"name": "paconus", 
         "power": 15, 
         "element": "terre"},
         

    ]

    # spell_list = [

    # ]

    # mage_stats_list = [

    # ]


    test = artifact_sorter(artifact_list)
    test2 = power_filter(power_filter_list, 10)
    print(test2)
    # spell_transformer(spell_list)
    # mage_stats(mage_stats_list)