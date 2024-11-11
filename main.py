#. 1. Определить переменную в которую передаем строку
#  2. Удаляем пробелы в строке и приводим к единому регистру (нижнему)
#  3. Создаем обратную строку: используем срез с обратным шагом.
#  4. Сравниваем 2 строки : если строки равны - вернуть `True`, если нет - вернуть `False`
def check_palindrome(string):
    string = string.lower().replace(" ", "")
    if string == string[::-1]:
        return True
    else:
        return False

print (check_palindrome(input('Введите искомую строку: ')))