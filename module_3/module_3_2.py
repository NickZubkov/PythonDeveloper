def send_email(message, recipient, *, sender="university.help@gmail.com"):
    default_sender = "university.help@gmail.com"
    allowed_domains = [".com", ".ru", ".net"]

    if "@" not in str(recipient) or "@" not in str(sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    is_recipient_domain_allowed = False
    is_sender_domain_allowed = False

    for i in allowed_domains:
        if str(recipient).endswith(i):
            is_recipient_domain_allowed = True
            break

    for i in allowed_domains:
        if str(sender).endswith(i):
            is_sender_domain_allowed = True
            break

    if not is_recipient_domain_allowed or not is_sender_domain_allowed:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == default_sender:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
