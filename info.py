import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7760628586:AAG5krIGBLes2phnjp5YhzpE_daXYa_4q5c")
API_ID = int(os.environ.get("API_ID", "23889992"))
API_HASH = os.environ.get("API_HASH", "70bf3c9baebf30afff8c32649bf23c3d")
PICS = os.environ.get("PICS", "https://files.catbox.moe/4yd59m.jpg").split()
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1900118264').split()]
DB_URL = os.environ.get("DB_URL", "mongodb+srv://HDMoviesEarth:unqOY8gUrmDLNXHd@cluster0.0xjypxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "HDMoviesEarth")
RemoveBG_API = os.environ.get("RemoveBG_API", "")
IBB_API = os.environ.get("IBB_API", "")
FORCE_SUB = os.environ.get("FORCE_SUB", "-1001943817170")
PORT = os.environ.get('PORT', '8080')          
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002645203047'))
LOG_TEXT = """<i><u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc_id}</code>
○ First Name : <code>{first_name}<code>
○ UserName : @{username}

By = {bot}</i>"""
