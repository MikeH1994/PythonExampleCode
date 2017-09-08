import numpy as np
import matplotlib.pyplot as plt
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
outputfilepath = os.path.join(dir_path,'exampleData.txt')
data = np.genfromtxt(outputfilepath)
x = data[:,0]
y = data[:,1]


fig = plt.figure()
ax = fig.add_subplot(111)
xtickLoc = range(0,100,10)
labels = [i*10 for i in range(10)]

ax.plot(x,y,label = r'$\alpha^{-1}_1$',color = 'r')
ax.annotate(r'$\alpha^{-1}_1$',xy = (5,13),fontsize = 16)
plt.title(r'Example Data')
plt.xlabel(r'$\mu$ (GeV)', fontsize = 18)
plt.ylabel(r'$\alpha^{-1}$', fontsize = 18)
plt.xticks(xtickLoc,labels,fontsize = 14)
plt.xlim(xmax = 16.7)
plt.ylim(ymin = 0, ymax = 300)
plt.show()


