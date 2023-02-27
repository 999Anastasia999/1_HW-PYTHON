'''Модуль контроллер - пусковой файл'''

import manager
import view 


def start():   
    while True:  
        choice = view.menu()                        
        match choice:                               
            case 1:                                 
                manager.open_file()             
            case 2:
                manager.save_file()
            case 3:
                pb = manager.get()
                view.show_contacts(pb)
            case 4:
                new = view.new_contact_input()
                manager.add(new)                  
            case 5:
                pb = manager.get()
                view.show_contacts(pb)
                ind = view.input_id()
                contact = view.new_contact_input()
                manager.change_contact(ind, contact)
            case 6:
                find = view.find_contact()           
                result = manager.find(find)
                view.show_contacts(result)          
            case 7:
                pb = manager.get()
                view.show_contacts(pb)
                ind = view.input_id()
                name = manager.get_name(ind)
                if view.confirm('удалить', name):
                    manager.delete_contact(ind)            
            case 8:
                if manager.check_changes():
                    if view.confirm_changes():
                        manager.save_file()
                print('До свидания!')
                break
            