

def find_two_multipliers_for_product(product):
    product = int(product)
    list_of_multipliers = list(range(1, 10))
    multipliers = []
    for i in list_of_multipliers:
        for j in list_of_multipliers:
            if i * j == product:
                multipliers.append((i, j))
    return multipliers


def find_three_multipliers_for_product(product):
    product = int(product)
    list_of_multipliers = list(range(1, 10))
    multipliers = []
    for i in list_of_multipliers:
        for j in list_of_multipliers:
            for k in list_of_multipliers:
                if i != j and i != k and j != k:
                    if i * j * k == product:
                        multipliers.append((i, j, k))
    return multipliers


two_multipliers = find_two_multipliers_for_product(36)
print(two_multipliers)
three_multipliers = find_three_multipliers_for_product(36)
print(three_multipliers)
