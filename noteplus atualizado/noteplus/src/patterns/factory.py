from src.models.note import Note

class NoteFactory:
    @staticmethod
    def create_note(title, content, note_type="simple"):
        return Note(title, content, note_type)
