import discord
# from discord.ext.commands import Bot

# bot = Bot("!")

client = discord.Client()

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(f"""Welcome to the server {member.mention}""")


@client.event
async def on_message(message):
    id = client.get_guild(847402192587718663)
    channels = ["general"]

    if str(message.channel) in channels:
        if message.content.find("!hi") != -1:
            await message.channel.send("Hfi")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)


# @client.commands(pass_content=True)
# async def changenick(ctx, member: discord.Member, nick):
#   await member.edit(nick=nick)
#   await ctx.send('testanother') 


client.run('ODY5NTMyNjYxNjA0MDM2NjQ5.YP_lZQ.r7VEAReL1HIT0Zo106pUPaxJN8E')