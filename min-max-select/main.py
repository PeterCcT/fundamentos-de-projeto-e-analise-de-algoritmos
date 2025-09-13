
from typing import Union


Number = Union[int, float]

def get_min_and_max(values: list[Number]) -> tuple[Number, Number]:
    if len(values) == 1:
        return values[0], values[0]

    list_middle_index = len(values) // 2
    left_values = values[:list_middle_index]
    right_values = values[list_middle_index:]

    left_result = get_min_and_max(left_values)
    right_result = get_min_and_max(right_values)
    return min(left_result[0], right_result[0]), max(left_result[1], right_result[1])

print('Executando algoritmo de busca de min e max')
values = [3,4,5,3,1,2]
print(f'Entrada, {values}\nResultado:', get_min_and_max(values))