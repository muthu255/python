import pandas as pd



df1=pd.read_excel('D:\Studies\Python\practice\Dept.xlsx')
df2=pd.read_excel('D:\Studies\Python\practice\Dept.xlsx')
#df1=pd.read_csv('file name',delimiter=''')



print(df1)
print(df2)
for index,row in df1.iterrows():
    print('-------')
    print(row)
for index,row in df2.isnull():
        print(index,row)
print(df1.iloc[2,2]==df1.iloc[1,2])


