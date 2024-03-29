from colorama import *

"""

Основні Функції та  Класи для роботи з 'colorama' є:

init(...) === та встановлення налаштувань консолі;

Fore === Для встановлення кольору тексту;
Back === Для встановлення кольору фону тексту;
Style === Для встановлення стилю тексту;
Cursor === Для встановлення позиції тексту у консолі;
"""

# =====================================================================================#

""" Приклади: """
""" init() """

"""
        init(autoreset=False, convert=False, strip=False, wrap=False)
"""
"""
        init() атрибут autoreset(bool) :

Якщо ви неодноразово надсилаєте послідовності скидання для
вимкнення зміни кольору в кінці кожного друку, тоді
""init(autoreset=True)"" автоматизує це."""
"""
Example  
"""

# from colorama import init
# init(autoreset=True)
# print(Fore.RED + 'some red text')
# print('automatically back to default color again')

# =====================================================================================#

"""

        init() атрибут convert(bool) :

Передайте True або False, щоб перевизначити, чи слід видаляти коди ANSI з виводу.
Поведінка за замовчуванням — видаляти, якщо в Windows або якщо вихід перенаправляється

"""
# =====================================================================================#

"""

        init() атрибут strip(bool) :

Передайте True або False, щоб змінити, чи потрібно перетворювати коди ANSI у виводі на виклики win32.
Поведінка за замовчуванням полягає в тому, щоб конвертувати, якщо у Windows

"""
# =====================================================================================#

"""

        init() атрибут wrap(bool) :

У Windows Colorama працює шляхом заміни sys.stdout і sys.stderr на проксі-об’єкти, які замінюють метод .
write() для виконання своєї роботи. Якщо таке обгортання викликає у вас проблеми, його можна вимкнути, 
передавши init(wrap=False). Поведінка за замовчуванням полягає в перенесенні, якщо автоматичне скидання,
видалення чи перетворення мають значення True.

Якщо обтікання вимкнено, кольоровий друк на платформах, відмінних від Windows, працюватиме як зазвичай. 
Щоб зробити міжплатформний кольоровий вивід, ви можете безпосередньо використовувати проксі AnsiToWin32 від Colorama:
"""
"""
        Example  
"""
# import sys
# from colorama import init, AnsiToWin32
# init(wrap=False)
# stream = AnsiToWin32(sys.stderr).stream
#
# # Python 2
# print >>stream, Fore.BLUE + 'blue text on stderr'
#
# # Python 3
# print(Fore.BLUE + 'blue text on stderr', file=stream)


# =====================================================================================#

""" Fore: """

""" Використовується для встановлення кольору тексту приклад:"""

print(Fore.RED + "HELLO COLORAMA")


# =====================================================================================#

""" Back: """
"""
 Використовується для встановлення кольору фону тексту приклад:

 #print(Back.RED + "HELLO COLORAMA")
"""

# =====================================================================================#

""" Style: """
"""
 Використовується для встановлення стилю тексту приклад:

 #print(Style.BRIGHT + "HELLO COLORAMA")
"""

# =====================================================================================#

""" Cursor: """
"""
 Використовується для встановлення позиції виводу тексту приклад:

 #print(Cursor.FORWARD(80) + "HELLO COLORAMA")

 P.S. Не процює в консолі PyCharm
"""

# =====================================================================================#

"""

Також можна поєднувати класи вигляду тексту наприклад:

#init(autoreset=True) (P.S. Можна використовувати без цього рядка але буде не дуже зручно)
#print(Fore.BLUE + Back.WHITE + Style.BRIGHT + Cursor.FORWARD(50) +"HELLO COLORAMA") 

"""