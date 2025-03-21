# - usurp (pyTree)-
import Post.PyTree as P
import Converter.PyTree as C
import Generator.PyTree as G
import Transform.PyTree as T
import KCore.test as test

# Creation des cylindres
a1 = G.cylinder((0,0,0), 0, 2, 360, 0, 1., (100,2,10))
a1 = T.subzone(a1, (1,2,1), (100,2,10)); a1[0]='cyl1'
a1 = C.addBC2Zone(a1,'overlap','BCOverlap','imin')
a1 = C.fillEmptyBCWith(a1, 'nref','BCFarfield')
a2 = G.cylinder((0,0,0), 0, 2, 90, 0, 0.5, (10,2,10))
a2 = T.translate(a2, (0,0,0.2))
a2 = T.subzone(a2, (1,2,1),(10,2,10)); a2[0]='cyl2'

# creation des celln
C._addVars(a1,'Density')
C._initVars(a1, 'centers:cellN',1.)
C._initVars(a2, 'centers:cellN',1.)
t = C.newPyTree(['Base',2])
t[2][1][2] += [a1, a2]
t[2][1] = C.addState(t[2][1], 'Mach', 0.6)
try:
    t = P.usurp(t)
    test.testT(t[2][1][2][0])
except: pass
