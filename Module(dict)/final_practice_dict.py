"""

# есть словарь песен и их длительности: необходимо указать
# количество песен, а далее найти итоговую длительность всех перечисленных песен
violator_songs = {
    'world in my eyes': 4.86,
    'sweetest perfection': 4.43,
    'personal jesus': 4.56,
    'halo': 4.9,
    'waiting for the night': 6.07,
    'enjoy the silence': 4.20,
    'policy of truth': 4.76,
    'blue dress': 4.29,
    'clean': 5.83
}

count_of_songs = int(input("Сколько песен выбрать? "))
total_min = 0

for _ in range(count_of_songs):
    name = input("Введите название песни: ").lower()
    if name in violator_songs:
        total_min += violator_songs[name]
    else:
        print("Такой песни нет!")

print("Общее время звучания песен: {:.2f}".format(total_min))
"""


data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

data["ETH"]["total_diff"] = 100


