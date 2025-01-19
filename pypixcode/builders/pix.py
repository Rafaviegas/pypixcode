from commons.qr_code import QrCode
from pypixcode.commons import Calculator


class PixBuilder:
    """
        Gera o payload Pix para QR Code.

        Args:
            name (str): Nome do recebedor.
            pix_key (str): Chave Pix no formato UUID ou CPF.
            value (str): Valor da transação (utilizar ponto como separador decimal).
            city (str): Cidade do recebedor.
            tx_id (str): Identificador da transação.
            directory (str): Caminho para salvar o QR Code gerado (padrão: ~/).
    """

    def __init__(self, name, pix_key, value, city, tx_id, directory="~/"):
        self.__name = name
        self.__pix_key = pix_key
        self.__value = value
        self.__city = city
        self.__tx_id = tx_id
        self.__directory = directory

    def get_code(self) -> str:
        value_formatted = f"{float(self.__value):.2f}"

        payload_segments = [
            ("00", "01"),  # Formato do payload
            ("26", f"0014BR.GOV.BCB.PIX01{len(self.__pix_key):02d}{self.__pix_key}"),
            ("52", "0000"),  # Categoria do negócio
            ("53", "986"),  # Moeda (BRL)
            ("54", value_formatted),  # Valor
            ("58", "BR"),  # País
            ("59", self.__name),  # Nome do recebedor (limite de 25 caracteres)
            ("60", self.__city),  # Cidade (limite de 15 caracteres)
            ("62", f"05{len(self.__tx_id):02d}{self.__tx_id}"),  # Dados adicionais
        ]

        payload = "".join(f"{id}{len(value):02d}{value}" for id, value in payload_segments)
        payload += "6304"

        payload += Calculator.crc16(payload)

        return payload

    def get_qrcode(self) -> str:
        pix_code = self.get_code()

        return QrCode.generate(pix_code)
