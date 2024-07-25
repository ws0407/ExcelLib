# 输入只有整数的两个list：A和B
# 输出它们的交集C
# 注意A和B中分别可能有相同的元素，但C中不要有相同的元素

A = [1,1,1,3,4,5,'a', '#@', 'aaa', 1000000000000000000]
B = [2,3,1,0,1, '#@', 100000000000000]

# print(set(A) & set(A))


C = []
for a in A:
    C += [a] if a in B and a not in C else []

print(C)


# 模拟人的思路
# 1. 遍历A
# 2. 遍历B
# 3. 判断A和B中的元素是否相同
# 4. 如果相同，判断C中是否有相同的元素，没有则追加到C中

C = []
for a in A:
    if a in B and a not in C:
            C.append(a)
print(C)

C = [val for idx, val in enumerate([_ for _ in A if _ in B]) if val not in [_ for _ in A if _ in B][:idx]]    # 去重

print("C:", C)


# # 一句话
# c = [val for idx, val in enumerate([j for j in [i for i in a if i in b]]) if val not in [j for j in [i for i in a if i in b]][:idx]]
# print(c)