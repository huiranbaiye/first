# 猜数字小游戏
# 程序功能：电脑随机生成一个 1~100 的数字，玩家反复输入猜测，
# 电脑提示"大了"或"小了"，直到猜中为止，并统计一共猜了几次。

import random  # 导入 random 模块，用来生成随机数

# 1. 电脑偷偷想一个 1 到 100 之间的整数
answer = random.randint(1, 100)

# 2. 用一个变量记录玩家猜了多少次，一开始是 0 次
count = 0

print("========== 猜数字小游戏 ==========")
print("我已经想好了一个 1 到 100 之间的数字，快来猜吧！")

# 3. 用 while 循环反复让玩家猜，直到猜中才跳出循环
while True:
    # 让玩家输入一个数字，并把输入的文字转成整数
    user_input = input("请输入你猜的数字：")
    guess = int(user_input)  # 把字符串转成数字，才能比较大小

    # 每猜一次，次数加 1
    count = count + 1

    # 4. 比较玩家猜的数字和正确答案
    if guess > answer:
        print("大了！往小了猜～")
    elif guess < answer:
        print("小了！往大了猜～")
    else:
        # 猜中了，跳出循环
        print(f"恭喜你，猜对了！答案就是 {answer}")
        break  # break 用来结束整个 while 循环

# 5. 循环结束后，告诉玩家一共猜了几次
print(f"你一共猜了 {count} 次。")
print("游戏结束，再见！")
