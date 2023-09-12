# name = input('ismingizni kiriting: ')

# a = int(input('a sonni kiriting: '))
# b = int(input('b sonni kiriting: '))

buzz = 0

# 1-ifoda
# i = 20
#
# while i <= 30:
#     print(i)
#     i = i + 1


# 2-ifoda
# foo = 1
# bar = len(name)
#
# while foo < bar:
#     print(name[foo])
#     foo += 2


# example masala

# while a <= b:
#     print(a)
#     buzz += a
#     a += 1
# print(buzz)


# 1-masala

# while a > b:
#     a = a - b
#     buzz += 1
# print(a, buzz)


# HELLO Function of Python

# def positive_negative_numbs(numb):
#     if numb > 0:
#         print(f"{numb} is positive number")
#     else:
#         print(f"{numb} is negative number")
#
# positive_negative_numbs(a)



# def degree(numb, numb_first):
#     max_elem = max(numb, numb_first)
#     max_elem = print(max_elem ** 2)
#     return max_elem
#
# degree(a, b)


# def even_odd(numb, numb_first):
#     for i in range(numb, numb_first):
#         if i % 2 == 0:
#             print(i)
#
# even_odd(a,b)


# new lesson
# 18-lesson exercise-1
#
# products = []
#
# while True:
#     foo = input('Enter the product name: ')
#     products.append(foo)
#     if foo == '' or foo == '0':
#         break
#     else:
#         buzz += 1
#         continue
#
# if '' in products:
#     products.remove('')
# elif '0' in products:
#     products.remove('0')
# print(products)


# 14-lesson exercise-1
# my_friends = {
#     'friend1': {
#         'name': 'Qiqi',
#         'age': 36,
#         'country': 'London'
#     },
#     'friend2': {
#         'name': 'Lusy',
#         'age': 33,
#         'country': 'USA'
#     }
# }
#
# info_friends = f"My first friend is {my_friends['friend1']['name']}, she's {my_friends['friend1']['age']}. She was born in {my_friends['friend1']['country']}"
# print(info_friends)

# exercise-2
# meals_of_my_family = {
#     'dad': 'meet',
#     'mum': 'palov',
#     'sister': 'hadisa'
# }
#
# # print(meals_of_my_family.items())
#
# for name, food in meals_of_my_family.items():
#     if name in ['dad', 'mum', 'sister']:
#         txt_meal = f'{name}\'s favourite food is {food}'
#         print(txt_meal)

# exercise-3
# key_words = {
#     'integer':'butun son',
#     'flost':'o\'nlik son',
#     'string':'ip',
#     'dictionary':'lug\'at',
#     'list':'ro\'yxat',
#     'tyuplr':'o\'zgartirib bo\'lmas ro\'yxat'
# }
#
# buzz = input('Enter the key word: ')
#
# if buzz in key_words:
#     print(f"""{buzz}ning tarjimasi: "{key_words[buzz]}\"""")
# else:
#     print('Bunday so\'z mavjud emas')