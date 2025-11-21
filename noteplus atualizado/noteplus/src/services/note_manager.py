from src.patterns.singleton import Singleton
from src.patterns.factory import NoteFactory
from src.patterns.strategy import ExportJSON, ExportMarkdown, ExportText
from src.patterns.observer import Subject, LoggerObserver

class NoteManager(Subject, metaclass=Singleton):

    def __init__(self):
        super().__init__()

        self.notes = []
        self.lists = {}

        self.attach(LoggerObserver())

        self.export_strategies = {
            "json": ExportJSON(),
            "md": ExportMarkdown(),
            "txt": ExportText()
        }

    def add_note(self, title, content):
        note = NoteFactory.create_note(title, content)
        self.notes.append(note)

        self.notify(f"Nota criada: {title}")

        return note

    def list_notes(self):
        return self.notes

    def remove_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                
                self.notify(f"Nota removida: {title}")
                return True
                
        return False

    def create_list(self, list_name):
        if list_name not in self.lists:
            self.lists[list_name] = []
            self.notify(f"Lista criada: {list_name}")

    def add_note_to_list(self, list_name, title, content):
        if list_name in self.lists:
            note = NoteFactory.create_note(title, content)
            self.lists[list_name].append(note)

            self.notify(f"Nota '{title}' adicionada à lista '{list_name}'")

    def list_notes_in_list(self, list_name):
        return self.lists.get(list_name, [])

    def remove_note_from_list(self, list_name, title):
        if list_name in self.lists:
            for n in self.lists[list_name]:
                if n.title == title:
                    self.lists[list_name].remove(n)
                    
                    self.notify(f"Nota '{title}' removida da lista '{list_name}'")
                    return True

        return False

    def export_note(self, title, formato):
        note = next((n for n in self.notes if n.title == title), None)

        if not note:
            for lista in self.lists.values():
                for n in lista:
                    if n.title == title:
                        note = n
                        break

        if not note:
            return False

        strategy = self.export_strategies.get(formato)

        if not strategy:
            print("Formato inválido.")
            return False

        self.notify(f"Nota '{title}' exportada como {formato.upper()}")
        strategy.export(note)

        return True
