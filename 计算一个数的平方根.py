# 1.判断是否有整数根
# 2.如果没有遍历除数
# 3.如果除数没有整数开平方数，遍历商

# def math(a):
# 	b = False

# 	for i in range(2 , a):
# 		b = a / i
# 		if b == i:
# 			print(f"正负{i}")
# 			return

# 	for i in range(2 , a):
# 		b = a / i

# 		if type(b) == int:
# 			for j in range(2 , i):
# 				if (i / j) == j:
# 					print(f"正负{j}倍的根号{b}")
# 					return

# 			for j in range(2 , i):
# 				if (b / j) == j:
# 					print(f"正负{j}倍的根号{i}")
# 					return

# 	b = True

# 	if b:
# 		print("正负根号%d" % a)

# if __name__ == '__main__':
# 	a = eval(input('请输入一个数字:'))
# 	math(a)



def math(a):
	b = False

	for i in range(2 , a):
		b = a / i
		if b == i:
			print(f"正负{i}")
			return

	for i in range(2 , a):
		b = a / i

		
		for j in range(2 , i):
			if (i / j) == j:
				print(f"正负{j}倍的根号{b}")
				return

		for j in range(2 , i):
			if (b / j) == j:
				print(f"正负{j}倍的根号{i}")
				return

	b = True

	if b:
		print("正负根号%d" % a)

if __name__ == '__main__':
	a = eval(input('请输入一个数字:'))
	math(a)
	