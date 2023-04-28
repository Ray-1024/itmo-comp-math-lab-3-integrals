def user_input(methods, names):
    def get_id(message, arr):
        print(message)
        for i in range(len(arr)):
            print(i + 1, ':', arr[i])
        id = int(input())
        assert (id >= 1) and (id <= len(arr))
        return id - 1

    while True:
        try:
            function_id = get_id('Пожалуйста введите номер функции которую желаете проинтегрировать: ', names)
            method_id = get_id('Пожалуйста введите номер метода который желаете использовать: ', methods)
            l = float(input('Пожалуйста введите начало интервала интегрирования: '))
            r = float(input('Пожалуйста введите конец интервала интегрирования: '))
            assert l <= r
            eps = float(input('Пожалуйста введите точность интегрирования: '))
            assert eps >= 0
            return function_id, method_id, l, r, eps
        except:
            print('Упс. Что-то не то. Попробуйте снова.')
