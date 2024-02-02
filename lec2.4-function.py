# x, y之间所有的整数和
my_sum = lambda x, y : (x + y) * (abs(x - y) + 1) // 2   
print(my_sum(1, 100))	# 5050

# 求字符串每个单词的长度
sentence = "Welcome To Beijing!"
words = sentence.split()
lengths  = map(lambda x:len(x),words)
print(list(lengths))	# [7,2,8]