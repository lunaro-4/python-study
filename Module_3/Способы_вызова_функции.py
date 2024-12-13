def is_email_valid(email: str) -> bool:
    is_valid = (email.find("@") != -1 and
                (email.endswith(".com")
                or email.endswith(".ru")
                or email.endswith(".net")))
    return is_valid


def send_email(message: str, recipient: str, *,
               sender: str | None = None):
    is_default = True
    if sender is None:
        sender = "university.help@gmail.com"
    else:
        is_default = False
    is_recipient_valid: bool = is_email_valid(recipient)
    is_sender_valid: bool = is_email_valid(sender)
    if not is_recipient_valid or not is_sender_valid:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return

    log: str = f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
    if not is_default:
        log = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! " + log
    print(log)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
