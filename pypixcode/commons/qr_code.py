import segno
import base64
from io import BytesIO


class QrCode:

    @staticmethod
    def generate(value: str):
        qr = segno.make(value)

        buffer = BytesIO()
        qr.save(buffer, kind="png", scale=5)
        buffer.seek(0)

        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return img_base64
