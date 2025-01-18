import unittest

from pypixcode import PixBuilder


class TestPixBuilder(unittest.TestCase):

    def test_success_get_code(self):
        # Arrange
        name = "Bruno Maciel Duarte"
        pix_key = "42fbd387-e918-48c7-abd9-13958bea32ce"
        value = "1.00"
        city = "Para De Minas"
        tx_id = "***"
        expected_crc = "76D3"  # CRC esperado para o payload fornecido

        # Cria uma instância do PixBuilder
        pix_builder = PixBuilder(name, pix_key, value, city, tx_id)

        # Act
        result = pix_builder.get_code()

        # Assert
        self.assertIn(name, result)
        self.assertIn(pix_key, result)
        self.assertIn(value, result)
        self.assertIn(city, result)
        self.assertIn(tx_id, result)
        self.assertTrue(result.endswith(expected_crc))  # Verifica se o CRC está correto
