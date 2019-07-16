import pandas as pd

#创建DataFrame
R = pd.DataFrame([
    'A',
    'B',
    'C'
 ])

#获取DataFrame的数据数量
R_len = len(R)

#连接DataFrame中所有数据
R_mix = ''
for i in range(0,R_len):
	R_mix = ''.join([R_mix, R[0][i]])

#输出
print(R_len)

print(R_mix)