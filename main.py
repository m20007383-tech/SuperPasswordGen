import secrets
import string

pool = string.ascii_letters + string.digits + string.punctuation

try:
    length = int(input("Введите длину: "))
except ValueError:
    print("Ошибка! Используем длину по умолчанию (8).")
    length = 8

password = ''.join(secrets.choice(pool) for _ in range(length))
print(f"Ваш пароль: {password}")


