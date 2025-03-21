# - convertArrays2File (fmt_xfig) -
import Converter as C
import Generator as G

a = C.convertFile2Arrays('test.svg', 'fmt_svg',['density',100])
C.convertArrays2File(a, 'out.plt', 'bin_tp')
C.convertArrays2File(a, 'out.fig', 'fmt_xfig')

a = G.cart( (0,0,0), (1,1,1), (3, 3, 3) )
b = G.cart( (4,0,-2), (1,1,1), (3, 3, 1) )
c = G.cart( (0,-3,0),(1,1,1), (3,3,3) )
d = G.cart( (4,-3,-2),(1,1,1), (3,3,1) )
import Transform as T
a = T.rotate(a, (0,0,0), (1,1,0), 20.)
c = T.rotate(c, (0,-3,0), (1,1,0), 20.)
C.convertArrays2File([a,b,c,d], 'out1.fig', 'fmt_xfig')

b = C.convertArray2Tetra(b)
d = C.convertArray2Hexa(d)
C.convertArrays2File([a,b,c,d], 'out2.fig', 'fmt_xfig')

a = C.convertArray2Tetra(a)
c = C.convertArray2Hexa(c)
C.convertArrays2File([a,b,c,d], 'out3.fig', 'fmt_xfig')
