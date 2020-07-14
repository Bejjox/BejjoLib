import random
AZ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
az="abcdefghijklmnopqrstuvwxyz"
num="0123456789"
def char(count=1,upper=True,lower=True,numeric=True):
    rs=""
    l=list()
    if upper==True:
        rs+=AZ
    if lower==True:
        rs+=az
    if numeric==True:
        rs+=num

    for x in range(count):
        r=""
        r+=rs[random.randint(0,len(rs)-1)]
        l.append(r)
    if count==1:
        return l[0]
    else:
        return l
