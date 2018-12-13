# spaceX_cliente
CLI para consultar informações dos voos da SpaceX

Bibliotecas utilizadas:
- json
- unittest
- requests

Optei por utilizar essas bibliotecas por ter contato diário com elas, serem de fácil manipulação e apresentarem todas as ferramentas que eu precisava,
como o `json.loads(...)` para desserializar o conteúdo recebido por meio da api da SpaceX.

Usei as chamadas f-strings por apresentarem uma facilidade e legibilidade maior que as strings com .format (`'{}'.format(...)`) das versões até a 3.6.

O último trecho do código garante que quando o script for chamado diretamente (`python main.py`) o método `spaceXApi.run()` seja executado e não quando for chamado pelo script de testes
