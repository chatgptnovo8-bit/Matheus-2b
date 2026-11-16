# Lista de alunos cadastrados
alunos = []


def cadastrar_aluno():
    print("\n--- Cadastrar aluno ---")

    while True:
        nome = input("Nome: ").strip()

        if not nome:
            print("Digite um nome.")
            continue

        try:
            nota = float(input("Nota: ").replace(",", "."))
        except ValueError:
            print("Nota inválida. Digite um número.")
            continue

        # Cada aluno é guardado em um dicionário
        alunos.append({"nome": nome, "nota": nota})

        if nota >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Recuperação"

        print(f"\n{nome} cadastrado com sucesso!")
        print(f"Nota: {nota}")
        print(f"Situação: {situacao}")

        continuar = input("\nCadastrar outro aluno? (s/n): ").lower()

        if continuar == "s":
            continue
        else:
            break


def listar_alunos():
    print("\n--- Lista de alunos ---")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for numero, aluno in enumerate(alunos, start=1):
        if aluno["nota"] >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Recuperação"

        print(f"\n{numero}. Nome: {aluno['nome']}")
        print(f"   Nota: {aluno['nota']}")
        print(f"   Situação: {situacao}")


def pesquisar_aluno():
    print("\n--- Pesquisar aluno ---")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    nome = input("Digite o nome ou parte do nome: ").lower()
    encontrou = False

    for aluno in alunos:
        if nome in aluno["nome"].lower():
            print(f"\nNome: {aluno['nome']}")
            print(f"Nota: {aluno['nota']}")
            encontrou = True

    if not encontrou:
        print("Aluno não encontrado.")


def calcular_media():
    print("\n--- Média da turma ---")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    soma = 0

    for aluno in alunos:
        soma += aluno["nota"]

    media = soma / len(alunos)
    print(f"Média da turma: {media:.2f}")


def contar_aprovados():
    print("\n--- Alunos aprovados ---")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    aprovados = 0

    for aluno in alunos:
        if aluno["nota"] >= 7:
            aprovados += 1

    print(f"Quantidade de aprovados: {aprovados}")


def mostrar_quantidade_alunos():
    print(f"\nQuantidade de alunos cadastrados: {len(alunos)}")


def principal():
    while True:
        print("\n===== SISTEMA DE CADASTRO DE ALUNOS =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Pesquisar aluno")
        print("4 - Calcular média da turma")
        print("5 - Sair")
        print("6 - Quantidade de alunos cadastrados")
        print("7 - Quantidade de alunos aprovados")
        print("==========================================")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um número de 1 a 7.")
            continue

        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            listar_alunos()
        elif opcao == 3:
            pesquisar_aluno()
        elif opcao == 4:
            calcular_media()
        elif opcao == 5:
            print("Sistema encerrado.")
            break
        elif opcao == 6:
            mostrar_quantidade_alunos()
        elif opcao == 7:
            contar_aprovados()
        else:
            print("Opção inválida. Digite um número de 1 a 7.")


if __name__ == "__main__":
    principal()
