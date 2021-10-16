import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed) #seed()使每次生成的随机数字相同
#情况一
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound) #随机生成一个r
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)

#情况二
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

#情况三
cycles = [] #第三问闭环
reversed_dict_per_length = {} #第四问翻转字典
flag = [] #建立一个空列表暂存值
for key in mapping.keys(): #在mapping的key值中循环
    if key in flag: #如果key在flag中则跳出本次循环，执行下一次循环
        continue
    cycle = [key] #否则将key值存入cycle当中
    while True:
        key = mapping[key] #找到当前key值在mapping当中对应的value值，将其赋值给新的key
        if key == cycle[0]: #如果value值对应的新的key值与cycle[0]即原来的key值相等
            cycles.append(cycle) #在总闭环cycles中加入其中一个闭环cycle列表
            flag.extend(cycle) #依次加入一个闭环的每个key值
            break
        elif key not in mapping.keys() or key in cycle: #如果value值对应的新key不在mapping的key值或者已经存在在闭环cycle当中则跳出
            break
        else: #如果value值对应的新key在mapping当中存在且闭环cycle中还没有该值则加入到cycle当中
            cycle.append(key) 
           
print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)

#情况四
reversed_dic = {} #先建立一个初始翻转字典
for key, value in mapping.items(): #在原始mapping中循环
    if value not in reversed_dic: #如果value不在翻转字典中
        reversed_dic[value] = [key] #加入一个键值对，使value->key，key->value
    else:
        reversed_dic[value].append(key) #如果value即新的key已经存在于翻转字典当中，则在这个新key的value值后加入新的value

for key, value in reversed_dic.items(): #用len(value)进行比较，数值相同的放在一个key中
    if len(value) not in reversed_dict_per_length: #如果该长度不在字典中
        reversed_dict_per_length[len(value)] = {} #在原字典中拿该value值的长度作为key值建立一个新字典
    reversed_dict_per_length[len(value)][key] = value #存入key对应的value值
   
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length) #格式化输出
