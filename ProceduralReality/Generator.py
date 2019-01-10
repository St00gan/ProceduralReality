import random
fil=open('data/y','r').readline().strip()
yhigh=int(fil)
fil=open('data/x','r').readline().strip()
xwide=int(fil)
field = []
started = False
fil=open('data/y','w')
fil.write(str(yhigh))
fil.close()
fil=open('data/x','w')
fil.write(str(xwide))
fil.close()
for y in range(yhigh):
    row = []
    for x in range(xwide):
        row.append('?')
    field.append(row)

frontier = []

def carve(y, x):
    extra = []
    field[y][x] = '.'
    if x > 0:
        if field[y][x-1] == '?':
            field[y][x-1] = ','
            extra.append((y,x-1))
    if x < xwide - 1:
        if field[y][x+1] == '?':
            field[y][x+1] = ','
            extra.append((y,x+1))
    if y > 0:
        if field[y-1][x] == '?':
            field[y-1][x] = ','
            extra.append((y-1,x))
    if y < yhigh - 1:
        if field[y+1][x] == '?':
            field[y+1][x] = ','
            extra.append((y+1,x))
    random.shuffle(extra)
    frontier.extend(extra)

def harden(y, x):
    field[y][x] = '#'



def check(y, x, nodiagonals = True):
    edgestate = 0
    if x > 0:
        if field[y][x-1] == '.':
            edgestate += 1
    if x < xwide-1:
        if field[y][x+1] == '.':
            edgestate += 2
    if y > 0:
        if field[y-1][x] == '.':
            edgestate += 4
    if y < yhigh-1:
        if field[y+1][x] == '.':
            edgestate += 8
    
    if nodiagonals:
        if edgestate == 1:
            if x < xwide-1:
                if y > 0:
                    if field[y-1][x+1] == '.':
                        return False
                if y < yhigh-1:
                    if field[y+1][x+1] == '.':
                        return False
            return True
        elif edgestate == 2:
            if x > 0:
                if y > 0:
                    if field[y-1][x-1] == '.':
                        return False
                if y < yhigh-1:
                    if field[y+1][x-1] == '.':
                        return False
            return True
        elif edgestate == 4:
            if y < yhigh-1:
                if x > 0:
                    if field[y+1][x-1] == '.':
                        return False
                if x < xwide-1:
                    if field[y+1][x+1] == '.':
                        return False
            return True
        elif edgestate == 8:
            if y > 0:
                if x > 0:
                    if field[y-1][x-1] == '.':
                        return False
                if x < xwide-1:
                    if field[y-1][x+1] == '.':
                        return False
            return True
        return False
    else:
        if  [1,2,4,8].count(edgestate):
            return True
        return False
    
xchoice = random.randint(0, xwide-1)
ychoice = random.randint(0, yhigh-1)
carve(ychoice,xchoice)
branchrate = 0

from math import e

while(len(frontier)):
    pos = random.random()
    pos = pos**(e**-branchrate)
    choice = frontier[int(pos*len(frontier))]
    if check(*choice):
        carve(*choice)
    else:
        harden(*choice)
    frontier.remove(choice)

for y in range(yhigh):
    for x in range(xwide):
        if field[y][x] == '?':
            field[y][x] = '#'
    

ms=""
m=[]
h=[]
for y in range(yhigh):
    s = ''
    for x in range(xwide):
        s += field[y][x]
    ms=(ms+s+'\n')
    m.append(s)
for i in m[int((yhigh-1)/2)]:
    h.append(i)

h[int((xwide-1)/2)]='X'
h="".join(h)
m[int((yhigh-1)/2)]=h
fa=open('maps/defaultnum.mz','w')
fb=open('maps/defaultmap.mz','w',encoding='utf-8')
fb.write('█'*(xwide+2)+'\n')
fa.write('#'*(xwide+2)+'\n')
for i in m:
    l=i.replace('#','█')
    l=l.replace('.',' ')
    fb.write('█'+l+'█\n')
    for a in range(0,len(i)+1):
        i=i[:a].replace('.',str(random.randint(0,9)))+i[a:]
    if started == True:
     fa.write('#'+i+'#\n')
    else:
     fa.write('S'+i+'#\n')
     started = True
fb.write('█'*(xwide+2))
fa.write('#'*(xwide+2))
fa.close()
fb.close()
import Drawer
