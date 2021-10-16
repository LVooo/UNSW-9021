import sys

on = '\u26aa' #开的unicode字符
off = '\u26ab' #关的unicode字符
code = input('Enter a non-strictly negative integer: ').strip() #去除输入数字前后空格
try:
    if code[0] == '-': #第一位为负号的话报错
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1): #找出数字前0的个数
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

octal = '0' * nb_of_leaading_zeroes + f'{int(code):o}' #转化为八进制的数字
reoctal = reversed(octal) #翻转字符串使其从右至左读入

#1.Reverse input and set a move dic
#建立对应题目要求的移动字典，拿坐标系来判断东南西北
move = {
    '0': (0, 1),
    '1': (1, 1),
    '2': (1, 0),
    '3': (1, -1),
    '4': (0, -1),
    '5': (-1,-1),
    '6': (-1, 0),
    '7': (-1, 1)
}

list = [(0,0)] # 建立一个带有起始点(坐标原点)的列表用来存放出现过的坐标点
start_x = 0 #起始x
start_y = 0 #起始y

# 2.Store the coordinate points obtained by the movement into the list
list = [(0,0)] # has initial coordinate point(0,0)
for i in reoctal:
    x, y = move[i] #在move字典中查找i值对应的坐标点并赋值给x和y
    start_x += x #按照对应坐标点依次变化
    start_y += y
    if (start_x, start_y) not in list: #如果坐标点不在list列表里则加入，如果已存在则删除，对应开关
        list.append((start_x, start_y))
    else:
        list.remove((start_x, start_y))

# 3.Use max() and min() to find the boundary value in order to build the matrix,
# set the initial horizontal and vertical coordinates
#(set to unreasonable values：The largest coordinate is smaller than the smallest coordinate)
max_x = 0 #设置初始坐标边界值（不合理情况：max比min大）
min_x = 1
max_y = 0
min_y = 1

for i in list: #寻找边界值
    x, y = i
    max_x = max(x, max_x)
    min_x = min(x, min_x)
    max_y = max(y, max_y)
    min_y = min(y, min_y)

# 4.Loop through the boundary value to find whether the array exists in the list，
# store it in a str and then print out
switch = '' #存放开关
for y in range(max_y, min_y-1, -1): #按边界值从上到下，从左至右的方向循环每个坐标点
    for x in range(min_x, max_x+1, 1):
        if (x, y) in list: #如果循环到的坐标点在list中将开的图形加入到字符串当中，否则加入关的图形
            switch += on
        else:
            switch += off
    switch += '\n' #循环一遍x轴后加入一个换行符
print(switch) #打印最后图形
