import crcmod


class Calculator:

    @staticmethod
    def crc16(value: str) -> str:
        crc16_func = crcmod.mkCrcFun(poly=0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
        crc_result = crc16_func(value.encode("utf-8"))

        return f"{crc_result:04X}"
