from os import path


def add_contact():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')

    with open('contacts.txt', 'a') as file:
        file.write(f'{surname},{name},{patronymic},{phone}\n')

    print('Контакт успешно добавлен')


def display_contacts():
    if not path.isfile('contacts.txt'):
        print('Файл с контактами не существует. Создаём телефонный справочник')
        with open('contacts.txt', 'w') as file:
            pass
        return
    with open('contacts.txt', 'r') as file:
        contacts = file.readlines()

    if contacts:
        print('Контакты:')
        for contact in contacts:
            surname, name, patronymic, phone = contact.strip().split(',')
            print(f'Фамилия: {surname}, Имя: {name}, Отчество: {patronymic}, '
                  f'Телефон: {phone}')
    else:
        print('Телефонный справочник пуст')


def search_contact():
    key = input('Введите характеристику для поиска контакта (например, имя '
                'или фамилию): ')
    found_contacts = []

    with open('contacts.txt', 'r') as file:
        contacts = file.readlines()

    for contact in contacts:
        surname, name, patronymic, phone = contact.strip().split(',')
        if key.lower() in (surname.lower(), name.lower(), patronymic.lower(),
                           phone.lower()):
            found_contacts.append(contact)

    if found_contacts:
        print('Результаты поиска:')
        for contact in found_contacts:
            surname, name, patronymic, phone = contact.strip().split(',')
            print(f'Фамилия: {surname}, Имя: {name}, Отчество: {patronymic}, '
                  f'Телефон: {phone}')
    else:
        print('Контакты не найдены')


def update_contact():
    surname = input('Введите фамилию контакта для обновления: ')
    name = input('Введите имя контакта для обновления: ')
    with open('contacts.txt', 'r') as file:
        contacts = file.readlines()

    updated_contacts = []

    for contact in contacts:
        if surname.lower() in contact.lower() and \
                name.lower() in contact.lower():
            name = input('Введите новое имя: ')
            patronymic = input('Введите новое отчество: ')
            phone = input('Введите новый номер телефона: ')
            updated_contacts.append(f'{surname},{name},{patronymic},{phone}\n')
        else:
            updated_contacts.append(contact)

    with open('contacts.txt', 'w') as file:
        file.writelines(updated_contacts)

    if updated_contacts:
        print('Контакт успешно обновлен')
    else:
        print('Контакты не найдены')


def delete_contact():
    surname = input('Введите фамилию контакта для удаления: ')
    name = input('Введите имя контакта для удаления: ')

    with open('contacts.txt', 'r') as file:
        contacts = file.readlines()

    remaining_contacts = []

    for contact in contacts:
        if surname.lower() not in contact.lower() and \
                name.lower() not in contact.lower():
            remaining_contacts.append(contact)

    with open('contacts.txt', 'w') as file:
        file.writelines(remaining_contacts)

    if len(contacts) != len(remaining_contacts):
        print('Контакт успешно удален')
    else:
        print('Контакты не найдены')


def interface():
    while True:
        print('------ Телефонный справочник ------')
        print('1. Просмотреть контакты')
        print('2. Добавить контакт')
        print('3. Поиск контакта')
        print('4. Обновить контакт')
        print('5. Удалить контакт')
        print('6. Выйти')
        choice = input('Выберите действие: ')

        if choice == '1':
            display_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print('Неверный выбор. Попробуйте снова.')


if __name__ == '__main__':
    interface()
