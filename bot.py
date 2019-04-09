###[| Copyright 2019- AkaRyu, Droit à l'utilisation mais aucunement à la modification, droit à le propriété intelectuelle |]###
###[| Ce produit a le droit d'être utilisé uniquement par le serveur discord de Zenadia |]###
###[| Aucun remboursement possible une fois la période d'essai de 24h passé.|]###
###[| Produit imaginé, créé et codé par AkaRyu|]###



#
#
#
#
#
#                AAA               kkkkkkkk                             RRRRRRRRRRRRRRRRR
#               A:::A              k::::::k                             R::::::::::::::::R
#              A:::::A             k::::::k                             R::::::RRRRRR:::::R
#             A:::::::A            k::::::k                             RR:::::R     R:::::R
#            A:::::::::A            k:::::k    kkkkkkk  aaaaaaaaaaaaa     R::::R     R:::::Ryyyyyyy           yyyyyyyuuuuuu    uuuuuu
#           A:::::A:::::A           k:::::k   k:::::k   a::::::::::::a    R::::R     R:::::R y:::::y         y:::::y u::::u    u::::u
#          A:::::A A:::::A          k:::::k  k:::::k    aaaaaaaaa:::::a   R::::RRRRRR:::::R   y:::::y       y:::::y  u::::u    u::::u
#         A:::::A   A:::::A         k:::::k k:::::k              a::::a   R:::::::::::::RR     y:::::y     y:::::y   u::::u    u::::u
#        A:::::A     A:::::A        k::::::k:::::k        aaaaaaa:::::a   R::::RRRRRR:::::R     y:::::y   y:::::y    u::::u    u::::u
#       A:::::AAAAAAAAA:::::A       k:::::::::::k       aa::::::::::::a   R::::R     R:::::R     y:::::y y:::::y     u::::u    u::::u
#      A:::::::::::::::::::::A      k:::::::::::k      a::::aaaa::::::a   R::::R     R:::::R      y:::::y:::::y      u::::u    u::::u
#     A:::::AAAAAAAAAAAAA:::::A     k::::::k:::::k    a::::a    a:::::a   R::::R     R:::::R       y:::::::::y       u:::::uuuu:::::u
#    A:::::A             A:::::A   k::::::k k:::::k   a::::a    a:::::a RR:::::R     R:::::R        y:::::::y        u:::::::::::::::uu
#   A:::::A               A:::::A  k::::::k  k:::::k  a:::::aaaa::::::a R::::::R     R:::::R         y:::::y          u:::::::::::::::u
#  A:::::A                 A:::::A k::::::k   k:::::k  a::::::::::aa:::aR::::::R     R:::::R        y:::::y            uu::::::::uu:::u
# AAAAAAA                   AAAAAAAkkkkkkkk    kkkkkkk  aaaaaaaaaa  aaaaRRRRRRRR     RRRRRRR       y:::::y               uuuuuuuu  uuuu
#                                                                                                 y:::::y
#                                                                                                y:::::y
#                                                                                               y:::::y
#                                                                                              y:::::y
#                                                                                             yyyyyyy
#Merci de ne pas retirer les lignes de Copyrights !!!!!!!
from random import randint
import json
import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType
import time
timecommand = 0
Client = discord.Client()
client = commands.Bot(command_prefix='z.')
token = "NTY0MDYzMzU0MzE5MjczOTg0.XKibWg.B4Be_G5cxPYE4wX_mUCiOy3zKWk"
userlock=[]
ticketauthorlist = []
ticketlist = []
channelmute=[]
antispamakaryu=[]
antispamakaryuvalue=[]
loopid="561636466543820822"
verifid="564882388870627350"
msgverifid="564882746489700352"
dejaverif=[]
admin="Permission du bot"
concour="561687383867654146"
#--------------------------Initialisation du bot---------------------------#
#--------------------------Initialisation du bot---------------------------#

async def msg_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        msg="Bon jeu sur Zenodia !"
        embed = discord.Embed(
            description=msg,
            colour=discord.Colour.blue()
        )
        embed.set_author(name="Message automatique")

        await client.send_message(client.get_channel("561636466543820822"), embed=embed)
        await asyncio.sleep(4900)
        msg = "Pensez à visiter notre boutique si vous aimez le serveur!"
        embed = discord.Embed(
            description=msg,
            colour=discord.Colour.blue()
        )
        embed.set_author(name="Message automatique")

        await client.send_message(client.get_channel("561636466543820822"), embed=embed)
        await asyncio.sleep(4900)



async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed:
        del antispamakaryu[:]
        del antispamakaryuvalue[:]

        await asyncio.sleep(8)






@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Zenadia->z.aide'))
    print("Bot ready")


def is_empty(any_structure):
    if any_structure:
        print('Structure is not empty.')
        return False
    else:
        print('Structure is empty.')
        return True



def is_number(s):
    try:
        float(s)
    except ValueError:
        try:
            complex(s) # for complex
        except ValueError:
            return False

    return True


@client.command(pass_context=True)
async def info(ctx):
    online=0
    for e in ctx.message.server.members:
        if e.status!=discord.Status.offline:
            online+=1
    total=0
    for e in ctx.message.server.members:
        total+=1
    aide = """**Info sur __Zenadia__**:
    **Lien du site:** *http://zenadia.fr/maintenance*
    **Joueurs en ligne**:*{}*
    **Nombres de joueurs sur le serveur**:*{}*
    **TeamSpeak:** *Tu me diras ce que je mets*
    __**Staff du serveur**__
    **Fondateur**:__XeTrOS__
    **Fondateur**:__King Noctis__
    **Développeur**:__Ts3hostinger__
    **Développeur**:__Pingouin 2 combat__
    **Développeur**:__Lidras__
    **Développeur**:__Turn Bass__
    **Administrateur**:__Lidras__
    **Administrateur**:__TheGameurZeph__
    **Modérateur**:__Felix15__
    **Modérateur**:__Keyzo__
    **Buildeurs**:__EvanPvP__ / __Weez Sweez__ / Oméga Thauwne
    **Helpeurs**:__Akayto__ / __Matteo__
    
    *Bot Créé par* **__AkaRyu#1962__**
    """.format(online,total)
    timecommand = 0
    user = ctx.message.author
    embed = discord.Embed(
        description=aide,
        colour=discord.Colour.blue()
    )
    embed.set_author(name=user.display_name, icon_url=user.avatar_url)

    await client.send_message(ctx.message.channel, embed=embed)
    await client.send_message(ctx.message.author, embed=embed)





@client.command(pass_context=True)
async def addticket(ctx, *, msg=''):
    timecommand = 0
    author = ctx.message.author.id
    user = ctx.message.author
    message = msg,
    if author in ticketauthorlist:
        messagefail = await client.send_message(ctx.message.channel, "Vous avez déjà un ticket en attente")
        await asyncio.sleep(3)
        client.delete_message(messagefail)
    else:
     embed = discord.Embed(
         description=("{} Numéro de ticket: {}".format(msg, len(ticketlist) + 1)),
         colour=discord.Colour.blue()
     )
     embed.set_author(name=user.display_name, icon_url=user.avatar_url)
     message1 = await client.say(embed=embed)
     ticketauthorlist.append(author)
     ticketlist.append("Ticket de : <@{}>   Message :   {} Numéro:   {}".format(author, msg, len(ticketlist)))
     await client.send_message(ctx.message.channel,"<@{}> Votre ticket est le numéro {}".format(author, len(ticketlist)))


@client.command(pass_context=True)
@commands.has_role(admin)
async def showtickets(ctx):
    timecommand = 0
    author = ctx.message.author.id
    await client.send_message(ctx.message.channel, ticketlist)




@client.command(pass_context=True)
@commands.has_role(admin)
async def nextticket(ctx):
    timecommand = 0
    author = ctx.message.author.id
    await client.send_message(ctx.message.channel, ticketlist[0])



@client.command(pass_context=True)
@commands.has_role(admin)
async def ticketvalide(ctx):
    timecommand = 0
    author = ctx.message.author.id
    del ticketlist[0]
    del ticketauthorlist[0]
    await client.send_message(ctx.message.channel, "<@{}> vient de valider un ticket !".format(author))

@client.command(pass_context=True)
async def aide(ctx):
    aide = """**Bienvenue sur la page d'aide de __Zenadia__**:
    **|-----Partie Joueur-----|**
    z.addticket -> z.addticket Votre problème -> Permet de créer un ticket afin d'être aidé par le staff.
    z.msgtemp -> z.msgtemps [Durée, nombre entier en seconde] Votre message ->Créé un message supprimé après  le temps indiqué.
    z.aide -> Affiche ce message.
    **|-----Partie Staff-----|**
    z.showtickets -> Affiche la liste des tickets
    z.nextticket -> Affiche le dernier ticket de la liste
    z.ticketvalide -> Supprime le dernier ticket de la liste
    z.clear x -> Supprime x messages.
    z.showblockusers -> Affiche les personnes bloqués
    z.block @Personne#xxxx->Bloque une personne
    z.unblock @Personne#xxxx->Debloque une personne
    z.spam -> Bloque un channel.
    z.spamstop -> Débloque un channel.
    z.giveaway durée(nombre à virgule, 1=1heure) nombres de gagnants(entier) Gain
    z.kickplayer @Personne#xxxx -> Kick la personne en question. 
    z.ban @Personne#xxxx x -> Ban la personne en question pour x jours
    z.sondage durée(nombre à virgule, 1=1heure) message
    """
    timecommand = 0
    user = ctx.message.author
    embed = discord.Embed(
        description=aide,
        colour=discord.Colour.blue()
    )
    embed.set_author(name=user.display_name, icon_url=user.avatar_url)
    await client.send_message(ctx.message.author, embed=embed)

@client.command(pass_context=True)
@commands.has_role(admin)
async def clear(ctx, amount=1):
    timecommand = 0
    userID = ctx.message.author.id
    channel = ctx.message.channel
    messages = []

    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("Messages effacés.")




@client.command(pass_context=True)
@commands.has_role(admin)
async def showblockusers(ctx):
    timecommand = 0
    author = ctx.message.author.id
    await client.send_message(ctx.message.channel, userlock)


@client.command(pass_context=True)
@commands.has_role(admin)
async def block(ctx):
    timecommand = 0
    user = ctx.message.mentions[0].id
    userlock.append(user)


@client.command(pass_context=True)
@commands.has_role(admin)
async def unblock(ctx):
    timecommand = 0
    if ctx.message.author.id in userlock:
        client.say(ctx.message.channel, "*Vous ne pouvez pas vous unlock tout seul")
    else:
        user = ctx.message.mentions[0].id
        userlock.remove(user)


@client.command(pass_context=True)
async def msgtemp(ctx, int1 : int, *, msg=''):
    if ctx.message.author.id in userlock:
        return
    if ctx.message.channel.id in channelmute:
        return
    timecommand = 0
    user = ctx.message.author
    message = ctx.message

    await client.delete_message(message)
    embed = discord.Embed(
        description = msg,
        colour = discord.Colour.blue()
    )
    embed.set_author(name=user.display_name, icon_url=user.avatar_url)
    message1 = await client.say(embed=embed)
    await asyncio.sleep(int1)
    await client.delete_message(message1)
    print("Delete by {} ".format(ctx.message.author.id))

@client.command(pass_context = True)
@commands.has_role(admin)
async def spam(ctx):
    await client.say("Ce channel est désormais fermé !")
    if not ctx.message.channel.id in channelmute:
        channelmute.append(ctx.message.channel.id)


@client.command(pass_context = True)
@commands.has_role(admin)
async def spamstop(ctx):
    await client.say("Ce channel est désormais ré-ouvert!")
    if ctx.message.channel.id in channelmute:
        channelmute.remove(ctx.message.channel.id)


@client.command(pass_context = True)
@commands.has_role(admin)
async def sondage(ctx,duree:float,*,message : str):
    msg="**SONDAGE**: {}".format(message)
    embed = discord.Embed(
        description=msg,
        colour=discord.Colour.blue()
    )
    embed.set_author(name="Sondage")
    msgnew = await client.send_message(client.get_channel("561688444980690984"), embed=embed)

    await client.add_reaction(msgnew, emoji='👌')
    await client.add_reaction(msgnew, emoji='⛔')
    cache_msg = discord.utils.get(client.messages, id=msgnew.id)
    await asyncio.sleep(duree * 3600)
    actuel=1
    pour=0
    contre=0
    for reactor in cache_msg.reactions:
        reactors = await client.get_reaction_users(reactor)
        for member in reactors:
            if member.id !="564063354319273984":
                if actuel==1:
                    pour+=1
                else:
                    contre+=1
        actuel+=1

    if pour>contre:
        msg="Le sondage a été accepté! : {} ".format(message)
    elif contre>pour:
        msg="Le sondage a été refusé! : {}".format(message)
    else:
        msg="Le sondage a fait égalité ! : {}".format(message)

    embed = discord.Embed(
        description=msg,
        colour=discord.Colour.gold()
    )
    embed.set_author(name="Sondage terminé.")
    await client.edit_message(msgnew, embed=embed)



@client.command(pass_context = True)
@commands.has_role(admin)
async def giveaway(ctx,duree : float,gagnant:int, *,gain : str):
    msg="**GIVEAWAY ACTIF:** Proposé par : {}, temps d'activité: {}, nombre de gagnants : {}".format(ctx.message.author,duree,gagnant)
    embed = discord.Embed(
        description=msg,
        colour=discord.Colour.red()
    )
    embed.set_author(name="GIVEAWAY : {}".format(gain))
    msgnew=await client.send_message(client.get_channel(concour), embed=embed)
    await client.add_reaction(msgnew, emoji='👊')
    await asyncio.sleep(duree*3600)
    listeparticipant=[]
    gagnants=[]
    cache_msg = discord.utils.get(client.messages, id=msgnew.id)
    for reactor in cache_msg.reactions:
        reactors = await client.get_reaction_users(reactor)
        for member in reactors:
            if member.id !="564063354319273984":
                listeparticipant.append(member.id)
    a=0
    while a<gagnant:
        if len(listeparticipant)>1:
            resultat = randint(0, len(listeparticipant) - 1)
            gagnants.append(listeparticipant[resultat])
            a += 1

        else:
            gagnants.append(listeparticipant[0])
            a += 1
    msg="Les gagnants sont : "
    for e in gagnants:
        msg+="<@{}> ".format(e)
    msg+="\n **Vous remportez {} que vous donnera <@{}>".format(gain,ctx.message.author.id)
    embed = discord.Embed(
        description=msg,
        colour=discord.Colour.gold()
    )
    embed.set_author(name="GIVEAWAY FINI".format(gain))
    await client.edit_message(msgnew,embed=embed)







@client.command(pass_context=True)
@commands.has_role(admin)
async def kickplayer(ctx):
    timecommand = 0
    user = ctx.message.mentions[0]
    await client.kick(user)

@client.command(pass_context=True)
@commands.has_role(admin)
async def banplayer(ctx, days : int=1):
    timecommand = 0
    user = ctx.message.mentions[0]
    await client.ban(user, days)



@client.event
async def on_ready():
    Channel = client.get_channel("561662797876953110")
    Text= "Ajoute la réaction 👊 pour avoir le rôle vérifié"
    Moji = await client.send_message(Channel, Text)
    await client.add_reaction(Moji, emoji='👊')
@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.channel.id != verifid:
        return
    if reaction.emoji == "👊":
        if user.id !="564063354319273984":
            Role = discord.utils.get(user.server.roles, name="Vérifié")
            await client.add_roles(user, Role)
            await client.send_message(user, "Vous avez reçu le grade vérifié ! Bienvenue dans Zénadia")








@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author.id in userlock:
        await client.delete_message(message)
    elif message.channel.id in channelmute:
        await client.delete_message(message)
        await client.send_message(message.author, "Ce channel est fermé !")
    else:
        if message.author.id in antispamakaryu:
            index=antispamakaryu.index(message.author.id)
            antispamakaryuvalue[index]+=1
            print(antispamakaryuvalue[index])
            if antispamakaryuvalue[index]>12:
                userlock.append(message.author.id)
                await client.send_message(message.author,"Vous avez été mute 1heure pour spam, vous pouvez vous plaindre en vocal cependant.")
                await asyncio.sleep(3600)
                userlock.remove(message.author.id)
        else:
            antispamakaryu.append(message.author.id)
            antispamakaryuvalue.append(1)




@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await client.send_message(member, "Bienvenue sur __**Zenadia!**__")
    embed = discord.Embed(
        description="Nous pouvons souhaiter la bienvenue à {}".format(member.name),
        colour=discord.Colour.gold()
    )
    embed.set_author(name="Bienvenue !")
    await client.send_message(client.get_channel("565254274343501825"),embed=embed)

#-Fin du code, lancement-#
client.loop.create_task(my_background_task())
client.loop.create_task(msg_loop())
client.run(token)
