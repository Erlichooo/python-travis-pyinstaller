#你的python代码
import pandas as pd

SPP_fname = '202111 SPP 1015133.xlsx'
MGT_fname = ''
# 202111 SPP 1015133.xlsx
# 工作簿2.xlsx

def define_fname():
    global SPP_fname
    global MGT_fname
    SPP_fname = input('「请输入 SPP 文件名全称」 ：')
    MGT_fname = input('「请输入 MGT 文件名全称」 ：')
    # print(MGT_fname)

def SPPTotalDis_Merge2MGT(SPP_fname, MGT_fname):
    # 定义 SPP、MGT文件的 dataframe
    SPP_DF = pd.read_excel(SPP_fname, skiprows=1)
    MGT_DF = pd.read_excel(MGT_fname)
    print(MGT_DF)

    # SPP 按 「Linked Account」分组，按「Total Discount」求和。并存在 tmp 变量
    tmp = SPP_DF.groupby('Linked Account')['Total Discount'].sum()
    print(tmp)
    # tmp与 MGT_DF 按照 Linked Account ID 合并，并生成新 MGT_DF_new
    MGT_DF_new= MGT_DF.merge(tmp, how='left', left_on='Linked Account ID', right_on='Linked Account')

    print(MGT_DF.head())
    print(SPP_DF.head())
    print(MGT_DF_new.head())
    MGT_DF_new.to_excel(f'new_{MGT_fname}', index=False)    # 写入新文件，index=False 忽略索引列
    # print(MGT_DF.loc[MGT_DF['Linked Account ID'] == 114664981934].get(['Linked Account ID', 'Total Discount']))
    # print(MGT_DF.loc(MGT_DF['Linked Account ID'] == '114664981934'))

    print('\n********************************')
    print('* 🎉🎉 恭喜你，新的MGT文件生成啦！！*')
    print('********************************\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    define_fname()
    print(MGT_fname)
    SPPTotalDis_Merge2MGT(SPP_fname, MGT_fname)
