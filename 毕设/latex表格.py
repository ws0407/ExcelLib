tables = """风险	&等级	&证据强度   &风险	&等级	&证据强度 \\\\
\\midrule
\\textbf{所有危险因素}	&0  &  &\\textbf{社会人口学因素}	&1  & \\\\
\\cline{1-6}
\\textbf{疾病风险}	&1	& &      高龄	&2	&*** \\\\
\\cline{1-3}
\\textbf{躯体功能}	&2	& &      移动限制	&2	&*** \\\\
\\cline{1-3}
	步态和平衡问题	&3	&*** &      跌倒史	&2	&*** \\\\
	视力问题	&3	&*** &      女性	&2	&** \\\\
	听力/前庭功能问题	&3	&** &      人种	&2	&* \\\\
	外周感觉问题	&3	&** &      独居	&2	&** \\\\
	肌肉力量问题	&3	&*** &      睡眠障碍	&2	&** \\\\
	虚弱	&3	&* &      助行器使用	&2	&** \\\\
\\cline{4-6}
	反应时间问题	&3	&*** &  \\textbf{环境风险}	&1	& \\\\
\\cline{1-3}
\\textbf{心理问题}	&2	& &  	鞋具问题	&2	&* \\\\
\\cline{1-3}
	跌倒恐惧	&3	&*** &  	家居环境问题	&2	&* \\\\
	焦虑	&3	&** &  	外部环境问题	&2	&* \\\\
\\cline{4-6}
	执行功能受损	&3	&*** &  \\textbf{行为风险}	&1	& \\\\
\\cline{4-6}
	处理速度下降	&3	&** &  	吸烟	&2	&** \\\\
	选择性注意力受损	&3	&* &      饮酒 &2	&** \\\\
\\cline{1-3}
\\textbf{疾病问题}	&2	& &      身体活动不足 &2	&** \\\\
\\cline{1-6}
	痴呆症	&3	&*** &  \\textbf{代谢风险}	&1	& \\\\
\\cline{4-6}
	认知障碍	&3	&** &      高BMI（体重指数）	&2	&* \\\\
	中风	&3	&*** &      低骨密度 &2	&*** \\\\
\\cline{4-6}
	帕金森氏症	&3	&*** &  \\textbf{药物使用}	&1	& \\\\
\\cline{4-6}
	白质病变	&3	&* &  	精神活性药物	&2	&*** \\\\
	抑郁症	&3	&*** &  	抗抑郁药物	&2	&*** \\\\
	失禁	&3	&** &  	抗精神病药物	&2	&*** \\\\
	急症	&3	&** &  	苯二氮卓类药物	&2	&** \\\\
	前庭疾病	&3	&** &  	抗高血压药	&2	&* \\\\
	关节炎	&3	&** &  	抗心律不齐药	&2	&* \\\\
	足步问题	&3	&** &  	阿片类药物	&2	&** \\\\
	眩晕	&3	&** &  	抗炎药	&2	&* \\\\
	直立性低血压	&3	&* &  	酒精使用	&2	&* \\\\
	-& - & - &     4+种药物联合用药	&2	&*** \\\\"""
lines = tables.split("\n")
for i in range(len(lines)):
    if '&' in lines[i]:
        lines[i] = lines[i].replace('\\', '').strip()
        lines[i] = [_.strip() for _ in lines[i].split('&')]

flag = False
for i in range(len(lines) - 1):
    if '\\' not in lines[i]:
        if flag or '饮酒' in lines[i]:
            flag = True
            j = i + 1
            if '\\' in lines[j]:
                j += 1
            lines[i][3:] = lines[j][3:]
        lines[i] = '\t&\t'.join(lines[i]) + '\\\\'
lines[-1] = '\t&\t'.join(lines[-1]) + '\\\\'

print("\n".join(lines))