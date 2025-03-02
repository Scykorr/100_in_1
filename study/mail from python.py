import smtplib as smtp

login = 'fedosovtoxa96@gmail.com'
password = 'hxhw fqzz ohzz ylrj'

server = smtp.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(login, password)

subject = 'test theme'
text = 'test text'

server.sendmail(login, 'fedosov-toxa@mail.ru', f'Subject:{subject}\n{text}')