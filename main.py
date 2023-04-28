import data, choice, methods

function_id, method_id, l, r, eps = choice.user_input(data.methods, data.names)

try:
    if method_id == 0:
        for _, i in [('левых', 0), ('средних', 1), ('правых', 2)]:
            value, n = methods.find_integral_and_n(data.functions[function_id], l, r, eps, i)
            print('Найденное значение интеграла методом', _, 'прямоугольников:', value)
            print('Количество разбиений для достижения требуемой точности:', n)
    else:
        value, n = methods.find_integral_and_n(data.functions[function_id], l, r, eps, method_id + 2)
        print('Найденное значение интеграла:', value)
        print('Количество разбиений для достижения требуемой точности:', n)
except:
    print("Упс. При вычислении интеграла что-то пошло не так.")
