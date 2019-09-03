import os
filePath = './'
for i,j,k in os.walk(filePath):
    print(i,j,k)