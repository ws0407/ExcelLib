import numpy as np
import pandas as pd


# 定义一个表格
df = pd.DataFrame({
        'Index': list(range(1, 13)),
        'A': ['one', 'one', 'two', 'three'] * 3,
        'B': ['A', 'B', 'C'] * 4,
        'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
        'D': np.random.randint(low=10, high=20, size=12, dtype='int'),
        'E': np.random.randn(12),
        'F': np.random.randint(low=20, high=30, size=12, dtype='int'),
    })
print(df)

# 数据筛选：筛选A中为one的数据
print(df[df['A'] == 'one'])
# 数据筛选：筛选F中大于25的数据
print(df[df['F'] > 25])
# 数据筛选：筛选B中为A或C的数据
print(df[(df['B'].isin(['A', 'C']))])

# 删除F列
df.drop('F', axis=1, inplace=True)  # 或者df = df.drop(columns=['F'])
print(df)

# 数据透视表
df_pivot = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
print(df_pivot)

# 分割成两个表
df_1 = df[['Index', 'A', 'B', 'C']]
print(df_1)
df_2 = df[['Index', 'D', 'E']]
print(df_2)

# 检查重复值
print(df_1['Index'].duplicated().value_counts())
print(df_2['Index'].duplicated().value_counts())

# vlookup合并
df_m = pd.merge(df_1, df_2, on='Index')
print(df_m)

# 保存到Excel
df.to_excel("new_data.xlsx", sheet_name = "sheet1", index = False, na_rep = 0, inf_rep = 0)
