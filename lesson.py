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
#     'float':'o\'nlik son',
#     'string':'ip',
#     'dictionary':'lug\'at',
#     'list':'ro\'yxat',
#     'tyuple':'o\'zgartirib bo\'lmas ro\'yxat'
# }
#
# buzz = input('Enter the key word: ')
#
# if buzz in key_words:
#     print(f"""{buzz}ning tarjimasi: "{key_words[buzz]}\"""")
# else:
#     print('Bunday so\'z mavjud emas')


# 15-lesson exercise-1

# for key_w, value_w in sorted(key_words.items()):
#     print(key_w, '-', value_w)

# exercise-2

# countries = {
#     'Ozbekiston': 'Toshkent',
#     'Amerika': 'Vashington',
#     'Xitoy': 'Pekin',
#     'Koreya': 'Seul',
#     'Fransiya': 'Parij',
#     'Tojikiston': 'Dushanbe',
#     'Rassiya': 'Moskva',
# }
#
# print('Davlatlar nomi:')
# for key_w in sorted(countries):
#     print(key_w)
#
# print("""
#
# Poytaxtlar nomi:""")
# for value_w in sorted(countries.values()):
#     print(value_w)
#
# foo = input("""
#
# Enter the name of the country: """).title()
# capital = countries.get(foo)
#
# if capital == None:
#     print(f'There is no info about {foo}')
# else:
#     print(f'{capital.title()} is the capital of {foo.upper()}')

# exercise-3

# food = {
#     'manti': 20000,
#     'lagmon': 30000,
#     'hadisa': 40000,
#     'chuchvara':20000,
#     'mandu':15000
# }
#
# print('3 ta taom buyurtma bering.')
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-food:").lower())
#
# for buyurtma in buyurtmalar:
#     if buyurtma in food:
#         print(f"{buyurtma.title()} {food[buyurtma]} sum")
#     else:
#         print(f"Soory, we have no {buyurtma}")

# new-lesson
# my_book = {
#     'name': 'IELTS Practice',
#     'author': 'James Bon',
#     'price': 40000,
#     'year': 2023
# }
#

# print(type(my_book))

# Nesting
# exercise-1
ilm_fandagi_shaxslar = {
    'Abu Abdulloh Muhammad ibn Ismoil': {
        'yil': 810,
        'shahar': 'Buxoro',
        'yosh': 60
    },
    'Alisher Navoiy': {
        'yil': 1441,
        'shahar': 'Xirot',
        'yosh': 60
    },
    'Erkin Vohidov': {
        'yil': 1936,
        'shahar': 'Farg\'ona',
        'yosh': 80
    },
    'Abdulla Qodiriy': {
        'yil': 1894,
        'shahar': 'Toshkent',
        'yosh': 44
    }
}

#
# for ism, malumot in ilm_fandagi_shaxslar.items():
#     info = f"{ism} {malumot['yil']}-yilda tug'ilgan {malumot['shahar']}da tavallud topgan. {malumot['yosh']} yil umr ko'rgan"
#
# print(info)


# exercise-2
# ilm_fandagi_shaxslar['Abu Abdulloh Muhammad ibn Ismoil']['asarlar'] = ['al-jome', 'al-sahih', 'al-adab', 'al-mufrad']
# ilm_fandagi_shaxslar['Abdulla Qodiriy']['asarlar'] = ['O\'tgan kunlar']
# ilm_fandagi_shaxslar['Alisher Navoiy']['asarlar'] = ['Xamsa', 'Lison ut-tayr']
# ilm_fandagi_shaxslar['Erkin Vohidov']['asarlar'] = ['tong nafasi']
#
# for ism, info in ilm_fandagi_shaxslar.items():
#     print(f'\n{ism}ning asarlari: ')
#     for i in info['asarlar']:
#         print(i)



# new lesson
# try:
#     qwe = int(input('son kiriting: '))
#
#     if qwe % 2 == 0:
#         print('bu son juft')
#     else:
#         print('bu son toq')
# except ValueError:
#     print('iltimos faqatgina son kiriting: ')
#
# for i in range(5):
#     print(i)


# def first_non_consecutive(arr):
#     for i in range(1, len(arr)):
#         if arr[i] != arr[i-1] + 1:
#             return arr[i]
#         return None
#
# print(first_non_consecutive([1,2,3,4,6,7,8]))



# def find_smallest_int(arr):
#     smallest = arr[0]
#     for num in arr:
#         if num < smallest:
#             smallest = num
#     return smallest
# print(find_smallest_int([1,2,3,4,-5,7]))




# def sum_of_nums(a, b, *args):
#     foo = 0
#     print(args, type(args))
#     for i in args:
#         foo += i
#     return a + b + foo
# print(sum_of_nums(a, b, b))


#
# foo, bar, buzz, *goo = (1,2,3,4,5,6,7,8,9,9)
# print(foo, bar, buzz, goo, type(goo))




# def my_function(**args):
#     type(args)
#     for key, value in args.items():
#         print(f"The value of {key} is {value}")
#
# my_function(name="John", age=30, city="New York")



