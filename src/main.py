# main.py
from biblioteca import Biblioteca, Livro, Usuario


def main():
    biblioteca = Biblioteca()

    while True:
        print("\n--- Sistema de Biblioteca ---")
        print("1. Adicionar livro")
        print("2. Adicionar usuário")
        print("3. Emprestar livro")
        print("4. Devolver livro")
        print("5. Listar livros")
        print("6. Listar usuários")
        print("7. Sair")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            adicionar_livro(biblioteca)
        elif escolha == "2":
            adicionar_usuario(biblioteca)
        elif escolha == "3":
            emprestar_livro(biblioteca)
        elif escolha == "4":
            devolver_livro(biblioteca)
        elif escolha == "5":
            listar_livros(biblioteca)
        elif escolha == "6":
            listar_usuarios(biblioteca)
        elif escolha == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def adicionar_livro(biblioteca: Biblioteca):
    print("\n--- Adicionar Livro ---")
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()

    try:
        livro = Livro(titulo, autor)
        biblioteca.adicionar_livro(livro)
        print(f"✅ Livro '{titulo}' adicionado com sucesso!")
    except ValueError as e:
        print(f"❌ Erro: {e}")


def adicionar_usuario(biblioteca: Biblioteca):
    print("\n--- Adicionar Usuário ---")
    nome = input("Nome do usuário: ").strip()

    try:
        usuario = Usuario(nome)
        biblioteca.adicionar_usuario(usuario)
        print(f"✅ Usuário '{nome}' cadastrado com sucesso!")
    except ValueError as e:
        print(f"❌ Erro: {e}")


def emprestar_livro(biblioteca: Biblioteca):
    print("\n--- Empréstimo de Livro ---")
    usuario = input("Nome do usuário: ").strip()
    livro = input("Título do livro: ").strip()

    try:
        biblioteca.emprestar_livro(usuario, livro)
        print(f"✅ Livro '{livro}' emprestado para {usuario}!")
    except ValueError as e:
        print(f"❌ Erro: {e}")


def devolver_livro(biblioteca: Biblioteca):
    print("\n--- Devolução de Livro ---")
    usuario = input("Nome do usuário: ").strip()
    livro = input("Título do livro: ").strip()

    try:
        biblioteca.devolver_livro(usuario, livro)
        print(f"✅ Livro '{livro}' devolvido por {usuario}!")
    except ValueError as e:
        print(f"❌ Erro: {e}")


def listar_livros(biblioteca: Biblioteca):
    print("\n--- Acervo de Livros ---")
    if not biblioteca.livros:
        print("Nenhum livro cadastrado")
        return

    for i, livro in enumerate(biblioteca.livros, 1):
        status = "Emprestado" if livro.emprestado else "Disponivel"
        print(f"{i}. {livro.titulo} ({livro.autor}) - {status}")


def listar_usuarios(biblioteca: Biblioteca):
    print("\n--- Usuários Cadastrados ---")
    if not biblioteca.usuarios:
        print("Nenhum usuário cadastrado")
        return

    for i, usuario in enumerate(biblioteca.usuarios, 1):
        print(f"\n{i}. {usuario.nome}")
        if usuario.livros_emprestados:
            print(f"   Livros emprestados ({len(usuario.livros_emprestados)}/3):")
            for livro in usuario.livros_emprestados:
                print(f"   - {livro.titulo}")
        else:
            print("   Nenhum livro emprestado")


if __name__ == "__main__":
    main()