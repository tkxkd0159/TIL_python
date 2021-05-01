## 이거 안해주면 import mypkg 만 했을 시 attribute error 뜸

# from . import shapes
# from mypkg.shapes import shapes3d, shapes2d
from .shapes.api import Circle, cube
from . import stats

print(f"Execute -> {__file__}")