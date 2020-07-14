def kabisatcek(thn):
    if thn % 100 == 0:
        return thn % 400 == 0
    return thn % 4 == 0

def hitungtanggal(h,b,t,rnge):
    x=0
    y=0
    z=b
    zz=t
    while True:
        if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
            maxx=31
        elif b==4 or b==6 or b==9 or b==11:
            maxx=30
        elif b==2:
            maxx=kabisatcek(t)
            if maxx==False:
                maxx=28
            else:
                maxx=29
        if rnge>=maxx:
            rnge-=maxx
            x+=1
            if b<12:
                b+=1
            else:
                b=1
                t+=1
        else:
            break
    while True:
        if x>=12:
            x-=12
            y+=1
        else:
            break
    if h+rnge>=maxx:
        h=(h+rnge)-maxx
        x+=1
    else:
        h=h+rnge
    if z+x>=12:
        z=(z+x)-12
        y+=1
    else:
        z=z+x
    if len(str(h))<2:
        h="0"+str(h)
    if len(str(z))<2:
        z="0"+str(z)
    return h,z,y+zz

def acaktanggal():
    pass
