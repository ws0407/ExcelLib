s = """NCS 自然代码序列（Natural Code Sequence）
AST 抽象语法树（Abstract Syntax Tree）
CFG 控制流图（Control Flow Graphs）
DFG 数据流图（Data Flow Graphs）
CPG 代码属性图（Code Property Graphs）
PDG 程序依赖图（Program Dependence Graphs）
CNN 卷积神经网络（Convolutional Neural Networks）
RNN 循环神经网络（Recurrent Neural Networks）
GRU 门控循环单元（Gated Recurrent Unit）
LSTM 长短期记忆网络（Long Short-Term Memory）
Tree-LSTM 树形结构的长短期记忆网络（Tree-structural Long Short-Term Memory，Tree-LSTM）
GCN 图卷积神经网络（Graph Convolutional Network）
GGNN 图循环神经网络（Gated Graph Neural Networks）
ResNet 残差网络（Residual Network）
FS-GNN 流敏感图神经网络（Flow-Sensitive GNN）
MP-NN 消息传递神经网络（Message-Passing Neural Networks）
CSF 类分离特征（Class-Separation Features）
LLMs 大语言模型（Large Language Models）
GAT 图注意力网络（Graph Attention Network）
PoIs 兴趣点（Points of Interest），指漏洞可能触发的位置
ReliVul 本课题提出的漏洞代码库（Real-world Line-level Vulnerability dataset）
CP 共形预测（Conformal Prediction）
HyliVD 本课题提出的漏洞检测模型（Hybrid Line-level Vulnerability Detector）
WLJAN 单词-标签联合注意力网络（Word-Label Joint Attention Network）
IFA 初始误报（Initial False Alarm）"""

s = s.split("\n")
for i in range(len(s)):
    first_blank = s[i].find(' ')
    s[i] = '  \item[' + s[i][:first_blank] + ']' + s[i][first_blank:]
print("\n".join(s))