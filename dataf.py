import pandas as pd
import matplotlib.pyplot as plt
df =pd.DataFrame([[1,1,3,4],[5,1,7,8],[9,10,11,12],[14,15,16,17]] ,columns=['A','B','C','D'],index=['row1','row2','row3','row4'])
print(df) # Data frame
       #A   B   C   D
#row1   1   2   3   4
#row2   5   6   7   8
#row3   1  10  11  12
#row4  14  15  16  17
print(df.replace(to_replace=1,value=1000))

# print(df['A']) # Selecting single column
# print(df.A)    # Selecting single column
# print(df[['A','C']]) # Selecting TWO column
# df['E']=df['A']+100  # new column E addition
# drop_col=df.drop('B',axis=1) # axis=1 for clumn drop and axis=0 for row drop
# drop_row = df.drop('row1', axis=0) # becuase numpy shape of 2d array always (0,1) row with ZERO index and column with ONE index
# sel_row= df.loc['row2']  # selecting specific rows by name
# sel_mutliple_row=df.loc[['row1','row2']] # selecting multiple rows
# sel_row_index = df.iloc[1] # selecting row with specific index
# sel_perticular_value = df.loc['row3','B']  # 10 output
# sel_row_column = df.loc[['row1','row2'],['A','E']]  # Selecting rows and columns
#
# d=df[df>11]      # value greather then 11 and NA for all other
# d.dropna()       # drop all NA included rows becuase defalut axis=0
# d.dropna(axis=1)# drop all NA included columns becuase axis=1
# d.dropna(thresh=2) # row having minimum 2 non NA entry
# d.fillna(value='Alert')  # fill NA with Alert
# df['A'].unique() # return unique value of specific column
# df['A'].nunique() # lenght of unique values
# S=df[df['A']<10]   # drop as per condition in data frame
# t=df['A'].apply(lambda x:x*2)  # apply function or values
# f=df.pivot_table(values='A',index=['C','D'],columns='B')  # creating table as we want index and columns
# #df.read_csv('abc.csv')
# #df.to_csv('abc',index=False) # While converting to csv index should be false else it will create index as cloumn
# df.columns  # list the  clumns
# len(df.index)    # total rows in dataframe
# df.info()# number of columns and rows/number of entry in each row.
# df['B'].value_counts()  # total repeated values in specific columns
# # pandas with visualization
# # df['A'].hist()
# # df.plot.area()
# # df.plot.bar()
# # df.plot.scatter(x='A',y='B',c='red',figsize=[8,2])
# # df.plot.box()
# # df.plot.kde()
# # plt.show()
# df.describe() # detail min,max ,mean,std etc
# print('hi',df.iloc[:,1].values) # values used to exclude index colums from data frame
# print(df.iloc[:,:0]) # indexing start from dataframe index columns