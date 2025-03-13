"""
输入：非传染性疾病（Non-Communicable Diseases，NCDs）
输出：\item[NCDs] 非传染性疾病（Non-Communicable Diseases）
"""
tables = """非传染性疾病（Non-Communicable Diseases，NCDs）
世界卫生组织（World Health Organization，WHO）
疾病控制优先（Disease Control Priorities，DCP）
全球疾病负担数据库（Global Burden of Disease，GBD）
伤残调整生命年损失（Disability-adjusted Life Years，DALYs）
遵循系统综述和荟萃分析的首选报告项目（Preferred Reporting Items for Systematic Reviews and Meta-analyses，PRISMA）
循证医学文献检索格式（Patient, Intervention, Comparison, Outcome, Study的缩写，PICOS）
贝叶斯年龄-周期-队列（Bayesian Age-Period-Cohort Model，BAPC）
长短期记忆网络（Long Short-Term Memory，LSTM）
人群归因分数（Population Attributable Fraction，PAF）
人力资本法（Human Capital Approach，HCA）
欧洲跌倒预防协作网（Prevention of Falls Network Europe，ProFaNE）
体重指数（Body Mass Index，BMI）
国际身体活动问卷（The International Physical Activity Questionnaire，IPAQ）
起立行走测试（the Timed Up and Go，TUG）
质量调整生命年（Quality-Adjusted Life Years，QALY）
踏步垫训练（Step-Mat-Training，SMT）
英国国家卫生服务系统（National Health Service System，NHS）
年度百分比变化（Annual Percentage Change，APC）
平均年度百分比变化（Average Annual Percentage Change，AAPC）
年龄-周期-队列模型（Age-Period-Cohort，APC）
集成嵌套拉普拉斯近似（Integrated Nested Laplace Approximation，INLA）
早死所致的寿命损失年（Years of Life Lost，YLL）
疾病引起的健康寿命年损失（Years Lived with Disability，YLD）
中国健康与营养调查（China Health and Nutrition Survey，CHNS）
不确定性区间（Uncertainty interval，UI）
普通最小二乘（Ordinary Least Squares，OLS）
递归神经网络（Recurrent Neural Networks，RNN）
循证医学（Evidence-Based Medicine，EBM）
医学主题词（Medical Subject Headings，MeSH）
平衡量表得分（Berg Balance Scale，BBS）"""

tables = tables.split("\n")
for i in range(len(tables)):
    if '（' not in tables[i]:
        continue
    chinese_name = tables[i][:tables[i].find('（')]
    english_name = tables[i][tables[i].find('（') + 1: tables[i].find('，')]
    denotation = tables[i][tables[i].find('，') + 1: tables[i].find('）')]
    tables[i] = '\\item[' + denotation + '] ' + chinese_name + '（' + english_name + '）'

print("\n".join(tables))