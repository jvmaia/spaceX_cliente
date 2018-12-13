import requests
import json


class spaceXApi():
    def __init__(self):
        self.urlBase = 'https://api.spacexdata.com/v3/launches/'
        self.opcoes = {
            '1': ('Próximo Lançamento', 'next'),
            '2': ('Último lançamento', 'latest'),
            '3': ('Próximos lançamentos', 'upcoming'),
            '4': ('Lançamentos passados', 'past')
        }

    def run(self):
        print('O que você deseja visualizar?\n')
        for opcao in self.opcoes:
            print(f'{opcao} - {self.opcoes[opcao][0]}')
        print()
        opcao = None
        opcoes = ", ".join(self.opcoes.keys())
        while True:
            try:
                opcao = input('Insira uma opção: ')
                lancamentos = self.coletarLancamento(opcao)
                if not isinstance(lancamentos, list):
                    lancamentos = [lancamentos]
                break
            except KeyError:
                print(f'Opção "{opcao}" inválida, as opções disponíves são: {opcoes}')

        for lancamento in lancamentos:
            print('\nINFORMAÇÕES DO VOO')
            lancamentoFormatado = self.formatarInformacoes(lancamento)
            print(lancamentoFormatado)

            if len(lancamentos) > 1 and lancamento != lancamentos[-1]:
                proximo_lancamento = None
                while not proximo_lancamento in ['s', 'n']:
                    if not proximo_lancamento is None:
                        print('Opção inválida')
                    msg = 'Deseja as informações do próximo voo (s - sim || n - não)? '
                    proximo_lancamento = input(msg).lower()
                if proximo_lancamento == 's':
                    pass
                else:
                    break

    def coletarLancamento(self, opcao):
        url = self.urlBase + self.opcoes[opcao][1]
        r = json.loads(requests.get(url).content)
        return r

    def formatarInformacoes(self, voo):
        data, hora = voo['launch_date_utc'].split('T')
        hora = hora[0:5]
        mensagemFormatada = f'''
Número do Voo: {voo['flight_number']}
Missão: {voo['mission_name']}
Ano de lançamento: {voo['launch_year']}
Data de lançamento (UTC): {data} às {hora}
Detalhes: {voo['details']}
        '''
        return mensagemFormatada


if __name__ == '__main__':
    spaceXApi().run()
