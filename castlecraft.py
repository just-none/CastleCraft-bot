import asyncio, base64, codecs, ctypes, datetime, discord, json, os, random, requests, time
from colorama import Fore
from discord.ext import commands
from urllib.parse import urlencode

#bot settings
BOT_GUILD = "GUILD_ID_HERE"
MODROLE = "ID_FOR_MODERATOR_ROLE"
ROLECHANNEL = "CHANNEL_ID_FOR_REACTION_ROLES"
MODMAIL_CHANNEL = "CHANNEL_ID_FOR_MODMAIL"
MODLOG_CHANNEL = "CHANNEL_ID_FOR_LOGS"
WELCOME_CHANNEL = "CHANNEL_ID_FOR_WELCOME_MESSAGES"
BALANCE_CHANNEL = "CHANNEL_ID_FOR_BALANCES_EMBED"
MUTEROLE = "ID_FOR_MUTED_ROLE"
MEMBER_ROLE = "ID_FOR_ON-JOIN_ROLE"
TOKEN =  "BOT_TOKEN"
MANAGER = "MANAGER_ID" #manager is the person that will check in case of problems with the code

#embed settings
#color format: 0x + HEX value (0xcd0000 -> red)
color = 0x2C94DF
gold_color = 0xFFD700
error_color = 0xcd0000
title = "EMBED_TITLE" # must be a url
icon = "EMBED_ICON" # must be a url
server_icon = "SERVER_ICON" # must be a url
footer = "FOOTER_TEXT"

# convert time from Days, Hours or Minutes into Seconds
time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
def convert(time):

    try:

        return int(time[:-1]) * time_convert[time[-1]]

    except:

        return time

# functions for balance command
def _save():
    with open('balance.json', 'w+') as f:
        json.dump(balances, f)

def register(name, amount):
    balances[name] = amount
    _save()

#window title
ctypes.windll.kernel32.SetConsoleTitleW(f'Castle_craft bot | made by piombacciaio')

#bot ready to be connected
time__ = datetime.datetime.now().strftime("%H:%M")
print("" + time__ + " | " + Fore.GREEN + "[Event]  " + Fore.RESET + f' | Connecting to discord')

#bot setup
bot = discord.Client()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', case_insensitive=True, owner_ids=(624712494379827231, 775710967706157057), intents=intents)
bot.remove_command("help")

balances = {}

#bot version (arbitrary value)
version= 1.4


#help commands
@bot.command(name="help", usage=f"{bot.command_prefix}help", description="this message", brief="main")
async def _help(ctx):

    commandinfo = ''

    for command in bot.commands:

        if command.brief == "main":

            commandinfo += f'{command.usage} | {command.description}\n'

    embed = discord.Embed(title=title, description=f'\n{commandinfo}', color=color)
    embed.set_thumbnail(url=icon)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}tools", description="show tools commands", brief="main")
async def tools(ctx):

    commandinfo = ''

    for command in bot.commands:

        if command.brief == "tools":

            commandinfo += f'{command.usage} | {command.description}\n'

    embed = discord.Embed(title=title, description=f'\n{commandinfo}', color=color)
    embed.add_field(name=chr(173), value="() = unrequired element   [] = required element", inline=False)
    embed.set_thumbnail(url=icon)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}textual", description="show textual commands", brief="main")
async def textual(ctx):

    commandinfo = ''

    for command in bot.commands:

        if command.brief == "textual":

            commandinfo += f'{command.usage} | {command.description}\n'

    embed = discord.Embed(title=title, description=f'\n{commandinfo}', color=color)
    embed.add_field(name=chr(173), value="() = unrequired element   [] = required element", inline=False)
    embed.set_thumbnail(url=icon)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}fun", description="show fun commands", brief="main")
async def fun(ctx):

    commandinfo = ''

    for command in bot.commands:

        if command.brief == "fun":

            commandinfo += f'{command.usage} | {command.description}\n'

    embed = discord.Embed(title=title, description=f'\n{commandinfo}', color=color)
    embed.add_field(name=chr(173), value="() = unrequired element   [] = required element", inline=False)
    embed.set_thumbnail(url=icon)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}server", description="show server commands", brief="main")
async def server(ctx):
    
    commandinfo = ''

    for command in bot.commands:

        if command.brief == "server":

            commandinfo += f'{command.usage} | {command.description}\n'

    embed = discord.Embed(title=title, description=f'\n{commandinfo}', color=color)
    embed.add_field(name=chr(173), value="() = unrequired element   [] = required element", inline=False)
    embed.set_thumbnail(url=icon)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}admin", description="show server admin commands", brief="server")
async def admin(ctx):

    commandinfo = ''

    for command in bot.commands:

        if command.brief == "admin":

            commandinfo += f'{command.usage} | {command.description}\n'

    embed = discord.Embed(title=title, description=f'\n{commandinfo}', color=color)
    embed.add_field(name=chr(173), value="() = unrequired element   [] = required element", inline=False)
    embed.set_thumbnail(url=icon)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}image", description="show image commands", brief="main")
async def image(ctx):

    commandinfo = ''

    for command in bot.commands:

        if command.brief == "image":

            commandinfo += f'{command.usage} | {command.description}\n'

    embed = discord.Embed(title=title, description=f'\n{commandinfo}', color=color)
    embed.add_field(name=chr(173), value="() = unrequired element   [] = required element", inline=False)
    embed.set_thumbnail(url=icon)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}owner", description="show owner commands", brief="admin")
async def owner(ctx):

    commandinfo = ''

    for command in bot.commands:

        if command.brief == "owner":

            commandinfo += f'{command.usage} | {command.description}\n'

    embed = discord.Embed(title=title, description=f'\n{commandinfo}', color=color)
    embed.add_field(name=chr(173), value="() = unrequired element   [] = required element", inline=False)
    embed.set_thumbnail(url=icon)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)



#server
@bot.command(usage=f"{bot.command_prefix}poll", description="create a poll", brief="server")
async def poll(ctx):

    embed = discord.Embed(title="New poll!", description="we are going to create a new poll, answer those questions within 120 seconds.", color=color)
    embed.set_footer(text="we are switching to plain text, easier to code :)")
    await ctx.send(embed=embed)

    questions = [f"In which channel the poll is going to be? Please do like this {ctx.channel.mention}", "What is the title? (answer 'def' if you want the default title)", "What is the first option?", "What is the second option?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
        
    #send questions
    for i in questions:
        await ctx.send(i)

        try:

            msg = await bot.wait_for('message', timeout=120, check=check)

        except asyncio.TimeoutError:

            await ctx.send('You answered too late', delete_after=10)
            return

        else:

            answers.append(msg.content)
        
    #get channel
    try:

        c_id = int(answers[0][2:-1])

    except:

        await ctx.send(f"Invalid channel mention. Do like this {ctx.channel.mention}.", delete_after=10)
        return
        
    channel = bot.get_channel(c_id)

    #get title
    ti = answers[1]

    if ti == "def" or ti == "'def'":

        ti = "poll"

    #get description
    text1 = answers[2]
    text2 = answers[3]
    await ctx.send(f"The new poll will be found in {channel.mention}.")

    embed = discord.Embed(title=ti, description=f"`🟦{text1}`\n\nor\n\n`🟥{text2}`", color=color)

    m=await channel.send(embed=embed)
    await m.add_reaction("🟦")
    await m.add_reaction("🟥")

@bot.command(usage=f"{bot.command_prefix}suggest [text]", description="suggestion from members to staff", brief="server")
async def suggest(ctx, *, argument = None):

    if argument:

        no = "\N{THUMBS DOWN SIGN}"
        yes = "\N{THUMBS UP SIGN}"
        embed = discord.Embed(title="Suggestion", description=argument, color=color)
        embed.set_footer(text=f"Use one of the reactions to cast your vote")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(yes)
        await msg.add_reaction(no)

    else:

        embed = discord.Embed(title="Error!", description=f"Sorry for the inconvenient, but the following parameter is missing `text`. Please provide it", color=error_color)
        await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}servericon", description="transform the server icon into a PNG photo", brief="server")
async def servericon(ctx):

    if len(ctx.guild.icon_url) > 1:

        embed= discord.Embed().set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
        
    else:

        embed=discord.Embed(title="ERROR!", description="Server icon is either default of discord or unreachable", color=error_color)
        await ctx.send(embed=embed, delete_after=5)

@bot.command(usage=f"{bot.command_prefix}serverinfo", description="Get the info about a server", brief="server")
async def serverinfo(ctx):

    name = ctx.guild.name
    description = ctx.guild.description
    server_id = ctx.guild.id
    region = ctx.guild.region
    memberCount = ctx.guild.member_count
    icon = ctx.guild.icon_url

    embed = discord.Embed(title=name + " Server Information", description=f"server description: {description}", color=color)
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Server ID", value=server_id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}userinfo (mention)", description="Get the info about a user account", brief="server")
async def userinfo(ctx, user: discord.User = None):

    if user == None:
        user = ctx.message.author

    since_created = (ctx.message.created_at - user.created_at).days
    user_created = user.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(user_created, since_created)
    embed=discord.Embed(title=f"Info for: {user.name}", description=f"User: {user.name}#{user.discriminator}\nID: {user.id}\nAvatar: {user.avatar_url_as(static_format='png')}\nCreated On: {created_on}\nBot: {user.bot}", color=0x00dff)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}memberinfo [mention]", description="Get info about a server member", brief="server")
async def memberinfo(ctx, user: discord.Member = None):

    if isinstance(ctx.channel, discord.channel.DMChannel):

        embed=discord.Embed(title="ERROR!", description="Please use this command in a server", color=error_color)
        await ctx.send(embed=embed, delete_after=5)

    else:

        if user == None:
            user = ctx.author

        since_created = (ctx.message.created_at - user.created_at).days
        user_created = user.created_at.strftime("%d %b %Y %H:%M")
        created_on = "{} ({} days ago)".format(user_created, since_created)
        since_created2 = (ctx.message.created_at - user.joined_at).days
        user_joined = user.joined_at.strftime("%d %b %Y %H:%M")
        joined_on = "{} ({} days ago)".format(user_joined, since_created2)

        embed=discord.Embed(title=f"Member info for {user.name}", 
        description=f"Member: {user.name}#{user.discriminator}\nID: {user.id}\nJoined On: {joined_on}\nCreated On: {created_on}",
        color=color)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
    
@bot.command(usage=f"{bot.command_prefix}roleinfo [mention]", description="Get the info about a role", brief="server")
async def roleinfo(ctx, role: discord.Role = None):

    if isinstance(ctx.channel, discord.channel.DMChannel):
        embed=discord.Embed(title="ERROR!", description="Please use this command in a server", color=error_color)
        await ctx.send(embed=embed, delete_after=5)

    else:

        if role:

            since_created = (ctx.message.created_at - role.created_at).days
            role_created = role.created_at.strftime("%d %b %Y %H:%M")
            created_on = f"{role_created} ({since_created} days ago)"
            users = len([x for x in ctx.guild.members if role in x.roles])

            if str(role.colour) == "#000000":

                color = "default"

            else:

                color = str(role.color).upper()
                embed=discord.Embed(title=f"Role info for: {role.name}", description=f"Name: {role.name}\nServer: {role.guild}\nUsers: {users}\nColor: {color}\nPosition: {role.position}\nCreated On: {created_on}", color=0x00dfff)
                await ctx.send(embed=embed)

        else:

            embed=discord.Embed(title="ERROR!", description="Please provide a valid role", color=error_color)
            await ctx.send(embed=embed, delete_after=5)



#admin
@bot.command(usage=f"{bot.command_prefix}unmute [mention]", description="unmute a user", brief="admin")
@commands.guild_only()
@commands.has_any_role("Admin", "bot dev")
async def unmute(ctx, member : discord.Member = None):

    if member:

        modlog = bot.get_channel(MODLOG_CHANNEL)
        await member.remove_roles(discord.utils.get(ctx.guild.roles, id=MUTEROLE))

        unmute = discord.Embed(color=color, title="UNMUTE", description=f"{member.mention} has been unmuted")
        unmute.set_thumbnail(url=member.avatar_url)
        unmute.set_footer(text=footer)
        await modlog.send(embed=unmute)
    
    else:

        embed = discord.Embed(title="Error!", description=f"Please provide a member to unmute", color=error_color)
        await ctx.send(embed=embed)  

@bot.command(usage=f"{bot.command_prefix}mute [mention] (reason)", description="mute a user", brief="admin")
@commands.guild_only()
@commands.has_any_role("Admin", "bot dev")
async def mute(ctx, member : discord.Member = None, reason=None):

    if reason == None:
        reason = "No Reason Provided"

    if member:

        mute = discord.utils.get(ctx.guild.roles, id=MUTEROLE)
        modlog = bot.get_channel(MODLOG_CHANNEL)
        await member.add_roles(mute)

        muted = discord.Embed(colour=color, title="MUTE", description=f"{member.mention} has been muted!\nReason: {reason}")
        muted.set_thumbnail(url=member.avatar_url)
        muted.set_footer(text=footer)
        await ctx.channel.send(embed=muted)

        log = discord.Embed(color=color, title="MUTE", description=f"{member.mention} has been muted")
        log.set_thumbnail(url=member.avatar_url)
        log.add_field(name="Moderator", value=f"{ctx.message.author}")
        log.add_field(name="Reason", value=f"{reason}")
        log.set_footer(text=footer)
        await modlog.send(embed=log)

        Dm = discord.Embed(color=color, title="Mute Notification!", description="You have been muted in Castle_Craft Discord Server")
        Dm.set_footer(text=f"Responsible moderator: {ctx.message.author.mention}")
        Dm.add_field(name="Reason", value=f"{reason}")
        user = bot.get_user(member.id)
        await user.send(embed=Dm)

    else:

        embed = discord.Embed(title="Error!", description=f"Please provide a member to mute", color=error_color)
        await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}tempmute [mention] [s/m/h/d] (reason)", description="temporary mute a user", brief="admin", aliases=["tmute"])
@commands.guild_only()
@commands.has_any_role("Admin", "bot dev")
async def tempmute(ctx, member : discord.Member, time=None, reason=None):

    if reason == None:
        reason = "No Reason Provided"

    if time == None:
        time = "600s"
    
    if member:

        t = convert(time)
        mute = discord.utils.get(ctx.guild.roles, id=MUTEROLE)
        modlog = bot.get_channel(MODLOG_CHANNEL)
        await member.add_roles(mute)

        mute = discord.Embed(colour=color, title="MUTE", description=f"{member.mention} has been muted!\nReason: {reason}")
        mute.set_thumbnail(url=member.avatar_url)
        mute.set_footer(text=footer)
        await ctx.channel.send(embed=mute)

        log = discord.Embed(color=color, title="MUTE", description=f"{member.mention} has been muted for: {time}")
        log.set_thumbnail(url=member.avatar_url)
        log.add_field(name="Moderator", value=f"{ctx.message.author}")
        log.add_field(name="Reason", value=f"{reason}")
        log.set_footer(text=footer)
        await modlog.send(embed=log)

        Dm = discord.Embed(color=color, title="Mute Notification!", description="You have been muted in Castle_Craft Discord Server")
        Dm.set_footer(text=f"Responsible moderator: {ctx.message.author.mention}")
        Dm.add_field(name="Reason", value=f"{reason}")
        Dm.add_field(name="Duration", value=f"{time}")
        await member.send(embed=Dm)

        await asyncio.sleep(t)
        await member.remove_roles(discord.utils.get(ctx.guild.roles, id=MUTEROLE))

        unmute = discord.Embed(color=color, title="UNMUTE", description=f"{member.mention} has been unmuted")
        unmute.set_thumbnail(url=member.avatar_url)
        unmute.set_footer(text=footer)
        await modlog.send(embed=unmute)

    else:

        embed = discord.Embed(title="Error!", description=f"Please provide a member to temporary mute", color=error_color)
        await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}kick [user] (reason)", description="kick a member", brief="admin")
@commands.guild_only()
@commands.has_any_role("Admin")
async def kick(ctx, member : discord.Member = None, *,reason=None):

    if reason == None:
        reason = "No Reason Provided"
    
    if member:

        modlog = bot.get_channel(MODLOG_CHANNEL)

        Dm = discord.Embed(color=color, title="Kick Notification!", description="You have been kicked from Castle_Craft Discord Server")
        Dm.set_footer(text=f"Responsible moderator: {ctx.message.author.mention}")
        Dm.add_field(name="Reason", value=f"{reason}")
        await member.send(embed=Dm)

        await member.kick(reason=reason)

        embed = discord.Embed(title="Kick", color= color, description=f"successfully kicked {member.mention}")
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)

        log = discord.Embed(title="KICK", description=f"kicked user: {member.mention}", color=color)
        log.add_field(name="Moderator", value=ctx.message.author.mention)
        log.add_field(name="Reason", value=reason)
        log.set_footer(text=footer)
        await modlog.send(embed=log)
    
    else:

        embed = discord.Embed(title="Error!", description=f"Please provide a member to kick", color=error_color)
        await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}ban [user] (reason)", description="ban a member", brief="admin")
@commands.guild_only()
@commands.has_any_role("Admin")
async def ban(ctx, member : discord.Member = None, *,reason=None):

    if reason == None:
        reason = "No Reason Provided"
    
    if member:
       
        modlog = bot.get_channel(MODLOG_CHANNEL)

        Dm = discord.Embed(color=color, title="Ban Notification!", description="You have been banned from Castle_Craft Discord Server")
        Dm.set_footer(text=f"Responsible moderator: {ctx.message.author.mention}")
        Dm.add_field(name="Reason", value=f"{reason}")
        await member.send(embed=Dm)

        await member.ban(reason=reason)

        embed = discord.Embed(title="ban", color= color, description=f"successfully banned {member.mention}")
        embed.set_footer(text=footer)
        await ctx.send(embed=embed)

        log = discord.Embed(title="BAN", description=f"banned user: {member.mention}", color=color)
        log.add_field(name="Moderator", value=ctx.message.author.mention)
        log.add_field(name="Reason", value=reason)
        log.set_footer(text=footer)
        await modlog.send(embed=log)

    else:

        embed = discord.Embed(title="Error!", description=f"Please provide a member to ban", color=error_color)
        await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}purge (amount)", description="delete an amount of messages (Default: 10 messages)", brief="admin")
@commands.guild_only()
@commands.has_any_role("Admin", "bot dev")
async def purge(ctx, amount=10):

    modlog = bot.get_channel(MODLOG_CHANNEL)

    await ctx.message.delete()

    await ctx.channel.purge(limit=amount)

    log = discord.Embed(title="PURGE", description=f"{amount} message(s) have been purged in {ctx.channel.mention}", color=color)
    log.add_field(name="Moderator", value=f"{ctx.message.author.mention}")
    log.set_footer(text=footer)
    await modlog.send(embed=log)

@bot.command(usage=f"{bot.command_prefix}unban [name#tag]", description="unban a user", brief="admin")
@commands.guild_only()
@commands.has_any_role("Admin")
async def unban(ctx, *, member = None):

    if member:

        modlog = bot.get_channel(MODLOG_CHANNEL)
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:

                user = ban_entry.user

                if(user.name, user.discriminator) == (member_name, member_discriminator):

                    await ctx.guild.unban(user)
                    embed = discord.Embed(title="Unban", color=color, description=f"successfully unbanned {user.mention}")
                    embed.set_footer(text=footer)
                    await ctx.send(embed=embed)
            
        if len(user) > 1:

            log=discord.Embed(title="UNBAN", description=f"User unbanned: {user.mention}", color=color)
            log.add_field(name="Moderator", value=ctx.message.author.mention)
            log.set_footer(text=footer)
            await modlog.send(embed=log)

        else:

            embed = discord.Embed(title="Unban", color=color, description=f"no user found matching the input")
            await ctx.send(embed=embed)

    else:

        embed = discord.Embed(title="Error!", description=f"Please provide a member to unban with the following format `name#discriminator`", color=error_color)
        await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}reboot", description="Reboots the bot", brief="owner")
@commands.is_owner()
async def reboot(ctx):

    print("Rebooting...")
    print("Please wait...")
    os.system('cls')
    time.sleep(0.1)

    try:

        os.system("python castlecraft.py")
        quit()

    except:
        os.system("cls")
        os.system("castlecraft.exe")

@bot.command(usage=f"{bot.command_prefix}nuke [channel]", description="nuke a channel", brief="admin")
@commands.guild_only()
@commands.has_any_role("Admin")
async def nuke(ctx, *, channel: discord.TextChannel = None):

    if isinstance(ctx.channel, discord.channel.DMChannel):

        embed=discord.Embed(title="ERROR!", description="Please use this command in a server", color=error_color)
        await ctx.send(embed=embed, delete_after=5)

    else:

        if channel:

            channel = channel or ctx.channel
            pos = channel.position
            newchannel = await channel.clone(reason=f"Action performed by {ctx.author} ({ctx.author.id})")
            await newchannel.edit(position=pos)
            await channel.delete()
        
        else:

            embed = discord.Embed(title="Error!", description=f"Missing channel, aborting operation to prevent accidental elimination of a channel", color=error_color)
            await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}balance [add/remove] [amount] [receiver] (sender)", description="manage economy", brief="admin")
async def balance(ctx, operator, amount : int, to_member:discord.User, from_member:discord.User = None):
    time_ = datetime.datetime.now().strftime("%H:%M")

    if to_member:

        if operator.lower() == "add":

            try:

                member_balance = int(balances[to_member.name])
                    
                member_balance += amount
                        
                balances[to_member.name] = member_balance

                _save()
                        
                print("" + time_ + " | " + Fore.YELLOW + "[Money]  " + Fore.RESET + f" | {ctx.message.author.name} added {amount} to {to_member.name}'s balance")

                if from_member:

                    try:
                
                        member_balance = int(balances[from_member.name])
                        
                        member_balance -= amount

                        if member_balance >= 0:
                                    
                            balances[from_member.name] = member_balance

                            _save()
                            print("" + time_ + " | " + Fore.YELLOW + "[Money]  " + Fore.RESET + f" | {ctx.message.author.name} removed {amount} to {from_member.name}'s balance")

                        else:

                            embed = discord.Embed(title="Attention", description=f"{from_member.name}'s balance is insufficient. The transaction will be cancelled.")
                            await ctx.message.reply(embed=embed)
                                
                            member_balance = int(balances[to_member.name])
                        
                            member_balance -= amount
                                    
                            balances[to_member.name] = member_balance

                            _save()
                                    
                            print("" + time_ + " | " + Fore.YELLOW + "[Money]  " + Fore.RESET + f" | {ctx.message.author.name} removed {amount} to {to_member.name}'s balance")

                    except:

                        value = 0

                        value -= amount
                            
                        embed = discord.Embed(title="Attention", description=f"{from_member.name} has been added to the database but the balance is negative.", color=gold_color)
                        await ctx.message.reply(embed=embed)

                        register(name=from_member.name, amount=value)
                        print("" + time_ + " | " + Fore.YELLOW + "[Money]  " + Fore.RESET + f" | {ctx.message.author.name} removed {amount} to {from_member.name}'s balance")

            except:
                        
                register(to_member.name, amount)
                print("" + time_ + " | " + Fore.YELLOW + "[Money]  " + Fore.RESET + f" | {ctx.message.author.name} added {amount} to {to_member.name}'s balance")

            embed = discord.Embed(title="Players wealth", color=color)
            embed.set_thumbnail(url=icon)
            for user in balances:
                embed.add_field(name=user, value=f"{balances[user]} CC", inline=False)
            balchannel = bot.get_channel(BALANCE_CHANNEL)
            await balchannel.purge(limit=25)
            await balchannel.send(embed=embed)

        elif operator.lower() == "remove":
                    
            try:
                        
                member_balance = int(balances[to_member.name])
                        
                member_balance -= amount

                if member_balance >= 0:
                            
                    balances[to_member.name] = member_balance

                    _save()
                    print("" + time_ + " | " + Fore.YELLOW + "[Money]  " + Fore.RESET + f" | {ctx.message.author.name} removed {amount} to {to_member.name}'s balance")

                else:

                    embed = discord.Embed(title="Attention", description=f"{to_member.name}'s balance is insufficient. The transaction will be cancelled.", color=gold_color)
                    await ctx.message.reply(embed=embed)

            except:

                value = 0
                value -= amount

                register(name=to_member.name, amount=value)

                embed = discord.Embed(title="Attention", description=f"{to_member.name} has been added to the database but the balance is negative.", color=gold_color)
                await ctx.message.reply(embed=embed)

                print("" + time_ + " | " + Fore.YELLOW + "[Money]  " + Fore.RESET + f" | {ctx.message.author.name} removed {amount} to {to_member.name}'s balance")

            embed = discord.Embed(title="Players wealth", color=color)
            embed.set_thumbnail(url=icon)
            for user in balances:
                embed.add_field(name=user, value=f"{balances[user]} CC", inline=False)
            balchannel = bot.get_channel(BALANCE_CHANNEL)
            await balchannel.purge(limit=25)
            await balchannel.send(embed=embed)

        else:

            embed = discord.Embed(title="Error!", description=f"an invalid operator has been passed, please do like this:\n $balance add 1 {ctx.author.mention} or $balance remove 1 {ctx.author.mention}")
            await ctx.send(embed=embed)

    else:

        embed = discord.Embed(title="Error!", description=f"Please provide all the required fields", color=error_color)
        await ctx.message.reply(embed=embed, mention_author=False)

emoji_list = ["1️⃣",
              "2️⃣",
              "3️⃣", 
              "4️⃣",
              "5️⃣",
              "6️⃣",
              "7️⃣",
              "8️⃣",
              "9️⃣"]

@bot.command(usage=f"{bot.command_prefix}setuprolecolor", description="Creates the reaction role message for cosmetics roles", brief="owner")
@commands.is_owner()
async def setuprolecolor(ctx = None, channel = None):
    if not channel:
        channel = ctx.message.channel
    
    message_channel = bot.get_channel(channel)
    embed = discord.Embed(title="Color Roles", color=color)
    embed.add_field(name="Role", value="1️⃣ - Gold", inline=True)
    embed.add_field(name="Role", value="2️⃣ - Scarlet", inline=True)
    embed.add_field(name="Role", value="3️⃣ - Crimson", inline=True)
    embed.add_field(name="Role", value="4️⃣ - Hot Pink", inline=True)
    embed.add_field(name="Role", value="5️⃣ - Magenta", inline=True)
    embed.add_field(name="Role", value="6️⃣ - Chocolate", inline=True)
    embed.add_field(name="Role", value="7️⃣ - Aqua", inline=True)
    embed.add_field(name="Role", value="8️⃣ - Spring green", inline=True)
    embed.add_field(name="Role", value="9️⃣ - Silver", inline=True)
    msg = await message_channel.send(embed = embed)

    for emoji in emoji_list:

        await msg.add_reaction(emoji=emoji)


#image
@bot.command(usage=f"{bot.command_prefix}avatar [mention]", description="Get the PNG of a user pfp", brief="image")
async def avatar(ctx, *, user: discord.User = None):

    if user == None:
        user = ctx.message.author

    embed=discord.Embed(color=color).set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}gayav [mention]", description="make gay a user avatar", brief="image")
async def gayav(ctx, user: discord.User = None):

    if user == None:
        user = ctx.message.author

    url=f"https://some-random-api.ml/canvas/gay?avatar={user.avatar_url_as(static_format='png')}"
    embed=discord.Embed(color=color).set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}glassav [mention]", description="glass a user avatar", brief="image")
async def glassav(ctx, user: discord.User = None):

    if user == None:
        user = ctx.message.author

    url=f"https://some-random-api.ml/canvas/glass?avatar={user.avatar_url_as(static_format='png')}"
    embed=discord.Embed(color=color).set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}wasted [mention]", description="kill a user avatar", brief="image")
async def wasted(ctx, user: discord.User = None):

    if user == None:
        user = ctx.message.author

    url=f"https://some-random-api.ml/canvas/wasted?avatar={user.avatar_url_as(static_format='png')}"
    embed=discord.Embed(color=color).set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}greyscale [mention]", description="greyscale a user avatar", brief="image")
async def greyscale(ctx, user: discord.User = None):

    if user == None:
        user = ctx.message.author

    url=f"https://some-random-api.ml/canvas/greyscale?avatar={user.avatar_url_as(static_format='png')}"
    embed=discord.Embed(color=color).set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}invert [mention]", description="invert colors of a user avatar", brief="image")
async def invert(ctx, user: discord.User = None):

    if user == None:
        user = ctx.message.author

    url=f"https://some-random-api.ml/canvas/invert?avatar={user.avatar_url_as(static_format='png')}"
    embed=discord.Embed(color=color).set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}blur [mention]", description="blur a user avatar", brief="image")
async def blur(ctx, user: discord.User = None):

    if user == None:
        user = ctx.message.author

    url=f"https://some-random-api.ml/canvas/blur?avatar={user.avatar_url_as(static_format='png')}"
    embed=discord.Embed(color=color).set_image(url=url)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}screenshot [url]", description="screenshot the website page", brief="image", name="screenshot",aliases=["ss"])
async def screenshot(ctx, *, website = None):
    
    if website:

        if website.lower().startswith("https://"):
            web = website
            url = f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{website}"

        else:
            web = f"http://{website}"
            url = f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/http://{website}"

        embed=discord.Embed(description=f"`Provided URL:` {web}\n`Requested by:` {ctx.author.mention}", color=color)
        embed.set_image(url=url)
        embed.set_footer(text=f"Powered by thum.io", icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed, mention_author=False)

    else:
    
        embed = discord.Embed(title="Error!", description=f"Missing website, please provide a valid website to screenshot", color=error_color)
        await ctx.send(embed=embed)



#tools
@bot.command(usage=f"{bot.command_prefix}short [link]", description="reduce a link length with tinyurl", brief="tools")
async def short(ctx, *, link=None):

    if link:

        r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
        embed=discord.Embed(title="Success!", description=f"your link:\n{r}", color=color)
        await ctx.send(embed=embed)

    else:

        embed=discord.Embed(title="ERROR!", description="please provide a link to shorten", color=error_color)
        await ctx.send(embed=embed, delete_after=5)

@bot.command(usage=f"{bot.command_prefix}botinfo", description="get bot info", brief="tools")
async def botinfo(ctx):

    embed=discord.Embed(title=title, description=chr(173), color=color)
    embed.add_field(name="Ping:", value=f"{round(bot.latency * 1000, 1)}ms", inline=True)
    embed.add_field(name="Version", value=f"{version}", inline=True)
    embed.add_field(name="Commands", value=len(bot.commands), inline=True)
    embed.add_field(name="Prefix", value=f"{bot.command_prefix}", inline=True)
    embed.add_field(name=f"Changelog v{version}", value=f"Added:\n  - Source code ({bot.command_prefix}botinfo)\nImproved:\n  - Error handling", inline=False)
    embed.add_field(name="Source", value="[GitHub](https://github.com/just-none/CastleCraft-bot)",inline=False)
    embed.set_footer(text="Created by: Piombacciaio#2151")
    embed.set_thumbnail(url=icon)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}timer [time] (mention)", description="set a timer", brief="tools")
async def timer(ctx, time=None, user: discord.User = None):

    if time:

        try:
            seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400}
            res = int(time[:-1]) * seconds_per_unit[time[-1]]

        except:
            res = int(time)

        message = await ctx.send(f":timer: Timer for `{time}` has been set!")
        await asyncio.sleep(res)
        await message.delete()

        if user == None:
            await ctx.send(f":alarm_clock: Timer for `{time}` is over!")

        else:
            await ctx.send(f":alarm_clock: Timer for `{time}` is over! {user.mention}")
    
    else:
        embed=discord.Embed(title="ERROR!", description="Please insert a valid time to wait", color=error_color)
        await ctx.send(embed=embed, delete_after=5)

@bot.command(usage=f"{bot.command_prefix}ping", description="check the bot latency", brief="tools")
async def ping(ctx):

    embed = discord.Embed(title="Pong!", description=f"latency: {round(bot.latency * 1000, 1)}ms", color=color)
    embed.set_thumbnail(url=icon)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}lmgtfy [text]", description="search something on google", brief="tools") #To fix, invert try and if/else
async def lmgtfy(ctx, *, message=None):

    if message:

        text = urlencode({"q": message})
        embed=discord.Embed(title="here's the link:", description=f'<https://lmgtfy.com/?{text}>', color=color)
        await ctx.send(embed=embed)

    else:

        embed=discord.Embed(title="ERROR!", description="Pleas provide a valid text.", color=error_color)
        await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}mcuid [mc username]", description="get user id out of a minecraft username [JAVA Edition only]", brief="tools")
async def mcuid(ctx, mcname = None):

    if mcname:

        r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{mcname}')
        data = r.json()
        uuid = data['id']
        name = data['name']
        embed = discord.Embed(color=color, title=f'Minecraft UUID of {name}', description=f'{uuid}')
        embed.set_thumbnail(url=icon)
        await ctx.send(embed=embed)
    
    else:

        embed=discord.Embed(title="ERROR!", description="Please provide a valid minecraft username [Only for java edition]", color=error_color)
        await ctx.send(embed=embed)
 
@bot.command(usage = f"{bot.command_prefix}mcserver [ip:port]", description=f"lookup a serever's status ex. {bot.command_prefix}mcserver 127.0.0.1:25565", brief="tools")
async def mcserver(ctx, address = None):

    if address:

        r = requests.get(f'https://api.mcsrvstat.us/2/{address}')
        data = r.json()
        ip = data['ip']
        port = data['port']
        online = data['online']
            
        if online == True:

            hostname = data['hostname']
            motd1 = data['motd']['clean'][0]
            motd2 = data['motd']['clean'][1]
            max_players = data['players']['max']
            online_players = data['players']['online']
            version = data['version']
            protocol = data['protocol']
            icon = data['icon']

        embed = discord.Embed(color=color, title=f'Minecraft Server Info')
        embed.add_field(name = "IP", value = f"{str(ip)}", inline=True)
        embed.add_field(name = "Port", value = f"{str(port)}", inline=True)
        embed.add_field(name = "Online", value = f"{str(online)}", inline=True)

        if online == True:

            embed.add_field(name = "Hostname", value = f"{str(hostname)}", inline=True)
            embed.add_field(name = "Players", value = f"{str(online_players)}/{str(max_players)}", inline=True)
            embed.add_field(name = "Version", value = f"{str(version)}", inline=True)
            embed.add_field(name = "Protocol", value = f"{str(protocol)}", inline=True)
            embed.add_field(name = "MOTD", value = f"{str(motd1)}\n{str(motd2)}", inline=False)

        embed.set_thumbnail(url=f'https://api.mcsrvstat.us/icon/{address}')
        await ctx.send(embed=embed)
    
    else:

        embed=discord.Embed(title="ERROR!", description="Please provide a valid server address", color=error_color)
        await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}mcskin [mc username]", description="get user skin out of a minecraft username [JAVA Edition only]", brief="tools")
async def mcskin(ctx, mcname = None):

    if mcname:

        r = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{mcname}')
        data = r.json()
        name = data['name']
        embed = discord.Embed(color=color, title=f'Minecraft Skin of {name}')
        embed.set_image(url=f'https://minecraftskinstealer.com/api/v1/skin/render/fullbody/{name}/700')
        await ctx.send(embed=embed)

    else:

        embed=discord.Embed(title="ERROR!", description="Please provide a valid minecraft username [Only for java edition]", color=error_color)
        await ctx.send(embed=embed)



#textual
@bot.command(usage=f"{bot.command_prefix}encode [text]", description="encode text into base 64", brief="textual")
async def encode(ctx, *, text=None):

    if text:

        decoded_stuff = base64.b64encode(f'{text}'.encode('ascii'))
        encoded_stuff = str(decoded_stuff)
        encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
        embed = discord.Embed(title="Done", description=f"here's your encoded stuff:\n {encoded_stuff}", color=color)
        await ctx.send(embed=embed)

    else:

        embed = discord.Embed(title="ERROR!", description="Please provide a text to encode", color=error_color)
        await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}decode [text]", description="decode text from base 64", brief="textual")
async def decode(ctx, *, text=None):

    if text:

        strOne = text.encode("ascii")
        pad = len(strOne) % 4
        strOne += b"=" * pad
        encoded_stuff = codecs.decode(strOne.strip(), 'base64')
        decoded_stuff = str(encoded_stuff)
        decoded_stuff = decoded_stuff[2:len(decoded_stuff) - 1]
        embed = discord.Embed(title="Done", description=f"here's your decoded stuff:\n {decoded_stuff}", color=color)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="ERROR!", description="Please provide a text to decode", color=error_color)
        await ctx.send(embed=embed)

@bot.command(pass_context=True, usage=f"{bot.command_prefix}enchant [text]", description="translate a message into ᒷリᓵ⍑ᔑリℸ", brief="textual")
async def enchant(ctx, *, text: str = None):

    to_enchantmenttable = { 
        "a" : "ᔑ",
        "b" : "ʖ",
        "c" : "ᓵ",
        "d" : "↸",
        "e" : "ᒷ",
        "f" : "⎓",
        "g" : "⊣",
        "h" : "⍑",
        "i" : "╎",
        "j" : "⋮",
        "k" : "ꖌ",
        "l" : "ꖎ",
        "m" : "ᒲ",
        "n" : "リ",
        "o" : "𝙹",
        "p" : "!¡",
        "q" : "ᑑ",
        "r" : "∷",
        "s" : "ᓭ",
        "t" : "ℸ",
        "u" : "⚍",
        "v" : "⍊",
        "w" : "∴",
        "x" : " ̇/",
        "y" : "||",
        "z" : "⨅",
        "1" : "1",
        "2" : "2",
        "3" : "3",
        "4" : "4",
        "5" : "5",
        "6" : "6",
        "7" : "7",
        "8" : "8",
        "9" : "9",
        "0" : "0"}
    
    if text:

        cipher = ''
        for letter in text:

            if letter != ' ':
                cipher += to_enchantmenttable[letter.lower()]

            else:
                cipher += ' '

        await ctx.send(cipher)

    else:
        embed = discord.Embed(title="ERROR!", description="Please provide a text to encode", color=error_color)
        await ctx.send(embed=embed)



#fun
@bot.command(usage=f"{bot.command_prefix}meme", description="Send a random meme from reddit", brief="fun")
async def meme(ctx):

    result = requests.get("https://meme-api.herokuapp.com/gimme").json()
    embed=discord.Embed(title=f"subreddit: __{result['subreddit']}__", description=f"{result['title']}", color=color)
    embed.set_image(url=f"{result['url']}")
    await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}gcalc (mention)", description="Calc how much a user is gay", brief="fun")
async def gcalc(ctx, user: discord.User = None):

    if user == None:
        user = ctx.message.author

    percent = random.randint(0, 100)
    embed=discord.Embed(title="Gay Calc 2000", description=f"{user.name} is {percent}% gay", color=color)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@bot.command(aliases=['pp'], usage=f"{bot.command_prefix}ppcalc (mention)", description="Calc pp length", brief="fun")
async def ppcalc(ctx, user: discord.User = None):

    if user == None:
        user = ctx.message.author

    size = random.randint(1, 20)
    length = ""

    for segment in range(0, size):
        length += "="
        
    embed=discord.Embed(title="PPCalc 2000", description=f"{user.name}'s pp length is:\n8{length}D", color=color)
    embed.set_footer(text=footer)
    await ctx.send(embed=embed)

@bot.command(name="8ball", usage=f"{bot.command_prefix}8ball [question]", description="ask a question to the ball", brief="fun")
async def _8ball(ctx, *, question = None):

    responses = ["It is certain.",
               "It is decidedly so.",
               "Without a doubt.",
               "Yes, definitely.",
               "You may rely on it.",
               "As we see it, yes.",
               "Most likely.",
               "Outlooks good.",
               "Yes.",
               "Signs point to yes.",
               "Reply hazy, try again.",
               "Ask again later.",
               "Better not tell you now.",
               "Cannot predict now.",
               "Concentrate and ask again.",
               "Don't count on it.",
               "Our reply is no.",
               "Our sources say no.",
               "Outlook not so good.",
               "Very doubtful."]
    
    if question:

        embed = discord.Embed(title="mythological beings say", color=color, description=f'\n{random.choice(responses)}')
        await ctx.send(embed=embed)

    else:

        embed = discord.Embed(title="mythological beings say", color=color, description="What should we answer if you don't ask?")
        await ctx.send(embed=embed)

@bot.command(usage=f"{bot.command_prefix}repeat [message]", description="repeats a message", brief="fun")
async def repeat(ctx, *, message = None):

    await ctx.message.delete()

    if message:

        await ctx.channel.send(f"{message}")

    else:

        await ctx.channel.send("What should I repeat? An empty message?", delete_after=3)



#modmail
@bot.event
async def on_message(message):

    if message.author.id == bot.user.id:
        return
    
    if message.author != message.author.bot:

        if not message.guild:

            if message.content.startswith("$"):

                await bot.process_commands(message)
           
            else:
                
                em = discord.Embed(color=color)
                em.add_field(name="**Modmailing**", value=f"User: {message.author.mention} ({message.author})\nUser ID: {message.author.id}\nneeds help with: {message.content}\n\nto reply: {bot.command_prefix}reply {message.author.mention} [message]")
                await bot.get_guild(BOT_GUILD).get_channel(MODMAIL_CHANNEL).send(f"@&{MODROLE}>", delete_after=3)
                await bot.get_guild(BOT_GUILD).get_channel(MODMAIL_CHANNEL).send(embed=em)
        
        else:

            await bot.process_commands(message)

@bot.command(usage=f"{bot.command_prefix}reply [mention] [message]", description="reply to a modmail Dm", brief="admin")
@commands.has_any_role("Admin", "Staff Member")
async def reply(ctx, member:discord.Member, *, msg):
    try:

        await member.send(msg)

    except Exception as e: 

        embed = discord.Embed(title="Error!", description=f"Sorry for the inconvenient, but the following error has occourred\n`{e}`\n{ctx.message.author.mention} Please do not delete your message to allow a better understanding of the problem", color=error_color)
        await ctx.message.reply(content=f"<@!{MANAGER}> please check this", embed=embed, mention_author=False)
        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.RED + "[Error]  " + Fore.RESET + f' | The command has raised an exception: [{e}]')



#events
@bot.event
async def on_connect():

    try:

        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.GREEN + "[Event]  " + Fore.RESET + f' | {bot.user} is connected')
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game(f"{bot.command_prefix}help or Dm me for support"))

        await bot.wait_until_ready()
        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.GREEN + "[Event]  " + Fore.RESET + f' | Modmail is ready for use')
        print("" + time_ + " | " + Fore.GREEN + "[Event]  " + Fore.RESET + f' | Bot startup completed, waiting for inputs\n')

        await setuprolecolor(channel=ROLECHANNEL)

        global balances

        try:

            with open('balance.json') as f:
                balances = json.load(f)

        except FileNotFoundError:

            print("Could not load balance.json")
            balances = {}

    except Exception as e:

        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.RED + "[Error]  " + Fore.RESET + f' | Connection has raised an exception: [{e}]')

@bot.event
async def on_command(cmd):

    try:
        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.BLUE + "[Command]" + Fore.RESET + f" | {bot.command_prefix}{cmd.command.name}")

    except Exception as e:
        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.RED + "[Error]  " + Fore.RESET + f' | Command usage logging has raised an exception: [{e}]')

@bot.event
async def on_command_error(cmd, error):

    try:

        embed = discord.Embed(title="Error!", description=f"Sorry for the inconvenient, but the following error has occourred\n`{error}`\n{cmd.message.author.mention} Please do not delete your message to allow a better understanding of the problem", color=error_color)
        await cmd.message.reply(content="<@!624712494379827231> please check this. this is the v2", embed=embed, mention_author=False)
        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.RED + "[Error]  " + Fore.RESET + f' | The command {cmd.command.name} has raised the following error: [{error}]')

    except Exception as e:

        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.RED + "[Error]  " + Fore.RESET + f' | Hilarious, error logging has given an error.... Raised error: [{e}]')

@bot.event
async def on_member_join(member:discord.Member):

    try:

        guild = member.guild
        role_to_add = discord.utils.get(guild.roles, name='Members') 
        await member.add_roles(role_to_add)
        embed = discord.Embed(title="New Member!", description=f"Welcome {member.mention}!\nWe hope you will have a good time in Castle_Craft!\nIf you want, you can head to <#{ROLECHANNEL}> to customize your name's color", color=color)
        embed.set_thumbnail(url=member.avatar_url)
        await bot.get_guild(BOT_GUILD).get_channel(WELCOME_CHANNEL).send(embed=embed)

        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.GREEN + "[Event]  " + Fore.RESET + f" | {Fore.CYAN}Member Joined{Fore.RESET}: {member.name}#{member.discriminator} (ID. {member.id})")

    except Exception as e:

        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.RED + "[Error]  " + Fore.RESET + f' | "Member Join" logging has raised an exception: [{e}]')

@bot.event
async def on_member_remove(member):

    try:

        embed = discord.Embed(title="We sadly lost a member!", description=f"Goodbye {member.mention}!\nWe all wish you the best and hope to see you soon!", color=color)
        avatar = member.avatar_url
        embed.set_thumbnail(url=avatar)
        await bot.get_guild(BOT_GUILD).get_channel(WELCOME_CHANNEL).send(embed=embed)
        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.GREEN + "[Event]  " + Fore.RESET + f' | {Fore.YELLOW}Member Left{Fore.RESET}: {member.name}#{member.discriminator} (ID. {member.id})')
    
    except Exception as e:

        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.RED + "[Error]  " + Fore.RESET + f' | "Member Left" logging has raised an exception: [{e}]')
    
@bot.event
async def on_reaction_add(reaction, user):

    if user == bot.user:
        pass
        
    else:
        reaction_channel = bot.get_channel(ROLECHANNEL)
        guild = reaction.message.guild

        if reaction.message.channel.id != reaction_channel:

            pass

        try: 

            if reaction.emoji == '1️⃣':

                role_to_add = discord.utils.get(guild.roles, name='Gold')
                await user.add_roles(role_to_add)
            
            if reaction.emoji == '2️⃣':

                role_to_add = discord.utils.get(guild.roles, name='Scarlet')
                await user.add_roles(role_to_add)
            
            if reaction.emoji == '3️⃣':

                role_to_add = discord.utils.get(guild.roles, name='Crimson')
                await user.add_roles(role_to_add)
            
            if reaction.emoji == '4️⃣':

                role_to_add = discord.utils.get(guild.roles, name='Hot pink')
                await user.add_roles(role_to_add)
            
            if reaction.emoji == '5️⃣':
                
                role_to_add = discord.utils.get(guild.roles, name='Magenta')
                await user.add_roles(role_to_add)
            
            if reaction.emoji == '6️⃣':

                role_to_add = discord.utils.get(guild.roles, name='Chocolate')
                await user.add_roles(role_to_add)
            
            if reaction.emoji == '7️⃣':

                role_to_add = discord.utils.get(guild.roles, name='Aqua')
                await user.add_roles(role_to_add)
            
            if reaction.emoji == '8️⃣':

                role_to_add = discord.utils.get(guild.roles, name='Spring green')
                await user.add_roles(role_to_add)
            
            if reaction.emoji == '9️⃣':

                role_to_add = discord.utils.get(guild.roles, name='Silver')
                await user.add_roles(role_to_add)

        except Exception as e:

            time_ = datetime.datetime.now().strftime("%H:%M")
            print("" + time_ + " | " + Fore.RED + "[Error]  " + Fore.RESET + f" | An error as occourred while adding the {reaction.emoji} role: {e}")

@bot.event
async def on_reaction_remove(reaction, user):

    reaction_channel = bot.get_channel(ROLECHANNEL)
    guild = reaction.message.guild

    if reaction.message.channel.id != reaction_channel:

        pass

    try: 

        if reaction.emoji == '1️⃣':

            role_to_remove = discord.utils.get(guild.roles, name='Gold')
            await user.remove_roles(role_to_remove)
        
        if reaction.emoji == '2️⃣':

            role_to_remove = discord.utils.get(guild.roles, name='Scarlet')
            await user.remove_roles(role_to_remove)
        
        if reaction.emoji == '3️⃣':

            role_to_remove = discord.utils.get(guild.roles, name='Crimson')
            await user.remove_roles(role_to_remove)
        
        if reaction.emoji == '4️⃣':

            role_to_remove = discord.utils.get(guild.roles, name='Hot pink')
            await user.remove_roles(role_to_remove)
        
        if reaction.emoji == '5️⃣':
            
            role_to_remove = discord.utils.get(guild.roles, name='Magenta')
            await user.remove_roles(role_to_remove)
        
        if reaction.emoji == '6️⃣':

            role_to_remove = discord.utils.get(guild.roles, name='Chocolate')
            await user.remove_roles(role_to_remove)
        
        if reaction.emoji == '7️⃣':

            role_to_remove = discord.utils.get(guild.roles, name='Aqua')
            await user.remove_roles(role_to_remove)
        
        if reaction.emoji == '8️⃣':

            role_to_remove = discord.utils.get(guild.roles, name='Spring green')
            await user.remove_roles(role_to_remove)
        
        if reaction.emoji == '9️⃣':

            role_to_remove = discord.utils.get(guild.roles, name='Silver')
            await user.remove_roles(role_to_remove)

    except Exception as e:
        
        time_ = datetime.datetime.now().strftime("%H:%M")
        print("" + time_ + " | " + Fore.RED + "[Error]  " + Fore.RESET + f" | An error as occourred while adding the {reaction.emoji} role: {e}")

time_ = datetime.datetime.now().strftime("%H:%M")
user = input("" + time_ + " | " + Fore.GREEN + "[Event]  " + Fore.RESET + " | please choose between r (reboot) or c (continue): ")

if user.lower() == "c" or user.lower() == "continue":
    
    bot.run(TOKEN)

elif user.lower() == "r" or user.lower() == "reboot":

    try:

        os.system("python castlecraft.py")
        quit()

    except:
            
        os.system("cls")
        os.system("castlecraft.exe")

