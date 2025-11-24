import os
import discord
from discord.ext import commands
from discord import app_commands
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

client = OpenAI(api_key=OPENAI_API_KEY)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

EGGHUB_SCRIPT = '''
loadstring(game:HttpGet("https://raw.githubusercontent.com/minh597/Egg/refs/heads/main/ripperhub.lua"))()
getgenv().EggHub = {autoskip=true,SellAllTower=true,AtWave=0,autoCommander=false,MarcoUrl=""}
loadstring(game:HttpGet("https://api.junkie-development.de/api/v1/luascripts/public/563d9f1ab1ca207f7d8cfa7cfe82e94a1482d82c7962da52ce473c981b084220/download"))()
'''

GUIDE = """**EGG HUB FULL GUIDE (LATEST 24 NOV 2025)**

1. Inject any executor (Solara / Delta / Codex recommended)
2. Paste the script below → Execute

```lua
''' + EGGHUB_SCRIPT + '''
