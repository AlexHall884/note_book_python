from json_file import (read_file, write_file)
import user_interface as ui
import operations as op

def button_click():
    ui.greetings_user()
    while True:
        choice = ui.show_menu()
        if choice == 1:             # просмотр всех заметок
            notes = read_file()
            if not notes:
                ui.no_note_show()
            else:
                ui.show_list_note(notes)
        elif choice == 2:           # просмотр заметок по дате
            notes = read_file()
            result = op.filtr_note_by_date(notes)
            if not result:
                ui.no_note_error()
            else:
                ui.show_list_note(result)            
        elif choice == 3:           # поиск заметки
            notes = read_file()
            result = op.find_note(notes)
            if not result:
                ui.no_note_error()
            else:
                ui.show_note_info(result)
        elif choice == 4:           # добавить заметку
            notes = read_file()
            op.add_note(notes)
            ui.info()
            write_file(notes)
        elif choice == 5:           # удалить заметку
            notes = read_file()
            result = op.find_note(notes)
            if not result:
                ui.no_note_error()
            else:
                op.delete_note(notes, result)
                ui.info()
                write_file(notes)
        elif choice == 6:           # редактировать заметку
            notes = read_file()
            result = op.update(notes)
            if not result:
                ui.no_note_error()
            else:
                ui.info()
                write_file(notes)
        elif choice == 7:
            ui.farewell_user()
            break
        else:
            ui.no_index_search()


