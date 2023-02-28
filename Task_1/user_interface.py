import time
import uuid
from datetime import datetime
from colorama import Fore, Back, Style 

def greetings_user():
    '''
    Приветсвует пользователя
    
    '''
    print(f'{Fore.YELLOW + Style.BRIGHT}Добро пожаловать в Notebook. 📙 {Style.RESET_ALL}')
    

def farewell_user():
    '''
    Прощание с пользователем
    
    '''
    print(f'{Fore.YELLOW + Style.BRIGHT}До новых встреч 👋{Style.RESET_ALL}')

def show_menu()-> int:
    '''
    Выводит основное меню
    
    '''
    print('\n' + ('-' + 'o' + '-') * 10)
    print ('\n'
      f'{Fore.YELLOW + Style.BRIGHT}Выберите нужное действие: ↓{Style.RESET_ALL}\n'
      f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}' 
      ' 1 -👀 <Прсмотреть все заметки> \n'
      ' 2 -📅 <Просмотр заметок по дате> \n'
      ' 3 -🔎 <Найти заметку> \n'
      ' 4 -📝 <Добавить заметку>\n'
      ' 5 -🚮 <Удалить заметку \n'
      ' 6 -💾 <Редактировать заметку>\n'
      ' 7 -👋 <Выход> \n')
      
    return int(input(f' ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}'))

def show_search_menu() -> int:
    '''
    Выводит меню поиска заметки
    
    '''
    print('\n' + ('-' + 'o' + '-') * 10)
    print ('\n'
      f'{Fore.YELLOW + Style.BRIGHT}Выберите нужное действие: ↓{Style.RESET_ALL}\n'
      f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}' 
      ' 1 -🔎 <Поиск заметки по id> \n'
      ' 2 -📝 <Поиск заметки по заголовку> \n')
    
    return int(input(f' ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}'))

def show_update_menu()-> int:
    '''
    Выводит меню изменения заметки
    
    '''
    print('\n' + ('-' + 'o' + '-') * 10)
    print ('\n'
      f'{Fore.YELLOW + Style.BRIGHT}Выберите нужное действие: ↓{Style.RESET_ALL}\n'
      f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}' 
      ' 1 -🔎 <Обновить заметку по идентификатору> \n'
      ' 2 -📝 <Обновить заметку по заголовку> \n')
    
    return int(input(f' ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}'))

def create_note() -> dict:
    '''
    Создание заметки
    
    '''
    result = {}
    result['id'] = get_id()
    result['title_note'] = get_title_note()
    result['text_note'] = get_text_note()
    result['data_note'] = get_data_note()
    return result  

def get_id() -> int:
    '''
    Получение идентификатора заметки
    
    '''
    return  str(uuid.uuid4())[0:3]

def get_title_note() -> str:
    '''
    Получение заголовка заметки
    
    '''
    print('\n' + ('-' + 'o' + '-') * 10 + '\n')
    return input(f'{Fore.YELLOW + Style.BRIGHT}Введите заголовок заметки{Style.RESET_ALL}\n'   
                 f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}\n ✍ ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}')

def get_text_note() -> str:
    '''
    Получение тела 
    
    '''
    print('\n' + ('-' + 'o' + '-') * 10 + '\n')
    return input(f'{Fore.YELLOW + Style.BRIGHT}Введите текст заметки{Style.RESET_ALL}\n'   
                 f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}\n 📝 ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}')

def get_data_note() -> str:
    '''
    Получение даты заметки 
    
    '''
    return str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

def get_search_id() -> str:
    '''
    Получение id заметки для поиска
    '''
    print('\n' + ('-' + 'o' + '-') * 10 + '\n')
    return input(f'{Fore.YELLOW + Style.BRIGHT}Введите id заметки для поиска{Style.RESET_ALL}\n'   
                 f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}\n ✍  ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}') 

def get_changes() -> int:
    '''
    Получение изменений заметки 
    '''
    print('\n' + ('-' + 'o' + '-') * 10)
    print ('\n'
      f'{Fore.YELLOW + Style.BRIGHT}Выберите данные, которые необходимо изменить: ↓{Style.RESET_ALL}\n'
      f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}' 
      ' 1 -✍ <Заголовок заметки> \n'
      ' 2 -📝 <Текст заметки> \n')
      
    return int(input(f' ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}'))

def check_data():
    '''
    Проверка даты
    '''
    while True:
        print('\n' + ('-' + 'o' + '-') * 10)
        date = input('\n'
      f'{Fore.YELLOW + Style.BRIGHT}Введите дату в формате: dd.mm.yyyy: {Style.RESET_ALL}\n'
      f'{Style.RESET_ALL + Fore.CYAN + Style.BRIGHT}\n 📅  ➡ : {Fore.LIGHTGREEN_EX + Style.BRIGHT}')
        temp = date
        try:
            temp = time.strptime(date, '%d.%m.%Y')
            break
        except ValueError:
            print(f'{Fore.RED + Style.BRIGHT}🔴 Неправильный ввод даты!{Style.RESET_ALL}\n')
            continue
    return date

def no_note_error():
    print(f'{Fore.RED + Style.BRIGHT}🔴 Такой заметки нет в записной книге{Style.RESET_ALL}\n')

def no_note_show():
    print(f'{Fore.RED + Style.BRIGHT}🔴 В записной книге нет заметок{Style.RESET_ALL}\n')

def no_index_search():
    print(f'{Fore.RED + Style.BRIGHT}🔴 Неверный выбор, попробуйте еще раз{Style.RESET_ALL}\n')

def info():
    print(f'{Fore.GREEN + Style.BRIGHT}✅ Операция выполнена успешно{Style.RESET_ALL}\n')


def show_note_info(note: dict):
    for k, v in note.items():
        print(f'{k}: {v}')

def show_list_note(notes: list):
    for item in notes:
        print('\n' + ('-' + 'o' + '-') * 10)
        show_note_info(item)
       