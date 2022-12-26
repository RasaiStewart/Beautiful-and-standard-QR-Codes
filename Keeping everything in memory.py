import segno

beatle = segno.make('Rasai Stewart')
beatle = qrcode.to_pil()

import segno
import io

beatle = segno.make('Paul McCartney')
buff = io.BytesIO()
beatle.save(buff, kind='svg')