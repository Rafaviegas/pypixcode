

Este projeto é uma biblioteca Python para gerar codigo e qrcode do Pix. Ele fornece uma interface simples e intuitiva para criar, modificar e validar dados de Pix.

## Instalação

Para instalar o projeto, use o pip:

```bash
pip install nome-do-projeto
```

## Uso
Exemplo de como usar o projeto:

```python
from pypixcode import PixBuilder

name = "Fulano De Tau"
pix_key = "42fbd387-e918-48c7-abd9-13958bea32ce"
value = "1.00"
city = "Para De Minas"
tx_id = "***"

# Cria uma instância do PixBuilder
pix_builder = PixBuilder(name, pix_key, value, city, tx_id)

code = pix_builder.get_code()

# result  00020126580014BR.GOV.BCB.PIX013642fbd387-e918-48c7-abd9-13958bea32ce52040000530398654041.005802BR5913Fulano De Tau6013Para De Minas62070503***63045039
```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Faça um push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE` para mais detalhes.
