### 条件控制

if - elif - else

条件不需要小括号，语句块不需要大括号。以冒号和换行表示一个模块的开始，以相同长度的缩进表示归属于同一个模块。

```python
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```

```python
# 输入商品价格和购买数量
price = float(input("请输入商品价格："))
quantity = int(input("请输入购买数量："))

# 判断购买数量并计算销量
if price > 0 and quantity > 0:
    if quantity >= 10 and price > 50:	# 嵌套if
        discount_rate = 0.8 # 打八折
    elif quantity < 10 or (quantity >= 10 and price <= 50):
        discount_rate = 1   # 无折扣
else:
    print("输入错误！")
    exit()
 
total_sales = price * quantity * discount_rate
print("销量为：", total_sales)
```

常见判断运算符

| 操作符     | 描述                               |
| ---------- | ---------------------------------- |
| `<`      | 小于                               |
| `<=`     | 小于或等于                         |
| `>`      | 大于                               |
| `>=`     | 大于或等于                         |
| `==`     | 等于，比较两个值是否相等           |
| `!=`     | 不等于                             |
| `or`     | 或，类似 `C++` 的 `\|\|`        |
| `and`    | 且，类似 `C++` 的 `&&`         |
| `not`    | 非，类似 `C++` 的 `!`          |
| `is`     | 是，同一个对象（同一块内存）       |
| `is not` | 不是，不是同一个对象（同一块内存） |

类似于`C++`的`switch...case...`，python有`match...case...`

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

mystatus=400
print(http_error(400))
```
