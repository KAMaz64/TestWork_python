# Основная часть приложения для взаимодействия с пользователем

from datetime import datetime

from NoteManager import NoteManager


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
