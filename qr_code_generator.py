
import pyqrcode
import png
from pyqrcode import QRCode



s = "https://github.com/faazzzz"

url = pyqrcode.create(s)



url.png('myqr.png', scale = 6)
