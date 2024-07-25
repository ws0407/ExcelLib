import pandas as pd

# 扩展示例DataFrame
df1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'], 'key2': ['K0', 'K0', 'K1', 'K2'], 'value': [0, 1, 2, 3]})
df2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1'], 'key2': ['K0', 'K0', 'K0'], 'value2': [4, 5, 6]})
print(df1)
print(df2)
# 使用how='outer'进行外连接
result = pd.merge(df1, df2, how='inner', on=['key1', 'key2'])

print(result)

