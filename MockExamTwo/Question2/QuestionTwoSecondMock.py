items_info = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.7,
    "grape": 1.2
}

sales_info = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 12
}

empty1 = {}
empty2 = {}
missing_key1 = {
    "apple": 5,
    "orange": 3
}
missing_key2 = {
    "apple": 5
}

def total_revenue(items:dict, sales:dict) -> float:
    revenue = 0
    for x in sales:
        revenue += items[x] * sales[x] #I think I did it??? omg
    return revenue

print(total_revenue(missing_key1, missing_key2))