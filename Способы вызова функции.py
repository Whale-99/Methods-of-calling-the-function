recipient = input("Введите получателя: ")
message = input("Введите письмо: ")
sender = input("Введите отправителя (по умолчанию: university.help@gmail.com): ")
def send_email(message, recipient, sender="university.help@gmail.com"):
    valid_domains = [".com", ".ru", ".net"]

    if not (any(recipient.endswith(domain) for domain in valid_domains) and "@" in recipient):
        print("Неверный адрес получателя")
        return

    if not (any(sender.endswith(domain) for domain in valid_domains) and "@" in sender):
        print("Неверный адрес отправителя")
        return

    print(f"Отправлено сообщение: {message}")
    print(f"Получатель: {recipient}")
    print(f"Отправитель: {sender}")

if not sender:
    sender = "university.help@gmail.com"

send_email(message, recipient, sender)
