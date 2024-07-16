import pandas as pd

df = pd.read_csv(r"D:\Workspace\workspace_vscode_python\ExcelLib\数据\2023.8-2024.6合并数据.csv")

# 测试数据
# df = pd.DataFrame({
#         'Index': list(range(1, 8)),
#         '交易流水号': ['one', 'one', 'two', 'BBB', 'four', 'three', 'four'],
#         '原交易流水号': [np.nan, np.nan, np.nan, 'two', 'three', np.nan, np.nan],
#     })

# nums = df[df['原交易流水号'].notnull()]['原交易流水号'].tolist()
# # print(df.tail())
# print("共删除", len(nums) * 2, "条数据")
# df = df.drop(df[df['交易流水号'].isin(nums)].index)
# df = df.drop(df[df['原交易流水号'].notnull()].index)


# 一行
df = df.drop(df[(df['交易流水号'].isin(df[df['原交易流水号'].notnull()]['原交易流水号'].tolist())) | (df['原交易流水号'].notnull())].index)

# print(df.tail())

# 保存数据，gbk是中文编码
df.to_csv(r"D:\Workspace\workspace_vscode_python\ExcelLib\数据\2023.8-2024.6合并数据_new.csv", encoding='gbk')
