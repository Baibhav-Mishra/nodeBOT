import discord
import gspread
from discord import partial_emoji
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from discord.partial_emoji import PartialEmoji


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
# x = message.guild.members
# print(x)

# client = discord.Client()
# from discord.ext import commands

# bot = commands.Bot(command_prefix='!')

# @bot.command(pass_context=True)
# async def poke(ctx, member: discord.Member):
#     await bot.send_message(member, 'boop')
    
# bot.run('ODY5NTMyNjYxNjA0MDM2NjQ5.YP_lZQ.r7VEAReL1HIT0Zo106pUPaxJN8E')
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_message_id = 869869776338563143 # ID of the message that can be reacted to to add/remove a role.
        self.emoji_to_role = {
            discord.PartialEmoji(name='🎨'):869652074516861049,#create[x]
            discord.PartialEmoji(name='📊'): 869652804644511804,#MSway #nocopy
            discord.PartialEmoji(name='🎮'): 869652674314911754,#analogous
            discord.PartialEmoji(name='🎥'):869850824136876092,#infocus
            discord.PartialEmoji(name='mic', id=869861964430598174):847797471962071060,#geekathon
            discord.PartialEmoji(name='woym',id=869862400868892672):869653253758013511,#WOYM
            discord.PartialEmoji(name='mine', id=869807519407669279): 869658442997039134,#craftathon
            discord.PartialEmoji(name='paintbrush2', id=869862753748258847):869653307424124998,#comicdes
        }

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:

            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            print('hello')
            # user = client.get_user(payload.user_id)
            
            # await payload.message_id.reaction.remove(payload.emoji, user)
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        try:
            # Finally, add the role.
            await payload.member.add_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
        if payload.channel_id == 869519092338528286:

          channel = await client.fetch_channel(payload.channel_id)
          message = await channel.fetch_message(self.role_message_id)

          # iterating through each reaction in the message
          # print(message.reactions)
          for r in message.reactions:

              # checks the reactant isn't a bot and the emoji isn't the one they just reacted with
              # print(payload.emoji, r)
              if payload.member in await r.users().flatten() and  not payload.member.bot and str(r) != str(payload.emoji):

                  # removes the reaction
                  await message.remove_reaction(r.emoji, payload.member)

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        # The payload for `on_raw_reaction_remove` does not provide `.member`
        # so we must get the member ourselves from the payload's `.user_id`.
        member = guild.get_member(payload.user_id)
        if member is None:
            # Make sure the member still exists and is valid.
            return

        try:
            # Finally, remove the role.
            await member.remove_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
        









  
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
            await message.channel.send('gamer')
        elif message.content == "!help":
            await message.channel.send("!hello: hi\n!users: No of participants in server\n!mohak: gamer")
        elif message.content.startswith('!mute') and message.author.guild_permissions.administrator:
            # await message.mentions[0].remove_roles(message.mentions[0].roles)
            await message.mentions[0].add_roles(discord.utils.get(message.guild.roles, name="muted"))
            await message.channel.send('ok')
        elif message.content.startswith('!unmute') and message.author.guild_permissions.administrator:
            # await message.mentions[0].remove_roles(message.mentions[0].roles)
            await message.mentions[0].remove_roles(discord.utils.get(message.guild.roles, name="muted"))
            await message.channel.send('ok')
        elif message.content == "!edit":
          pass



        elif message.content.startswith('!result'):
          name_of_sheet = message.content.split()[1].lower()
          sheet = gspread.authorize(creds).open("Results").worksheet(name_of_sheet)
          data = sheet.get_all_records()
          embedVar = discord.Embed(title="Results", description= '')
          for i in data:
              embedVar.add_field(name=f"{i['Position']}" , value=f"Name: {i['Name']}\nSchool: {i['School']}", inline=False)
        
            
          # embedVar.add_field(name="Create[X]", value="1st: Baibhav\n2nd: Baibhav\n3rd: Baibhav", inline=False)
          
          # embedVar.add_field(name="Field2", value="hi2", inline=False)
          await message.channel.send(embed=embedVar)

        elif message.content.startswith('!member'):
          for guild in client.guilds:
            for member in guild.members:
              # me = await client.get_user_info('MY_SNOWFLAKE_ID')
              # await client.send_message(me, "Hello!")
              await client.send_message(member, 'boop')
                  # print(type(member))
                  # member.send('hi')
                  # channel = await member.create_dm()
                  # user=await client.get_user_info(428220061757472768)
                  # await client.send_message(user, "Your message goes here")
                  # pass
                  # await channel.send('message')
                  # await member.send('t')
                # await member.send('t')
                # print(member.display_name.split('|')[0])
                
        elif message.content == "!get-roles":
            await message.channel.send('''React with the corresponding emoji to get the role for your event 
Create[X] - :art:
MSway - :bar_chart:
Analogous - :video_game:
InFocus - :movie_camera:
Geekathon - <:mic:869861964430598174>
What's on your Mind - <:woym:869862400868892672>
Craftathon - <:mine:869807519407669279>
ComicDes - <:paintbrush2:869862753748258847>
''')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.get_channel(869671953500356649).send(to_send)
      # @client.command(pass_context=True)
      # async def dm(ctx):
      #     user=await client.get_user_info("User's ID here")
      #     await client.send_message(user, "Your message goes here")
      
      


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