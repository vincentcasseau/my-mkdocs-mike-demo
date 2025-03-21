# - adaptCells (array) -
# adapts a cells with respect to b points
import Intersector as XOR
import Converter as C
import Converter.Internal as I 
import Generator as G
import numpy
import KCore.test as test

a = G.cartHexa((0.,0.,0.), (0.1,0.1,0.1), (5,5,5))
aTH4 = C.convertArray2Tetra(a, split='withBarycenters')
a = C.convertArray2NGon(a); a = G.close(a)
aTH4 = C.convertArray2NGon(aTH4); aTH4 = G.close(aTH4)
#C.convertArrays2File([a], 'a.plt')

n = C.getNCells(a)
nodal_vals = numpy.empty((n,), dtype=I.E_NpyInt)
nodal_vals[:] = 2

## HEXA static adaptation
m = XOR.adaptCells(a, nodal_vals, sensor_type=3, smoothing_type=1)

m = XOR.closeCells(m[0])
#C.convertArrays2File([m], 'm1.plt')
test.testA(m,1)

## TETRA static adaptation
n = C.getNCells(aTH4)
nodal_vals = numpy.empty((n,), dtype=I.E_NpyInt)
nodal_vals[:] = 2

m = XOR.adaptCells(aTH4, nodal_vals, sensor_type=3, smoothing_type=1)

m = XOR.closeCells(m[0])
#C.convertArrays2File([m], 'm2.plt')
test.testA(m,2)
