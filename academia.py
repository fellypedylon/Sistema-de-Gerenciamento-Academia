import os

FICHAS = []

def limpar(texto):
    """Limpa e exibe o título."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\n{texto}\n' + "=" * len(texto))

def aguardar_enter():
    """Pausa a execução e aguarda o usuário pressionar Enter."""
    input('\nPressione ENTER para continuar...')

def cadastrar():
    """Cadastra nova ficha."""
    limpar('CADASTRO DE FICHA')
    aluno = input('Nome do Aluno: ').title()
    objetivo = input('Objetivo: ').title()
    data_inicio = input('Data de Início (ex: DD/MM/AAAA): ')
    
    treino = []
    print('\n-- EXERCÍCIOS (digite SAIR para finalizar) --')
    while True:
        exercicio_nome = input('Exercício (ou "SAIR"): ').title()
        if exercicio_nome == 'Sair':
            break
        series = input('Séries: ')
        repeticoes = input('Repetições: ')
        
        treino.append({'nome': exercicio_nome, 'series': series, 'repeticoes': repeticoes})
        
        print(f'-> {exercicio_nome} adicionado.')
        
    FICHAS.append({'aluno': aluno, 'objetivo': objetivo, 'data_inicio': data_inicio, 'treino': treino})
    print(f'\nFicha de {aluno} cadastrada.')
    aguardar_enter()

def consultar():
    """Consulta ficha por nome."""
    limpar('CONSULTAR FICHA')
    busca = input('Nome do aluno para consulta: ').title()

    for ficha in FICHAS:
        if busca == ficha['aluno']:
            print('\n--- FICHA ENCONTRADA ---')
            print(f"Aluno: {ficha['aluno']} | Objetivo: {ficha['objetivo']} | Início: {ficha['data_inicio']}")
            print("\nDetalhes do Treino:")
            
            for exercicio in ficha['treino']:
                print(f"- {exercicio['nome'].ljust(20)} | {exercicio['series']} Séries | {exercicio['repeticoes']} Reps")
            aguardar_enter()
            return
    
    print(f'ERRO: Aluno "{busca}" não encontrado.')
    aguardar_enter()

def listar():
    """Lista todas as fichas."""
    limpar('LISTA DE TODOS OS TREINOS')
    
    if not FICHAS:
        print('Nenhuma ficha cadastrada.')
        aguardar_enter()
        return

    print("ALUNO | OBJETIVO | INÍCIO | RESUMO")
    print("-" * 80)

    for ficha in FICHAS:
        
        resumo_exercicios = []
        for ex in ficha['treino']:
            texto_exercicio = f"{ex['nome']} ({ex['series']}x{ex['repeticoes']})"
            resumo_exercicios.append(texto_exercicio)
        
        
        resumo = ', '.join(resumo_exercicios)
        print(f"{ficha['aluno'].ljust(15)} | {ficha['objetivo'].ljust(10)} | {ficha['data_inicio']} | {resumo}")

    aguardar_enter()

def sair():
    """Encerra o programa."""
    limpar('Obrigado por usar o sistema! Até a próxima.')



def main():
    opcoes = {
        '1': cadastrar,
        '2': consultar,
        '3': listar,
    }

    while True:
        limpar('CORPO EM MOVIMENTO | GESTÃO DE TREINOS')
        print('1. Cadastrar nova ficha')
        print('2. Consultar ficha por nome')
        print('3. Listar todos os treinos')
        print('4. Sair\n')
        opcao = input('Escolha uma opção: ').strip()

        funcao_escolhida = opcoes.get(opcao)

        if opcao == '4':
            sair()
            break
        elif funcao_escolhida:
            funcao_escolhida()
        else:
            print('Opção inválida.')
            aguardar_enter()


    main()