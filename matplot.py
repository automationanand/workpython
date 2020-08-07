import matplotlib.pyplot as plt
import numpy as np
# simple plot
x=np.linspace(0,5,20)
y=x**2
plt.plot(x,y,color='purple',linewidth=3,linestyle='-.',marker='o',markersize=4,
         markerfacecolor='yellow',markeredgecolor='red')
plt.xlabel('X axis')
plt.ylabel('y axis')
plt.title('matlab')
plt.show()

# subplot
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b', label='linear')  # name of curve
plt.legend()
plt.show()

# single figure with plot
fig=plt.figure()
axes =fig.add_axes([0.1,0.1,0.8,0.8])  # take four objects from 0 to 1
axes.plot(x,y)
plt.title("figure space")
plt.xlabel('X axis')
plt.ylabel('y axis')
plt.show()

#figure with two plot
fig=plt.figure()
axes =fig.add_axes([0.1,0.1,0.8,0.8])  # take four objects from 0 to 1
axes1 =fig.add_axes([0.2,0.5,0.4,0.3])
plt.show()

# subplot with figure
fig,axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y)
axes[1].plot(x,y)
plt.title("subplot")
plt.xlabel("x axis")
plt.show()
#
fig=plt.figure(figsize=(8,2))           # set figure size
fig.savefig('matlab2.png',dpi=200)      # saving figure with other formates
plt.show()


# # different plots
plt.bar(x,y)
plt.show()
plt.scatter(x,y)
plt.show()
plt.hist(x,y,color='red')
plt.show()
plt.pie(x,y)
plt.show()