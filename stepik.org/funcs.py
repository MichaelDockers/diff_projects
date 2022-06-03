from cgi import test
from functools import reduce
from re import L
from turtle import rt 
 
floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]
 
# Исправьте этот код
map_result = list(map(lambda num: round(num ** 2, 1), floats))
filter_result = list(filter(lambda name: len(name) > 4 and name == name[::-1], words))
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
 
print(map_result)
print(filter_result)
print(reduce_result)





data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

res = ', '.join([city[0] for city in sorted(filter(lambda city_type: city_type[2] == 'primary' and city_type[1] > 10_000_000, data), key=lambda city_type: city_type[0])])

print(f'Cities: {res}')


func = lambda x: True if (x % 19 == 0 or x % 13 == 0) else False

func2 = lambda x: True if (x[0].lower() == 'a' and x[-1].lower() == 'a') else False

is_non_negative_num = lambda x: True if (set(x).issubset(set('1234567890.')) and x.count('.') <= 1) else False

is_num = lambda x: True if (set(x).issubset(set('1234567890.-')) and x.count('.') <= 1 and x.count('-') <= 1 and x[1:].count('-') == 0) else False

words = [
    'beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 
    'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 
    'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 
    'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb'
    ]

print(*sorted(filter(lambda x: len(x) == 6, words)))

numbers = [
    46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 
    36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 
    4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33
    ]

print(*list(map(lambda x: x // 2 if x % 2 == 0 else x, filter(lambda x: (x % 2 != 0 and x <= 47) or (x % 2 == 0), numbers))))

city_data = [
    (19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), 
    (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), 
    (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')
    ]

for pop, city in sorted(city_data, key=lambda x: x[1][-1], reverse=True):
    print(f'{pop}: {city}')

ru_data = [
    'год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 
    'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']

print(*sorted(ru_data, key=lambda x: (len(x), x)))

mixed_list = [
    'tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 
    2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 
    'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 
    'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 
    894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 
    2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 
    'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]

print(max(mixed_list, key=lambda x: x if isinstance(x, int) else 0))

mixed_list_2 = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']

print(*sorted(mixed_list_2, key=lambda x: (isinstance(x, str), x)))

input_string = '244 11 120'

print(*map(lambda x: 255 - x, map(int, input_string.split())))
# print(*map(lambda x: 255 - x, [int(item) for item in input().split()]))


def evaluate(mult, cnt):
    coef_num = len(mult)
    return reduce(lambda a, b: a + b, map(lambda x, y: x * cnt ** (coef_num - y), mult, range(1, coef_num + 1)), 0)


mult = [2, 4, 3]
cnt = 10

print(evaluate(mult, cnt))

def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(x in command for x in ignore)

print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))

countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for country, capital, pop in zip(countries, capitals, population):
    print(f'{capital} is the capital of {country}, population equal {pop} people.')

abscissas = [0.637, -0.411, -0.247, 1.658, 0.061]
ordinates = [-0.78, -1.374, 0.762, 0.306, -0.614]
applicates = [-1.317, -0.444, -0.572, -0.341, 0.295]

# abscissas = map(float, input().split())
# ordinates = map(float, input().split())
# applicates = map(float, input().split())

print(all(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= 4, zip(abscissas, ordinates, applicates))))

def is_ip(ip_str: str) -> bool:
    if all(map(lambda x: x.isdigit(), ip_str.split('.'))):
        return all(map(lambda x: 0 <= int(x) <= 255, ip_str.split('.')))
    else:
        return False


def is_ip_ver2(ip_str: str) -> bool:
    return all(map(lambda x: x.isdigit() and 0 <= int(x) <= 255, ip_str.split('.')))


print(is_ip_ver2('192.0168a.0.255'))

n, m = 20, 30

print(*filter(lambda y: all([True if (int(k) != 0 and int(y) % int(k) == 0) else False for k in str(y)]), range(n, m + 1)))


test_pass = 'abcAB7k'

print('YES' if all(
    [len(test_pass) >= 7, 
    any(map(lambda x: x.isdigit(), test_pass)), 
    any(map(lambda x: x.islower(), test_pass)), 
    any(map(lambda x: x.isupper(), test_pass))]
    ) else 'NO')



# school_db = all(reduce(lambda x, y: x + y, [[any([int(input().split()[1]) == 5 for _ in range(int(input()))])] for iter in range(int(input()))]))
# print(school_db)

def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
    return (f'To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!')

print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
print()
print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2', 'Василь Ярошевич', 23))

def pretty_print(data, side='-', delimiter='|'):
    data_str = f' {delimiter} '.join(map(str, data))
    tab_str_size = len(data_str) + 2
    tab_str = f' {side * tab_str_size} '
    print(tab_str)
    print(f'{delimiter} {data_str} {delimiter}')
    print(tab_str)

pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

print([1, 2] + [] + [3, 4])

def concat(*arg, sep=' '):
    return f'{sep}'.join(map(str, arg))


print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))


def product_of_odds(data):
    return reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 1, data), 1)

print(product_of_odds([1, 2, 5, 7, 25]))

words_1 = 'the world is mine take a look what you have started'.split()
 
print(*map(lambda x: f'"{x}"', words_1))

numbers_1 = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*filter(lambda x: str(x) != str(x)[::-1], numbers_1))

numbers_2 = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
sorted_numbers = sorted(numbers_2, key=lambda x: sum(x) / len(x), reverse=True)
print(sorted_numbers)


def mul7(x):
    return x * 7
    
    
def add2(x, y):
    return x + y


def add3(x):
    return x + 3
    
    
def add33(x, y, z):
    return x + y + z
    
    
def call(func, *arg):
    return func(*arg)


def compose(func1, func2):
    return lambda x: func1(func2(x))


print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add33, 10, 30, 40))
print(call(bool, 0))

print(compose(mul7, add3)(2))

def arithmetic_operation(x):
    arithmetic_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    return arithmetic_dict[x]

print(arithmetic_operation('*')(10, 20))

sample_str = 'cate Frog cat FROGs bee CATERS mouse cATwalk dolphin mOus Cats CatAlo'.split()
print(*sorted(sample_str, key=lambda x: x.lower()))
print(*sorted(sample_str, key=str.lower))

def gematriya(x):
    return sum(ord(w) - 65 for w in x.upper())

#words_2 = [input() for cnt in range(int(input()))]
# print(words_2)
# print(list(map(gematriya, words_2)))
# print(*sorted([input() for cnt in range(int(input()))], key=lambda x: (sum([ord(w) - 65 for w in x.upper()]), x)), sep='\n')

# ip_list = [
#     '128.199.44.24',
#     '128.199.201.245',
#     '143.198.168.95',
#     '172.67.181.62',
#     '172.67.222.111',
#     '172.67.10.90',
#     '45.8.106.59',
#     '203.13.32.156',
#     '172.67.181.194'
#     ]
# ip_list_int = [list(map(int, input().split('.'))) for _ in range(int(input()))]


# for ip in sorted(ip_list_int, key=lambda x: reduce(lambda x, y: x + y, map(lambda x, y: x * 256 ** (3 - y), x, range(4)))):
#     print('.'.join(list(map(str, ip))))

#print(*ip_list_int)
import random

file_path = r'C:/Distr/nums.txt'
test_file = open(file_path, 'r', encoding='utf-8')
# content = list(map(int, filter(str.strip, test_file)))
test_1 = [int(x) for x in test_file.read().split()]
print(test_1)
test_file.close()

file_path_2 = r'C:/Distr/prices.txt'
price_file = open(file_path_2, 'r', encoding='utf-8')
price_file_parsed = [int(x.split()[1]) * int(x.split()[2]) for x in price_file.readlines()]
print(sum(price_file_parsed))
price_file.close()

file_path_3 = r'C:/Distr/text.txt'
with open(file_path_3, 'r', encoding='utf-8') as text_file:
    print(text_file.read()[::-1])

file_path_4 = r'C:/Distr/data.txt'
with open(file_path_4, 'r', encoding='utf-8') as text_file_2:
    print(*text_file_2.readlines()[::-1], sep='')

file_path_5 = r'C:/Distr/lines2.txt'
with open(file_path_5, 'r', encoding='utf-8') as text_file_3:
    max_str = max(map(len, text_file_3))
    text_file_3.seek(0)
    print(*filter(lambda x: len(x) == max_str, text_file_3), sep='')

file_path_6 = r'C:/Distr/numbers2.txt'
with open(file_path_6, 'r', encoding='utf-8') as text_file_4:
    print(*map(lambda x: sum(map(int, x)), [line.split() for line in text_file_4.readlines()]), sep='\n')

# file_path_7 = r'C:/Distr/nums2.txt'
# with open(file_path_7, 'r', encoding='utf-8') as text_file_5:
#     print(reduce(lambda x, y: int(x) + int(y), filter(lambda x: x.isdigit(), text_file_5.read())))

file_path_7 = r'C:/Distr/nums2.txt'
with open(file_path_7, 'r', encoding='utf-8') as text_file_5:
    parsed_content = [''.join([x if x.isdigit() else ' ' for x in line]) for line in text_file_5.readlines()]
    list_of_lines = [sum(map(int, x.split())) for x in parsed_content]
    print(sum(list_of_lines))

file_path_8 = r'C:/Distr/file2.txt'
with open(file_path_8, 'r', encoding='utf-8') as text_file_6:
    loaded_text = [line.split() for line in text_file_6.readlines()]
    print('Input file contains:')
    print(f'{sum([sum(map(len, line)) for line in loaded_text])} letters')
    print(f'{sum([len(line) for line in loaded_text])} words')
    print(f'{len(loaded_text)} lines')


from itertools import permutations

in_str = 'abs'

print(*permutations(in_str))