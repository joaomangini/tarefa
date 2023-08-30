def main():
    tarefas = []

    while True:
        print("1 - Adicionar tarefa")
        print("2 - Ver tarefas")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tarefa = input("Digite a nova tarefa: ")
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")
        elif escolha == "2":
            print("Lista de tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()