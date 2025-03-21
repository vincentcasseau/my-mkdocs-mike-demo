# - boolean union (pyTree) -
import Intersector.PyTree as XOR
import Generator.PyTree as G
import Converter.PyTree as C
import Geom.PyTree as D
import KCore.test as test

s1 = D.sphere((0,0,0), 1, N=20)
s2 = D.sphere((0.,1.,0.), 1, N=30)

s1 = C.convertArray2Tetra(s1); s1 = G.close(s1)
s2 = C.convertArray2Tetra(s2); s2 = G.close(s2)

x = XOR.booleanUnion(s1, s2, tol=0.)
test.testT(x)
