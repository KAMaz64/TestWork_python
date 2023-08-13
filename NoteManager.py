import csv
import os
from datetime import datetime

from Note import Note


class NoteManager:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        create_notes_file()
        with open(NOTES_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                note = Note(*row)
                self.notes.append(note)

    def save_notes(self):
        with open(NOTES_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            for note in self.notes:
                writer.writerow([note.note_id, note.title, note.body, note.creation_date, note.last_modified])

    def add_note(self, title, body):
        now = datetime.now()
        creation_date = now.strftime("%Y-%m-%d %H:%M:%S")
        last_modified = creation_date
        note_id = len(self.notes) + 1
        new_note = Note(note_id, title, body, creation_date, last_modified)
        self.notes.append(new_note)
        self.save_notes()

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = new_title
                note.body = new_body
                note.last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                break

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes()

    def view_notes_by_date(self, target_date):
        for note in self.notes:
            note_date = datetime.strptime(note.creation_date, "%Y-%m-%d %H:%M:%S")
            if note_date.date() == target_date.date():
                print(f"ID: {note.note_id}, Заголовок: {note.title}, Дата создания: {note.creation_date}")

    def view_all_notes(self):
        for note in self.notes:
            print(f"ID: {note.note_id}, Заголовок: {note.title}, Дата создания: {note.creation_date}")

def create_notes_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Title", "Body", "Creation Date", "Last Modified"])

NOTES_FILE = "notes.csv"