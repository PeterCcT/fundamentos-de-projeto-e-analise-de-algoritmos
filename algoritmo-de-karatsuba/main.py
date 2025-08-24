def get_max_len_from_numbers(x, y):
    return max(len(str(x)), len(str(y)))

def karatsuba_it(x, y):
    if x < 10 and y < 10:
        return x * y
    max_size = get_max_len_from_numbers(x, y)
    half_size = max_size // 2
    digit_splitter = 10**half_size

    a_left, b_right = divmod(x, digit_splitter)
    c_left, d_right = divmod(y, digit_splitter)

    left_result = karatsuba_it(a_left, c_left)
    right_result = karatsuba_it(b_right, d_right)
    middle_result = karatsuba_it((b_right + a_left), (d_right + c_left))

    full_left_result = left_result * 10**(2*half_size)
    adjusted_middle_result = (middle_result - left_result - right_result) * 10**half_size

    return full_left_result + adjusted_middle_result + right_result


print('Executando algoritmo de Karatsuba')
print('x = 1234')
print('y = 5678')
print(f'Resultado = {karatsuba_it(1234, 5678)}')