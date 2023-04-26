#x = [40,20,-10]
#y = [20,90,50]

#aux_1 = (y[0]-x[0])
#aux_2 = (y[1]-x[1])
#aux_3 = (y[2]-x[2])

#aux = [aux_1,aux_2,aux_3]

#print(aux)

import numpy as np
import time


#aux = np.zeros([1,3])
#x = np.random.randint(-90,90,(10,3))
#for i in x[:,]:
#    salida = i-aux
#    print(str(i), str(aux),"resultado : ", str(salida))
#    print("")
#    aux = i
    
listado = [1,23,3,4,5,6]
listado2 = [2,3,4,5,6]
listado3 = [listado,listado2]
print(listado3)
print(listado3[0][1])
