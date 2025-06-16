import numpy as np
array = np.full((5,5),None)
string="kotha"
index=0
c=96
for i in range(5):
    for j in range(5):
        if(index<len(string)):
            array[i][j]=string[index]
            index=index+1
for i in range(1,5):
    for j in range(5):
        c=c+1
        if chr(c) in string:
            c=c+1
        if(c==106):
            continue
        array[i][j]=chr(c)
        
        
        

print(array)    
