import seaborn as sb
import pandas as pd
from matplotlib import pyplot as plt
tip=sb.load_dataset('tips')
print(tip.head())  # default till 4 index values form tips dataset
print (sb.get_dataset_names()) #To view all the available data sets in the Seaborn library
#Distribution plots
# sb.distplot(tip['total_bill'],kde=True)# kde =False remove line from bar,
# sb.jointplot(x='total_bill',y='tip',data=tip,) # default scatter plot if kind='hex' hexagone representation kind='reg' kind='kde 'etc
# sb.pairplot(tip) # joint plot for every columns
#sb.pairplot(tip,hue='sex')  # catagarise columns data
# sb.rugplot(tip['total_bill']) # dash mark for very distribution as distplot
# sb.kdeplot(tip['total_bill']) # kernal density plot
# plt.show()

# # categorical plots
# sb.set_style('whitegrid') # background color
# sb.countplot(x='sex',data=tip)
# sb.boxplot(x='sex',y='total_bill',data=tip)
# sb.violinplot(x='sex',y='total_bill',data=tip)
# sb.stripplot(x='sex',y='total_bill',data=tip,jitter=True)
# sb.swarmplot(x='sex',y='total_bill',data=tip)# similar to strip and violin plot but points not overlapped
# plt.show()

# #Matrix plots
# tc=tip.corr() # to convert matrix form by correlation
# print(tc)
# sb.heatmap(tc,annot=True,cmap='coolwarm') # ANNOT indicate values on map
# plt.show()
# regression plot
sb.lmplot(x='total_bill',y='tip',data=tip)
plt.show()