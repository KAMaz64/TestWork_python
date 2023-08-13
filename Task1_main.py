# Основной класс для взаимодействия с пользователем

import csv
import os
from datetime import datetime

NOTES_FILE = "notes.csv"

class Note:
    def __init__(self, note_id, title, body, creation_date, last_modified):
        self.note_id = int(note_id)
        self.title = title
        self.body = body
        self.creation_date = creation_date
        self.last_modified = last_modified

class NoteManager:
    def __init__(self):
        self.notes = []
        self.load_notes()
        self.modified = False

    def load_notes(self):
        create_notes_file()
        with open(NOTES_FILE, "r", newline="") as file:
            reader = csv.reader(file, delimiter=";")
            next(reader)  # Пропустить заголовки столбцов
            for row in reader:
                note = Note(*row)
                self.notes.append(note)

    def save_notes(self):
        with open(NOTES_FILE, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["ID", "Title", "Body", "Creation Date", "Last Modified"])
            for note in self.notes:
                writer.writerow([note.note_id, note.title, note.body, note.creation_date, note.last_modified])
        self.modified = False

    def add_note(self, title, body):
        note_id = 1 if not self.notes else self.notes[-1].note_id + 1
        now = datetime.now()
        creation_date = now.strftime("%Y-%m-%d %H:%M:%S")
        last_modified = creation_date
        new_note = Note(note_id, title, body, creation_date, last_modified)
        self.notes.append(new_note)
        self.modified = True

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = new_title
                note.body = new_body
                note.last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.modified = True
                break

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.modified = True

    def view_notes_by_date(self, target_date):
        filtered_notes = [note for note in self.notes if note.creation_date[:10] == target_date.strftime("%Y-%m-%d")]
        self.display_notes(filtered_notes)

    def view_all_notes(self):
        self.display_notes(self.notes)

    def display_notes(self, notes_list):
        for note in notes_list:
            print(f"ID: {note.note_id}, Заголовок: {note.title}, Дата создания: {note.creation_date}")

    def view_full_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                print(f"ID: {note.note_id}, Заголовок: {note.title}")
                print(f"Текст: {note.body}")
                print(f"Дата создания: {note.creation_date}")
                print(f"Дата последнего изменения: {note.last_modified}")
                break

    def save_changes_prompt(self):
        while True:
            choice = input("Хотите ли вы сохранить внесенные изменения? (да/нет): ").lower()
            if choice == "да":
                self.save_notes()
                print("Изменения сохранены.")
                break
            elif choice == "нет":
                print("Изменения не сохранены.")
                self.load_notes()  # Откатываем изменения
                break
            else:
                print("Пожалуйста, введите 'да' или 'нет'.")

def create_notes_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["ID", "Title", "Body", "Creation Date", "Last Modified"])

def main():
    note_manager = NoteManager()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить новую заметку")
        print("2. Просмотреть список заметок по дате")
        print("3. Просмотреть список всех заметок")
        print("4. Посмотреть выбранную заметку полностью")
        print("5. Редактировать заметку")
        print("6. Удалить заметку")
        print("7. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note_manager.add_note(title, body)
        elif choice == "2":
            date_str = input("Введите дату (гггг-мм-дд), для просмотра заметок этой даты: ")
            try:
                target_date = datetime.strptime(date_str, "%Y-%m-%d")
                note_manager.view_notes_by_date(target_date)
            except ValueError:
                print("Некорректный формат даты. Введите дату в формате гггг-мм-дд.")
        elif choice == "3":
            note_manager.view_all_notes()
        elif choice == "4":
            note_id = int(input("Введите ID заметки, которую хотите просмотреть: "))
            note_manager.view_full_note(note_id)
        elif choice == "5":
            note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новый текст: ")
            note_manager.edit_note(note_id, new_title, new_body)
        elif choice == "6":
            note_id = int(input("Введите ID заметки, которую хотите удалить: "))
            note_manager.delete_note(note_id)
        elif choice == "7":
            if note_manager.modified:
                choice = input("Имеются несохраненные изменения. Хотите сохранить? (да/нет): ").lower()
                if choice == "да":
                    note_manager.save_notes()
            print("Программа завершена.")
            break
        else:
            print("Некорректный выбор. Введите номер действия снова.")

if __name__ == "__main__":
    main()
