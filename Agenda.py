class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = False

    def marcar_favorito(self):
        self.favorito = not self.favorito

    def __str__(self):
        favorito_str = " (Favorito)" if self.favorito else ""
        return f"{self.nome} - {self.telefone} - {self.email}{favorito_str}"


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone, email):
        contato = Contato(nome, telefone, email)
        self.contatos.append(contato)
        print(f"Contato {nome} adicionado com sucesso.")

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato cadastrado.")
        else:
            print("Lista de Contatos:")
            for i, contato in enumerate(self.contatos):
                print(f"{i + 1}: {contato}")

    def editar_contato(self, indice, nome, telefone, email):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice].nome = nome
            self.contatos[indice].telefone = telefone
            self.contatos[indice].email = email
            print("Contato atualizado com sucesso.")
        else:
            print("Índice inválido.")

    def marcar_favorito(self, indice):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice].marcar_favorito()
            status = "marcado" if self.contatos[indice].favorito else "desmarcado"
            print(f"Contato {status} como favorito.")
        else:
            print("Índice inválido.")

    def listar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if not favoritos:
            print("Nenhum contato favorito.")
        else:
            print("Contatos Favoritos:")
            for contato in favoritos:
                print(contato)

    def deletar_contato(self, indice):
        if 0 <= indice < len(self.contatos):
            removido = self.contatos.pop(indice)
            print(f"Contato {removido.nome} removido com sucesso.")
        else:
            print("Índice inválido.")


def main():
    agenda = Agenda()

    while True:
        print("\nEscolha uma opção:")
        print("1: Adicionar Contato")
        print("2: Listar Contatos")
        print("3: Editar Contato")
        print("4: Marcar/Desmarcar Favorito")
        print("5: Listar Contatos Favoritos")
        print("6: Deletar Contato")
        print("0: Sair")

        opcao = input("Digite sua escolha: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            agenda.adicionar_contato(nome, telefone, email)

        elif opcao == "2":
            agenda.listar_contatos()

        elif opcao == "3":
            agenda.listar_contatos()
            indice = int(input("Digite o índice do contato que deseja editar: ")) - 1
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Novo email: ")
            agenda.editar_contato(indice, nome, telefone, email)

        elif opcao == "4":
            agenda.listar_contatos()
            indice = int(input("Digite o índice do contato que deseja marcar/desmarcar como favorito: ")) - 1
            agenda.marcar_favorito(indice)

        elif opcao == "5":
            agenda.listar_favoritos()

        elif opcao == "6":
            agenda.listar_contatos()
            indice = int(input("Digite o índice do contato que deseja deletar: ")) - 1
            agenda.deletar_contato(indice)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()