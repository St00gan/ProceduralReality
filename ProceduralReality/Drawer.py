import numpy as np
from PIL import Image
list_im = []
list_im2 = []
p=0
perc=0
fil=open('data/y','r').readline().strip()
yhigh=int(fil)
for v in range(0,yhigh+2):
 f=open('maps/defaultnum.mz','r').readlines()[v:v+1]
 f=f[0].strip()
 for i in f:
     list_im.append('tiles/'+i+'.jpg')
     imgs    = [ Image.open(i) for i in list_im ]
     min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
     imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
     
     imgs_comb = Image.fromarray( imgs_comb)
 imgs_comb.save('parts/p'+str(v)+'.jpg')
 list_im2.append('parts/p'+str(v)+'.jpg')
 list_im=[]
 p=p+(1/(yhigh+2))
 perc=p
 perc=round(perc,2)
 perc=perc*100
 print((str(int(perc))+'%'),end='\r',flush=True)
imgs    = [ Image.open(i) for i in list_im2 ]
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
imgs_comb = Image.fromarray( imgs_comb)
imgs_comb.save( 'maps/visual.jpg' )
