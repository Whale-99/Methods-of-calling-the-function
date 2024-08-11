recipient = input("Введите получателя: ")
message = input("Введите письмо: ")
sender = input("Введите отправителя (по умолчанию: university.help@gmail.com): ")

def send_email(message, recipient, sender="university.help@gmail.com"):
    print(f"Отправлено сообщение: {message}")
    print(f"Получатель: {recipient}")
    print(f"Отправитель: {sender}")

print()

valid_domains = [".com", ".ru", ".net"]


if (any(recipient.endswith(domain) for domain in valid_domains)) and "@" in recipient:
    if sender:
        if (any(sender.endswith(domain) for domain in valid_domains)) and "@" in sender:
            send_email(message, recipient, sender)
        else:
            print("Неверный адрес отправителя")
    else:
        send_email(message, recipient)
else:
    print("Неверный адрес получателя")
