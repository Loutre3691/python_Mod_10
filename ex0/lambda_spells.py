
# from __future__ import annotations


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    result = list(sorted(artifacts, key=lambda x: x["power"], reverse=True))
    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result = list(filter(lambda x: x["power"] >= min_power, mages))
    return result


def spell_transformer(spells: list[str]) -> list[str]:
    result = list(map(lambda x: "* " + x + " *", spells))
    return result


def mage_stats(mages: list[dict]) -> dict:
    result_max = max(mages, key=lambda x: x["max_power"])["max_power"]
    result_min = min(mages, key=lambda y: y["min_power"])["min_power"]
    average = round((result_min + result_max) / 2, 2)
    new_dict = {
        "max_power": result_max,
        "min_power": result_min,
        "avg_power": average
    }
    return new_dict


if __name__ == "__main__":
    print("\033[1;34mTesting artifact sorter...\033[0m]")
    artifact_list = [
        {"name": "Fire Staff 🔥",
            "power": 92,
            "type": "Fire"},
        {"name": "Crystal Orb 💎",
            "power": 85,
            "type": "psy"},
        {"name": "Sword 🗡️",
            "power": 2,
            "type": "metal"},
    ]
    after_sort = artifact_sorter(artifact_list)
    for i in range(len(after_sort) - 1):
        print(f"{after_sort[i]['name']} ({after_sort[i]['power']} power)"
              f" comes before {after_sort[i+1]['name']}"
              f" ({after_sort[i+1]['power']} power)")

    print("\n\033[1;34mTesting filter power...\033[0m]")
    power_filter_list = [
        {"name": "Marianus",
            "power": 92,
            "element": "Fire"},
        {"name": "Chlogenius",
            "power": 5,
            "element": "Water"},
        {"name": "paconus",
            "power": 15,
            "element": "terre"},
    ]

    min_power = 10
    after_filter = power_filter(power_filter_list, 10)
    print(f"mages with power greater than {min_power}:")
    for i in range(len(after_filter)):
        print(f"- {after_filter[i]['name']} "
              f"({after_filter[i]['power']} power)")

    print("\n\033[1;34mTesting spell tranformer...\033[0m]")
    spell_list = [
        "itchy butt",
        "paco's dung shot",
        "gravity fart"
    ]
    after_transformer = spell_transformer(spell_list)
    for i in range(len(after_transformer)):
        print(f"{after_transformer[i]}", end=" ")

    print("\n")
    print("\033[1;34mTesting stats mage...\033[0m]")
    mage_stats_list = [
        {"name": "Marianus",
            "max_power": 98,
            "min_power": 20},
        {"name": "Chloegenius",
            "max_power": 82,
            "min_power": 20},
        {"name": "Paconus",
            "max_power": 15,
            "min_power": 2},
    ]
    after_stats = mage_stats(mage_stats_list)
    for key, value in after_stats.items():
        print(f"{key}: {value}")
