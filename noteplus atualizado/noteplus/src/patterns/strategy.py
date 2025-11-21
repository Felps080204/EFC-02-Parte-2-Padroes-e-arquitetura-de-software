import json

class ExportStrategy:
    def export(self, note):
        raise NotImplementedError


class ExportJSON(ExportStrategy):
    def export(self, note):
        data = {
            "title": note.title,
            "content": note.content,
            "type": note.note_type
        }
        filename = f"{note.title}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

class ExportMarkdown(ExportStrategy):
    def export(self, note):
        filename = f"{note.title}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {note.title}\n\n")
            f.write(f"{note.content}\n")
            f.write(f"\n*Tipo:* {note.note_type}\n")

class ExportText(ExportStrategy):
    def export(self, note):
        filename = f"{note.title}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Titulo: {note.title}\n")
            f.write(f"Conteúdo: {note.content}\n")
            f.write(f"Tipo: {note.note_type}\n")
