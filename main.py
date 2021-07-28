import discord

client = discord.Client()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('hi')
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {client.get_guild(847402192587718656).member_count}""")
        elif message.content == "!mohak":
            await message.channel.send('gamers')
        elif message.content == "!help":
            await message.channel.send("!hello: hi\n!users: No of participants in server\n!mohak: gamer")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.get_channel(847402192587718660).send(to_send)



#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.role_message_id = 869777307362013245 # ID of the message that can be reacted to to add/remove a role.
#         self.emoji_to_role = {
#             discord.PartialEmoji(name='🔴'): 0, # ID of the role associated with unicode emoji '🔴'.
#             discord.PartialEmoji(name='🟡'): 0, # ID of the role associated with unicode emoji '🟡'.
#             discord.PartialEmoji(name='green', id=0): 0 # ID of the role associated with a partial emoji's ID.
#         }

#     async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
#         """Gives a role based on a reaction emoji."""
#         # Make sure that the message the user is reacting to is the one we care about.
#         if payload.message_id != self.role_message_id:
#             return

#         guild = self.get_guild(payload.guild_id)
#         if guild is None:
#             # Check if we're still in the guild and it's cached.
#             return

#         try:
#             role_id = self.emoji_to_role[payload.emoji]
#         except KeyError:
#             # If the emoji isn't the one we care about then exit as well.
#             return

#         role = guild.get_role(role_id)
#         if role is None:
#             # Make sure the role still exists and is valid.
#             return

#         try:
#             # Finally, add the role.
#             await payload.member.add_roles(role)
#         except discord.HTTPException:
#             # If we want to do something in case of errors we'd do it here.
#             pass

#     async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
#         """Removes a role based on a reaction emoji."""
#         # Make sure that the message the user is reacting to is the one we care about.
#         if payload.message_id != self.role_message_id:
#             return

#         guild = self.get_guild(payload.guild_id)
#         if guild is None:
#             # Check if we're still in the guild and it's cached.
#             return

#         try:
#             role_id = self.emoji_to_role[payload.emoji]
#         except KeyError:
#             # If the emoji isn't the one we care about then exit as well.
#             return

#         role = guild.get_role(role_id)
#         if role is None:
#             # Make sure the role still exists and is valid.
#             return

#         # The payload for `on_raw_reaction_remove` does not provide `.member`
#         # so we must get the member ourselves from the payload's `.user_id`.
#         member = guild.get_member(payload.user_id)
#         if member is None:
#             # Make sure the member still exists and is valid.
#             return

#         try:
#             # Finally, remove the role.
#             await member.remove_roles(role)
#         except discord.HTTPException:
#             # If we want to do something in case of errors we'd do it here.
#             pass

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('ODY5NTMyNjYxNjA0MDM2NjQ5.YP_lZQ.r7VEAReL1HIT0Zo106pUPaxJN8E')