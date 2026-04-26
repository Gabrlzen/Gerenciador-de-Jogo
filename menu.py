# Importação dos módulos necessários
import json
import missao
import jogador

# FUNÇÕES DE SALVAMENTO E CARREGAMENTO
def salvar_missoes(missoes):
    dados = []

    for m in missoes:
        if isinstance(m, missao.MissaoCombate):
            tipo = 'combate'
            extra = {'inimigo': m.inimigo}
        elif isinstance(m, missao.MissaoExploracao):
            tipo = 'exploracao'
            extra = {'local': m.local}
        else:
            tipo = 'normal'
            extra = {}
        
        dados.append({
            'nome': m.nome,
            'tipo': tipo,
            'concluida': m.concluida,
            **extra
        })
    
    with open('missoes.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)


def carregar_missoes():
    try:
        with open('missoes.json', 'r') as arquivo:
            dados = json.load(arquivo)
        
        missoes = []

        for d in dados:
            if d['tipo'] == 'combate':
                m = missao.MissaoCombate(
                    nome = d['nome'],
                    inimigo = d['inimigo']
                )
            elif d['tipo'] == 'exploracao':
                m = missao.MissaoExploracao(
                    nome = d['nome'],
                    local = d['local']
                )
            else:
                m = missao.Missao(nome = d['nome'])
            
            m.concluida = d['concluida']
            missoes.append(m)
        
        return missoes

    except FileNotFoundError:
        return []


# FUNÇÃO PRINCIPAL DO MENU
def main():
    # Carrega as missões salvas, ou cria as padrões se o arquivo não existir
    missoes = carregar_missoes()
    
    # Se não houver missões salvas, cria as três padrões
    if not missoes:
        # Inicializa a lista de missões com três missões padrão
        # Contém: uma missão básica, uma missão de combate e uma de exploração
        missoes = [missao.Missao(nome = 'Recuperar o item perdido'),
                   missao.MissaoCombate(nome = 'Derrotar o dragão', inimigo = 'Dragão Vermelho'),
                   missao.MissaoExploracao(nome = 'Explorar a caverna misteriosa', local = 'Caverna do Eco')]
    
    # Loop principal do menu - continua até que o usuário escolha sair
    while True:
        # Exibe as opções disponíveis ao usuário
        print('[ 1 ] - Listar missões')
        print('[ 2 ] - Concluir missão')
        print('[ 3 ] - Criar missão')
        print('[ 0 ] - Sair')

        # Captura e valida a entrada do usuário
        escolha = input('Escolha uma opção: ')
        try:
            escolha = int(escolha)
        except ValueError:
            print('Opção inválida. Tente novamente.')
            continue
        
        # OPÇÃO 1: Listar todas as missões disponíveis
        if escolha == 1:
            # Exibe uma seção formatada com o título centrado
            print('-' * 30)
            print('Missões disponíveis'.center(30))
            print('-' * 30)
            print('~' * 75)
            # Itera sobre todas as missões e as exibe
            for m in missoes:
                print(m)
            print('~' * 75)

        # OPÇÃO 2: Concluir uma missão selecionada
        elif escolha == 2:
            # Exibe as missões disponíveis com números para seleção
            print("Missões disponíveis:")
            for i, m in enumerate(missoes, start=1):
                print(f"{i} - {m}")

            # Loop para obter um índice válido da missão a concluir
            while True:
                try:
                    indice = int(input("Qual missão deseja concluir? "))

                    # Valida se o índice está dentro do intervalo de missões
                    if 1 <= indice <= len(missoes):
                        break
                    else:
                        print("Índice inválido. Tente novamente.")

                except ValueError:
                    print("Digite um número válido.")

            # Obtém a missão selecionada e marca como concluída
            mission = missoes[indice - 1]
            mission.concluir()
            salvar_missoes(missoes)

            # Exibe mensagem de conclusão com recompensa
            print(f'Missão "{mission.nome}" concluída! Recompensa: {mission.obter_recompensa()} pontos.')
            
            # Salva as missões após concluir uma
            salvar_missoes(missoes)
        
        # OPÇÃO 3: Criar uma nova missão
        elif escolha == 3:
            # Loop para obter um tipo de missão válido (combate ou exploração)
            while True:
                try:
                    tipo_missao = input('Deseja criar uma missão de combate ou exploração? ').lower().strip()

                    # Valida o tipo de missão inserido
                    if tipo_missao in ['combate', 'exploracao', 'exploração']:
                        print(f'Tipo de missão: {tipo_missao.capitalize()}')
                        break
                    else:
                        print('Tipo de missão inválido. Tente novamente.')

                except KeyboardInterrupt:
                    print('\nOperação cancelada pelo usuário. Retornando ao menu principal.')
                    continue
            
            # Cria uma missão de combate se o tipo escolhido for "combate"
            if tipo_missao == 'combate':
                # Obtém o nome da missão de combate e valida se não está vazio
                nome_missao = input('Digite o nome da missão de combate: ')
                if nome_missao.strip() == '':
                    print('O nome da missão não pode ser vazio. Operação cancelada.')
                    continue

                # Obtém o nome do inimigo e valida se não está vazio
                inimigo_missao = input('Digite o nome do inimigo da missão de combate: ')
                if inimigo_missao.strip() == '':
                    print('O nome do inimigo não pode ser vazio. Operação cancelada.')
                    continue

                # Cria a nova missão de combate e adiciona à lista
                nova_missao_combate = missao.MissaoCombate(nome = nome_missao, inimigo = inimigo_missao)
                missoes.append(nova_missao_combate)
                salvar_missoes(missoes)
            
            # Cria uma missão de exploração se o tipo escolhido for "exploração"
            elif tipo_missao in ['exploracao', 'exploração']:
                # Obtém o nome da missão de exploração e valida se não está vazio
                nome_missao = input('Digite o nome da missão de exploração: ')
                if nome_missao.strip() == '':
                    print('O nome da missão não pode ser vazio. Operação cancelada.')
                    continue

                # Obtém o local da exploração e valida se não está vazio
                local_missao = input('Digite o nome do local da missão de exploração: ')
                if local_missao.strip() == '':
                    print('O nome do local não pode ser vazio. Operação cancelada.')
                    continue

                # Cria a nova missão de exploração e adiciona à lista
                nova_missao_exploracao = missao.MissaoExploracao(nome = nome_missao, local = local_missao)
                missoes.append(nova_missao_exploracao)
                salvar_missoes(missoes)

        
        # OPÇÃO 0: Sair do programa
        elif escolha == 0:
            # Salva as missões antes de encerrar
            salvar_missoes(missoes)
            # Exibe mensagem de encerramento formatada
            print('-' * 30)
            print('Programa encerrado'.center(30))
            print('-' * 30)
            # Sai do loop principal
            break

        # Tratamento para opções inválidas
        else:
            print('Opção inválida. Tente novamente.')

# Executa a função principal
main()
