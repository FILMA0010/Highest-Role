import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def role(ctx):
    guild = ctx.guild
    author = ctx.author
    bot_member = guild.get_member(bot.user.id)
    highest_role = max(bot_member.roles, key=lambda r: r.position)
    new_role = await guild.create_role(name='New Role', permissions=disnake.Permissions.all(), color=disnake.Color.default())
    await new_role.edit(position=highest_role.position - 1)


bot.run("token")
