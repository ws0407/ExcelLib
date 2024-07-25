import pandas as pd
import numpy as np
import time

filepath = 'D:/Workspace/workspace_vscode_python/ExcelLib/数据/'
filename = '2023.8-2024.6合并数据_format.csv'
# filename = '120109194004221029-总.csv'
filename2 = '异地门诊合并_1-2_split.csv'
# filename2 = '120109194004221029-门诊.csv'

s_t = time.time()
df = pd.read_csv(filepath + filename)
df2 = pd.read_csv(filepath + filename2)
print("读取数据耗时:", time.time() - s_t, "秒")

df = df.rename(columns={'身份证号':'身份证号码'})

# 根据日期和身份证号码求两个dataframe的交集
df3 = pd.merge(df, df2, how='inner', on=['日期', '身份证号码', '总金额'])
df3.to_csv(filepath + '120109194004221029_merge.csv', index=False, encoding='utf-8')
"""
合并结果：82715条数据
原总数据：179208条数据
门诊数据：118941条数据
"""
exit()

filepath = 'D:/Workspace/workspace_vscode_python/ExcelLib/数据/'
filename = '2023.8-2024.6合并数据_new.csv'
filename2 = '异地门诊合并_1-2.csv'

s_t = time.time()
df = pd.read_csv(filepath + filename)
df2 = pd.read_csv(filepath + filename2)
print("读取数据耗时:", time.time() - s_t, "秒")

df[['日期', '时间']] = df['交易日期'].str.split(' ', expand=True)
df2[['日期', '时间']] = df2['收费日期'].str.split(' ', expand=True)

df['日期'] = pd.to_datetime(df['日期'])
df2['日期'] = pd.to_datetime(df2['日期'])

df.drop(['交易日期'], axis=1, inplace=True)
df2.drop(['收费日期'], axis=1, inplace=True)

df.to_csv(filepath + '2023.8-2024.6合并数据_split.csv', index=False, encoding='utf-8')
df2.to_csv(filepath + '异地门诊合并_1-2_split.csv', index=False, encoding='utf-8')

exit()

filepath = 'D:/Workspace/workspace_vscode_python/ExcelLib/数据/'
filename = '2023.8-2024.6合并数据_new.csv'
filename2 = '异地门诊合并_1-2.csv'

s_t = time.time()
df = pd.read_csv(filepath + filename)
df2 = pd.read_csv(filepath + filename2)
print("读取数据耗时:", time.time() - s_t, "秒")

df = df[df['身份证号']=='120109194004221029']
df.to_csv(filepath + '120109194004221029-总.csv', encoding='gbk')

df2 = df2[df2['身份证号码']=='120109194004221029']
df2.to_csv(filepath + '120109194004221029-门诊.csv', encoding='gbk')

exit()

s_t = time.time()
df = pd.read_csv(filepath + filename)
df2 = pd.read_csv(filepath + filename2)
df3 = pd.read_csv(filepath + filename3)
print("读取数据耗时:", time.time() - s_t, "秒")

print('2023.8-2024.6合并数据_new.csv: \n', df['医疗类别'].value_counts())
print('\n\n异地门诊合并_1-2.csv: \n', df2['医疗类别'].value_counts())
print('\n\n异地挂号合并_1-2.csv: \n', df3['医疗类别'].value_counts())

exit()

s_t = time.time()
filepath = 'D:/Workspace/workspace_vscode_python/ExcelLib/数据/' \
           '2023.8-2024.6合并数据.csv'

df = pd.read_csv(filepath)
print("读取数据耗时:", time.time() - s_t, "秒")

df = df.drop(df[df['险种类别'] == '合计'].index)

df.to_csv(filepath[:-4] + '_new.csv')

exit()

s_t = time.time()
filepath = 'D:/Workspace/workspace_vscode_python/ExcelLib/数据/' \
           '异地门诊患者结算数据20230801-20240630新.xls'

sheet_names = ['门诊20230801-20240131', '门诊20240201-0630', 
               '挂号20230801-1231', '挂号20240101-0430', 
               '挂号20240501-0630']

# df = pd.read_excel(filepath, dtype=str, sheet_name=None)
df1 = pd.read_excel(filepath, dtype=str, sheet_name=sheet_names[2])
print("读取数据耗时:", time.time() - s_t, "秒")
df2 = pd.read_excel(filepath, dtype=str, sheet_name=sheet_names[3])
print("读取数据耗时:", time.time() - s_t, "秒")
df3 = pd.read_excel(filepath, dtype=str, sheet_name=sheet_names[4])
print("读取数据耗时:", time.time() - s_t, "秒")
# 合并两个数据表
df = pd.concat([df1, df2, df3], ignore_index=True)
print("合并完成，正在保存...")

df.to_csv(filepath[:-4] + '_3-5.csv')

exit()

# 测试数据
# df = pd.DataFrame({
#         'Index': list(range(1, 8)),
#         '交易流水号': ['one', 'one', 'two', 'BBB', 'four', 'three', 'four'],
#         '原交易流水号': [np.nan, np.nan, np.nan, 'two', 'three', np.nan, np.nan],
#     })

nums = df[df['原交易流水号'].notnull()]['原交易流水号'].tolist()
# print(df.tail())
print("共删除", len(nums) * 2, "条数据")
df = df.drop(df[df['交易流水号'].isin(nums)].index)
df = df.drop(df[df['原交易流水号'].notnull()].index)

# 一行
# df = df.drop(df[(df['交易流水号'].isin(df[df['原交易流水号'].notnull()]['原交易流水号'].tolist())) /
#                  | (df['原交易流水号'].notnull())].index)

# print(df.tail())

# 保存数据，gbk是中文编码
df.to_csv(r"D:/Workspace/workspace_vscode_python/ExcelLib/数据/2023.8-2024.6合并数据_new.csv", encoding='gbk')
