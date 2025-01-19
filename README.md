

Este projeto é uma biblioteca Python para gerar codigo e qrcode do Pix. Ele fornece uma interface simples e intuitiva para criar, modificar e validar dados de Pix.

## Instalação

Para instalar o projeto, use o pip:

```bash
pip install pypixcode
```

## Uso
Exemplo de como gerar um código Pix:

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

# result str:  00020126580014BR.GOV.BCB.PIX013642fbd387-e918-48c7-abd9-13958bea32ce52040000530398654041.005802BR5913Fulano De Tau6013Para De Minas62070503***63045039
```

Exemplo de como gerar um QR em base64 do código Pix:

```python
from pypixcode import PixBuilder

name = "Fulano De Tau"
pix_key = "42fbd387-e918-48c7-abd9-13958bea32ce"
value = "1.00"
city = "Para De Minas"
tx_id = "***"

# Cria uma instância do PixBuilder
pix_builder = PixBuilder(name, pix_key, value, city, tx_id)

code = pix_builder.get_qrcode()
# result base64 image: iVBORw0KGgoAAAANSUhEUgAAAQkAAAEJAQAAAACvE+/JAAACuklEQVR42u1ZMY6rUBCbfApKjsBNyMWQiMTFkptwBEoKxKztednVr7b78peSYvVEXuGdeDz2EPnb5xGfK58rplf2iLhlbhHDmvkcMvsXvuqfeN7jyp/49fPPrhDukvnauzym4QS+fR6Pe65bCrMh3DlQzscYAnmhunHfO8DdY3SFC3wsLGgBbqDOufXOcPMcD3IXTzpyI8IW7lL4QIYT+MiDK/jMlLtUBjQYyvnXH1NlqM8Z0AMpQxDpTB6U1vlVt1USNSV3t+MGWsQ0QCgM4b5FQWNC3AVtt/6iPHgqA3/9FD6c0HT7skEoHqNjdRdUMogZ+A4gTckwvpsd4XKWsaaQL8zfG9AngQP9atlq+PUnCC18zprospU8WEnb01LIMNAIsjSCtMg25CyFDEUMmbFLvQVv1stFqgcth3ApA/EVGSZy9zLlbozCHGJsOXOeTHUXkSKKp7tGGwzkHf/C4SpktAscbeLuJY2gmnEmW+puc7nUXXkGBratnrl6hqUkV3432slSGVDdCj+srjJEtpMlGarBFgZ3pQkw4pbtZEmGlJ358bvJpnPlLoX2wklOAfK1tBUDMFtOtY7uBt6RPqe5SPL5GlzDDxxZtzWzs0t3tYg6LXX3UcuQd9PNITNGSfPUXaEaOYnJ3Y57vXUrl2bZapwQKaFlemdqKx54ChkriUk8yYeFFHjlaLOsbm1xKr2PxVhlNVPu0uLcU348S3dBi8VWdzkSvj0Dg0Qc03u0eQqZRgJpm33LQl0eZSEs1yKvprvNKTBalnsw3UDK3SicyfkyDrsmYSkDeZBa8WuqnaF+S9PtOQ3u9b1deL2rm66vUqhcldVU03N05W7BxUmLBU01JmGmd9/qKgkjpj3LLsjvnr5vfvS+B0LGTbSSMDywa7SsPUglIHL3Wd5xtdXdz6v9z5X/7coXs9mf7/Qucv8AAAAASUVORK5CYII=

```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Faça um push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo `LICENSE` para mais detalhes.
