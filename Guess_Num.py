# 產生一個隨機(不要印出來)
# 讓使用者輸入數字去猜
# 猜對的話 印出"終於猜對了"
# 猜錯的話 要告訴他比答案大/小

import random
start = input('請決定隨機數字開始值: ')
end   = input('請決定隨機數字結束值: ')

start = int(start)
end   = int(end)

r = random.randint(start, end)
count = 0

while True:
	count += 1 # count = count +1
	num = input('請猜數字 ')
	num = int(num)
	if num == r:
		print('終於猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('你要猜更小一點的數字')
	elif num < r:
		print('你要猜更大一點的數字')
	print('這是你猜的第', count, '次')

