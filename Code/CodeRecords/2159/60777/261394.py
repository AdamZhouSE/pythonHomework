tar=int(input())
exp=''

while(tar>=1000):
    tar=tar-1000
    exp+='M'
    
while(tar>=900):
    exp+='CM'
    tar-=900
    
while(tar>=500):
    tar-=500
    exp+='D'
    
while(tar>=400):
    tar-=400
    exp+='CD'
    
while(tar>=100):
    tar-=100
    exp+='C'
    
while(tar>=90):
    tar-=90
    exp+='XC'
    
while(tar>=50):
    tar-=50
    exp+='L'
    
while(tar>=40):
    tar-=40
    exp+='XL'

while(tar>=10):
    tar-=10
    exp+='X'

while(tar>=9):
    tar-=9
    exp+='IX'

while(tar>=5):
    tar-=5
    exp+='V'

while(tar>=4):
    tar-=4
    exp+='IV'
    
for i in range(tar):
    exp+='I'
    
print(exp)