# 1-) region parametresini all_contracts içerisindeki key değeri ile eşleştir.
# ve karşılığındaki listi return et.
def get_contracts_by_region(region: str) -> list:
    all_contracts = {
        "Kaedwen": ["ghoul", "wraith"],
        "Skellige": ["drowner", "leshen"],
        "Blaviken": ["vampire", "griffin"]
    }
    return all_contracts[region]

# 2-) reward değeri şu formül ile hesaplanır. FORMULA = base_gold X (1 + difficulty X 0.1)
def calculate_reward(base_gold: int, difficulty: int) -> float:
     return base_gold * (1 + difficulty * 0.1)


# 3-) monster_name değerini weaknesses dictionary key değeri ile eşleşri ve karşısındaki list değerini return et.
# Unutma, monster_name büyük harflerde içerebilir. Bu durumlarda da doğru key değerini bulabilmelisin.
def get_monster_weakness(monster_name: str) -> list:
    weaknesses = {
        "leshen": ["fire", "dimeritium bomb"],
        "griffin": ["hybrid oil", "aard"],
        "vampire": ["moon dust", "devil's puffball"]
    }
    return weaknesses[monster_name.lower()]


# 4-) difficulty değeri 5'ten büyükse veya region 'Blaviken' ise bu fonksiyon 'True' dönmelidir. Diğer şartlarda fonksiyon 'False' dönmelidir.
def is_high_danger_contract(difficulty: int, region: str) -> bool:
       return difficulty > 5 or region == "Blaviken"


# 5-) Example inputtaki gibi bir liste monsters parametresi ile birlikte gelecektir. Bu listedeki her bir eleman ve kaç adet geççtiği bir dictionar olarak geri dönülecektir.
# Example input: ['ghoul', 'leshen', 'ghoul', 'drowner', 'leshen', 'ghoul']
# Output: {'ghoul': 3, 'leshen': 2, 'drowner': 1}
def summarize_monster_data(monsters: list) -> dict:
    result = {}
    for monster in monsters:
        result[monster] = result.get(monster, 0) + 1
    return result


# 6-) contracts gibi bir list parametre olarak gelecektir. min_rewar değeri her bir contract için reward değerinden büyükse o elemanlar bir list olarak döneceklerdir.
#  Example input: contracts list with reward field
# contracts = [
    #     {"id": 1, "monster": "ghoul", "reward": 300},
    #     {"id": 2, "monster": "drowner", "reward": 150},
    #     {"id": 3, "monster": "leshen", "reward": 500}
    # ]
#  Output: only contracts with reward >= min_reward
def filter_contracts_by_reward(contracts: list, min_reward: int) -> list:
     return [c for c in contracts if c["reward"] >= min_reward]


# 7-) Aşağıdaki listedeki gibi en sık görülen eleman listede bulunup return edilmelidir
# Example input: ['ghoul', 'ghoul', 'leshen', 'drowner', 'ghoul']
# Output: 'ghoul'
def get_most_common_monster(monster_list: list) -> str:
    counts = {}
    for monster in monster_list:
        counts[monster] = counts.get(monster, 0) + 1
    return max(counts, key=counts.get)


# 8-) Aşağıdaki gibi bir contracts listesi parametre olarak alınacaktır. liste difficulty değerine göre küçükten büyüğe göre sıralanarak geri dönecektir.
# contracts = [
#     {"id": 1, "monster": "ghoul", "difficulty": 2},
#     {"id": 2, "monster": "leshen", "difficulty": 5},
#     {"id": 3, "monster": "drowner", "difficulty": 1}
# ]
def sort_contracts_by_difficulty(contracts: list) -> list:
     return sorted(contracts, key=lambda c: c["difficulty"])


# 9-) Witcher adılığı ödüle yaptığı indirim sonrasında alması gereken ücreti hesaplamaktadır.
# reward parametresi orijanl fiyatı, lambda discont ise yapılcak olan indirimi lmabda fonksiyonu olarak alır.
# bu işlemi yapıp en son fiyatı dönen fonksiyonu yazınız.  
def apply_discount(reward: float, lambda_discount) -> float:
    return lambda_discount(reward)


#10-) Görevin her bir bölgede toplamda ne kadar contract olduğunu bulmaktır.
# contracts parametresi aşağıdaki gibi bir dictionary içerir.
# contracts = [
#     {"id": 1, "region": "Kaer Morhen"},
#     {"id": 2, "region": "Kaer Morhen"},
#     {"id": 3, "region": "Blaviken"},
#     {"id": 4, "region": "Novigrad"}
# ]
def count_contracts_by_region(contracts: list) -> dict:
    result = {}
    for contract in contracts:
        region = contract["region"]
        result[region] = result.get(region, 0) + 1
    return result
