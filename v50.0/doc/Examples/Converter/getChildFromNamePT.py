# - getChildFromName (pyTree) -
import Converter.Internal as Internal

z = Internal.newZone('Zone', zsize=[[10, 2, 0]], ztype='Structured')
print(Internal.getChildFromName(z, 'ZoneType'))
#>> ['ZoneType', array([b'S', b't', b'r', b'u', b'c', b't', b'u', b'r', ...]
