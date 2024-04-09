# Завдання 1
# Користувач вводить з клавіатури набір чисел. Збережіть отримані числа до однозв’язного списку. Після
# чого покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.
# Дія виконується залежно від вибору користувача,
# після чого меню з’являється знову.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('None')

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def replace(self, old_value, new_value):
        if not self.head:
            return
        if self.head.data == old_value:
            self.head.data = new_value
            return
        current = self.head
        while current.next:
            if current.next.data == old_value:
                current.next.data = new_value
                return
            current = current.next

    def menu(self):
        print('Введіть список чисел, розділених пробілами:')
        numbers = list(map(int, input().split()))
        for num in numbers:
            self.append(num)
        while True:
            print('\n1. Додати елементи.')
            print('2. Видалити елементи.')
            print('3. Показати вміст списку.')
            print('4. Перевірте, чи є значення у списку.')
            print('5. Замінити значення в списку.')
            print('6. Вийти.')
            choice = int(input('Введіть свій вибір: '))
            if choice == 1:
                value = int(input('Введіть значення для додавання: '))
                self.append(value)
            elif choice == 2:
                value = int(input('Введіть значення для видалення: '))
                self.delete(value)
            elif choice == 3:
                self.display()
            elif choice == 4:
                value = int(input('Введіть значення для перевірки: '))
                if self.search(value):
                    print('Значення є у списку.')
                else:
                    print('Такого значення немає в списку.')
            elif choice == 5:
                old_value = int(input("Введіть старе значення: "))
                new_value = int(input("Введіть нове значення: "))
                self.replace(old_value, new_value)
            elif choice == 6:
                break
            else:
                print('Неправильне значення, спробуйте ще раз.')

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.menu()















# Завдання 2
# Користувач вводить з клавіатури набір рядків. Збережіть отримані рядки до двозв’язного списку. Після чого
# покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.
# Дія виконується залежно від вибору користувача,
# після чого меню з’являється знову.