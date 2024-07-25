# 输入商品价格和购买数量
price = float(input("请输入商品价格："))
quantity = int(input("请输入购买数量："))

# 判断购买数量并计算销量
if price > 0 and quantity >= 0:
    if quantity >= 10 and price > 50:	# 嵌套if
        discount_rate = 0.8 # 打八折
    # elif quantity < 10 or price <= 50:
    #     discount_rate = 1   # 无折扣
    else:
        discount_rate = 1   # 无折扣
else:
    print("输入错误！")
    exit()
 
total_sales = int(price * quantity * discount_rate)
print("总收入为：", total_sales)