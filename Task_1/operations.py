import user_interface as ui  

def find_note_by_id(notes: list, id: str) -> dict:
    '''
    Поиск по id
    '''
    for note in notes:
        if note['id'] == id:
            return note
    return None

def find_note_by_title_note(notes: list, title_note: str) -> dict:
    '''
    Поиск по title
    '''
    for note in notes:
        if note['title_note'] == title_note:
            return note
    return None

def filtr_note_by_date(notes: list) -> list:
    '''
    Выборка по дате
    '''
    list_data = []
    date = ui.check_data()
    for note in notes:
        if note['data_note'][0:10] == date:
            list_data.append(note)
    if not list_data: 
        return None 
    else: 
        return list_data
    
def add_note(notes: list):
    '''
    Добавление заметки
    '''
    note = ui.create_note()
    notes.append(note)
    

def delete_note(notes: list, note: dict):
    '''
    Удаление заметки
    '''
    notes.remove(note)
    
def update_note(note: dict):
    '''
    Изменение заметки
    '''
    flag = True
    while flag:
        idx = ui.get_changes()
        if idx == 1:
            flag = False
            note['title_note'] = ui.get_title_note()
            note['data_note'] = ui.get_data_note()  
        elif idx == 2:
            flag = False
            note['text_note'] = ui.get_text_note()
            note['data_note'] = ui.get_data_note()
        else:
            ui.no_index_search() 
            
def find_note(notes: list) -> list:
    '''
    Поиск заметки
    '''
    flag = True
    while flag:
        search_choice = ui.show_search_menu()
        if search_choice == 1:
            flag = False
            id = ui.get_search_id()
            result = find_note_by_id(notes, id)
            if result is not None:
                return result
            else:   
                return None
        elif search_choice == 2:
            flag = False
            title_note = ui.get_title_note()
            result = find_note_by_title_note(notes, title_note)
            if result is not None:
                return result
            else:
                return None
        else:
            ui.no_index_search()  
            

def update(notes: list):
    '''
    Редактирование
    '''
    flag = True
    while flag:
        search_choice = ui.show_search_menu()
        if search_choice == 1:
            flag = False
            id = ui.get_search_id()
            for note in notes:
                if note['id'] == id:
                    ui.update_note(note)
                    return note
            return None
        elif search_choice == 2:
            flag = False
            title_note = ui.get_title_note()
            for note in notes:
                if note['title_note'] == title_note:
                    ui.update_note(note)
                    return note
            return None        
        else:
            ui.no_index_search()      