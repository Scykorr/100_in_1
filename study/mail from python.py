# import smtplib as smtp
#
# login = 'fedosovtoxa96@gmail.com'
# password = 'hxhw fqzz ohzz ylrj'
#
# server = smtp.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(login, password)
#
# subject = 'Тестовый заголовок'
# text = 'Тестовый текст письма'
#
# server.sendmail(login, 'fedosov-toxa@mail.ru', f'Subject:{subject}\n{text}'.encode('utf-8'))


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

login_main = 'fedosovtoxa96@gmail.com'
password = 'hxhw fqzz ohzz ylrj'

# Создаем объект сообщения
msg = MIMEMultipart()
msg['From'] = login_main
msg['To'] = 'fedosovtoxa96@gmail.com'
msg['Subject'] = 'Поздравляем! Вы успешно зарегистрировались на сайте inoutproject.ru!'

# HTML-контент
html_content = f"""
<html>
  <body>
    <h1>Поздравляем! Вы успешно зарегистрировались на сайте inoutproject.ru!</h1>
    <p>Ваши <b>логин и пароль</b> для доступа в клиентскую зону!</p>
    <ul>
      <li>Логин: {login_main}</li>
      <li>Пароль: {login_main}</li>
    </ul>
  </body>
</html>
"""

# Добавляем HTML-часть в сообщение
msg.attach(MIMEText(html_content, 'html', 'utf-8'))

# Отправка письма
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(login_main, password)
    # server.sendmail(login, 'fedosov-toxa@mail.ru', msg.as_string())
    server.sendmail(login_main, 'fedosovtoxa96@gmail.com', msg.as_string())
