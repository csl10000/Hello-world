# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:14:36 2020

@author: songl
"""

print('..........杨老师.............')
temp = input("不妨猜一下现在我内心里想的是哪个数字：")
guess = int(temp)
while guess != 520:
    temp = input("不妨猜一下现在我内心里想的是哪个数字：")
    guess = int(temp)
    if guess == 520:
        print("你是我心里的蛔虫吗？")
        print("哼，猜中了也没有奖励")
    else:
        if guess > 500:    
            print("大啦！")
        else:
            print("小了！")   
print("游戏结束，不玩啦")
