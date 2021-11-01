import math
item_1 = 3
item_2 = 6

result_sum = item_1 + item_2
result_subtr = item_2 - item_1
result_multi = item_1 * item_2
result_exp = item_1 ** item_2
result_m_exp = math.pow(item_1, item_2)
result_s_root = item_2 ** (0.5)
result_mp_s_root = math.sqrt(item_2)
result_division = item_1 / item_2
result_m_floor = math.floor(result_division)
result_m_ceil = math.ceil(result_division)
result_int = int(result_division)
result_no_division_loss = item_1 // item_2

print(item_1, '+', item_2, '=', result_sum)
print(item_2, '-', item_1, '=', result_subtr)
print(item_1, '*', item_2, '=', result_multi)
print(item_1, '^', item_2, '=', result_exp)
print(item_1, '^', item_2, '=', result_m_exp)
print('Квадратный корень из числа', item_2, 'это', result_s_root)
print('Квадратный корень из числа', item_2, 'это', result_mp_s_root)
print(item_1, '/', item_2, '=', result_division)
print('Ближайшее меньшее целое число от примера выше', result_m_floor)
print('Ближайшее большее целое число от примера выше', result_m_ceil)
print('Явное приведение к меньшему числу', result_int)
print( item_1, '//', item_2, '=', result_no_division_loss)

item_3 = 8
item_3 += 5
item_3 -= 5
item_3 *= 3
item_3 /= 2
item_3 **= 2
item_3 **= 0.5
item_3 %= 5

print(item_3)

b_item_t = True
b_item_f = False

b_item_relut_sum = b_item_t + b_item_f
b_item_relut_subtr = b_item_t - b_item_f
b_item_relut_multi = b_item_t * b_item_f
# b_item_result_division = b_item_t / b_item_f
b_item_1_int = int(b_item_t)
b_item_2_int = int(b_item_f)

print(b_item_relut_sum)
print(b_item_relut_subtr)
print(b_item_relut_multi)
# print(b_item_result_division)
print(b_item_1_int)
print(b_item_2_int)