import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.services.note_manager import NoteManager

manager = NoteManager()

def menu():
    while True:
        print("\n--- Bem vindo ao NotesPlus! ")
        print("--- Organize aqui sua rotina através de tarefas e listas!")
        print("1 - Adicione uma tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Crie uma lista de tarefas")
        print("5 - Visualize suas listas de tarefas")
        print("6 - Adicione uma tarefa em alguma lista")
        print("7 - Veja as tarefas de uma lista")
        print("8 - Remova tarefas de uma lista")
        print("9 - Exportar uma tarefa")
        print("0 - Sair do NotePlus")

        op = input("Digite a sua escolha: ")

        if op == "1":
            title = input("Título: ")
            content = input("Conteúdo: ")
            manager.add_note(title, content)

        elif op == "2":
            notes = manager.list_notes()
            for n in notes:
                print(n)

        elif op == "3":
            title = input("Título da nota a remover: ")
            if not manager.remove_note(title):
                print("Nota não encontrada.")

        elif op == "4":
            name = input("Nome da lista: ")
            manager.create_list(name)

        elif op == "5":
            for list_name in manager.lists:
                print(f"- {list_name}")

        elif op == "6":
            list_name = input("Nome da lista: ")
            title = input("Título da nota: ")
            content = input("Conteúdo: ")
            manager.add_note_to_list(list_name, title, content)

        elif op == "7":
            list_name = input("Lista: ")
            notes = manager.list_notes_in_list(list_name)
            for n in notes:
                print(n)

        elif op == "8":
            list_name = input("Lista: ")
            title = input("Nota: ")
            manager.remove_note_from_list(list_name, title)

        elif op == "9":
            title = input("Título da tarefa para exportar: ")
            print("Formatos disponíveis: json, md, txt")
            formato = input("Formato desejado: ")

            if manager.export_note(title, formato):
                print("Tarefa exportada com sucesso!")
            else:
                print("Não foi possível exportar a tarefa.")

        elif op == "0":
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
