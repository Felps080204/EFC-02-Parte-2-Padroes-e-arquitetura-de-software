class Note:
    def __init__(self, title, content, note_type="simple"):
        self.title = title
        self.content = content
        self.note_type = note_type

    def __str__(self):
        return f"[{self.note_type.upper()}] {self.title}: {self.content}"
