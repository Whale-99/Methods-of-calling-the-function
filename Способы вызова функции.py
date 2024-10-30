recipient = input("Введите получателя: ")
message = input("Введите письмо: ")
sender = input("Введите отправителя (по умолчанию: university.help@gmail.com): ")

def send_email(message, recipient, sender="university.help@gmail.com"):
    # Список допустимых доменов
    valid_domains = [".com", ".ru", ".net"]

    # Проверка корректности email с использованием допустимых доменов
    def is_valid_email(email):
        return "@" in email and any(email.endswith(domain) for domain in valid_domains)

    # Проверка на корректность email
    if not (is_valid_email(sender) and is_valid_email(recipient)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка, если отправитель по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Вызов функции с пользовательским вводом
send_email(message, recipient, sender if sender else "university.help@gmail.com")
