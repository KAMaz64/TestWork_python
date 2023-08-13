# Класс для представления заметок

class Note:
    def __init__(self, note_id, title, body, creation_date, last_modified):
        self.note_id = int(note_id)
        self.title = title
        self.body = body
        self.creation_date = creation_date
        self.last_modified = last_modified