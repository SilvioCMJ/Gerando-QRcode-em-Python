from pyqrcode import QRCode
import png

QRString = "http://www.exemplo.com"
#criando qr
url = pyqrcide.create(QRString)

#salvando o qr code
url.png(r'qr.png',scale=8)
