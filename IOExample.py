import math
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
outputfilepath = os.path.join(dir_path,'exampleData.txt')
f = file(outputfilepath,'w')
for i in range(100):
    x = i
    y = i**2 + 0.3*i +4
    f.write('{}\t{}\n'.format(x,y))
f.close()
print 'File {} written'.format(outputfilepath)
f = open('exampleData.txt')
print f.read()
f.close()

