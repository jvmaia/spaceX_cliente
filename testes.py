import json
import unittest
import requests
from main import spaceXApi


class Testes(unittest.TestCase):
    def setUp(self):
        self.urls = {
            1: ('Próximo Lançamento', 'next'),
            2: ('Último lançamento', 'latest'),
            3: ('Próximos lançamentos', 'upcoming'),
            4: ('Lançamentos passados', 'past')
        }
        self.api = spaceXApi()

    def testeColetarLancamentos(self):
        for i in range(1, 5):
            resultadoApi = self.api.coletarLancamento(str(i))
            url = 'https://api.spacexdata.com/v3/launches/' + self.urls[i][1]
            resultadoEsperado = json.loads(requests.get(url).content)
            self.assertEqual(
                resultadoApi,
                resultadoEsperado,
                f'Deveria(m) ser o(s) {self.urls[i][0].lower()} obtido(s) por meio da url: {url}'
            )


if __name__ == '__main__':
    unittest.main()
