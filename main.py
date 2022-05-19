import discord
import os
from keep_alive import keep_alive
import random
import asyncio
import re


keep_alive()
client = discord.Client()
prefix = "$"
flags = "WPCSC{"

dic = {}
dicti={}



class Person :
  def __init__(self, poin,name):
    self.name = name
    self.poin = poin



def helps():
  command = ["Need help?","You alr know what to do :/","I can't do anything :D","I love you <3","Have you submitted the flag?","Is the instruction from Line not clear enough?","I'm not the murderer, I promise! D:","UwU","I'm bored..","OwO","What?"]
  return random.choice(command)



def point(a):
  poins =0
  for guil in client.guilds:
    if a==guil.id:
      dicti[guil.id] -=1
      poins = dicti[guil.id]
      break
  return poins
  
    

def prints(ids):
  output="```Scoreboard : \n"
  a=1;
  sort_orders = sorted(dic[ids].items(), key=lambda x: x[1], reverse=True)
  for i in sort_orders:
    output += str(a)+". "+str(i[0]) +" "+ str(i[1])+"\n"
    a+=1
  output += "```"
  return output

def p(names):
  # names = "Welcoming Party"
  file = open(names+".txt", 'r')
  output="```Scoreboard : \n"
  i = 1;
  for each in file:
    output +=str(i)+"."+ each 
    i+=1;
  output+="```"
  return output
  

from discord.ext import commands
bot = commands.Bot(command_prefix='$')


async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for message in ctx.history():
      mgs.append(message)
    await client.delete_messages(mgs)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for guild in client.guilds:
        dic[guild.id]={}
        dicti[guild.id]=501
        
    

@client.event
async def on_message(message):
    # channel = discord.utils.get(message.guild.channels, name="scoreboard")
    # channel_id = channel.id
    if message.author == client.user:
        return
    if (message.content.startswith(prefix)):
      if ( message.content.split(prefix)[1].lower()=='tes'):
        await message.channel.send(str(dic[message.guild.id]))

      elif  ( message.content.split(prefix)[1].lower()=='help'):
        sendhelps = helps()
        await message.channel.send('{}'.format(sendhelps))

      elif   message.content.split(prefix)[1].lower()=='hello':
         await message.channel.send('Hello {}!'.format(message.author.name))

      # elif  message.channel.id== channel_id and  message.content.split(prefix)[1].lower()=='scoreboard':
      #     # a=prints(message.guild.id)
      #     a=p(message.guild.name)
      #     await message.channel.send(a)
      
      elif  message.content.split(prefix)[1].lower()=='me':
        await message.channel.send("```Name : "+ message.author.name +"\nID: " + str(message.author.id)+"```")
      
      elif  message.content.split(prefix)[1].lower()=='socmed':
        await message.channel.send("Want to know more about us? visit us on : \nhttps://linktr.ee/cybersecuritycommunity/")
      
      elif  message.content.split(prefix)[1].lower() =='command':
        embedVar = discord.Embed(title="I am a bot", description="Hi! you found me!", color=0x00ff00)
        embedVar.add_field(name="Prefix ($)", value="$ (prefix is used on start of every command except submitting flag)", inline=False)
        embedVar.add_field(name="Flag", value="The Flag format is WPCSC{flag}, and submit it in the \"submit-flag\" channel", inline=False)
        embedVar.add_field(name="Hello", value="Hello {name}!", inline=False)
        embedVar.add_field(name="Help", value="Doesn't really give helps ._. but give it a try :D", inline=False)
        embedVar.add_field(name="Me", value="Give back your username and User ID", inline=False)
        embedVar.add_field(name="clear <number>", value="Clear <number> of message", inline=False)
        embedVar.add_field(name="Socmed", value="https://linktr.ee/cybersecuritycommunity", inline=False)
        embedVar.set_image(url='https://i.ibb.co/tJDR2Dg/Banner-CSC.jpg')
        embedVar.set_footer(text="Hack Passionately, Act Righteously!")
        await message.channel.send(embed=embedVar)
      
      elif  message.content.split()[0].lower() =='$clear' and message.content.split()[1]!=None:
        # await message.channel.send("tes")
        # await clear(message,int (message.content.split()[1]))
        deleted = await message.channel.purge(limit=int(message.content.split()[1]))
        msg = await message.channel.send('Deleted {} message(s)'.format(len(deleted)))
        await asyncio.sleep(1)
        await msg.delete()
        

    channel = discord.utils.get(message.guild.channels, name="submit-flag")
    channel_id = channel.id

    if message.content.startswith(flags):
      await message.delete()
      if message.channel.id== channel_id: 
        if message.content.split(flags)[1]=='d0-Y0u-knOw-h0W-h3-ki11led-H3r?}':
          try:
            dic[message.guild.id][message.author.name]
            # await message.channel.send("you already got " + str(dic[message.guild.id][message.author.name]) +" point >:(")
            await message.channel.send("You think it's Angger, Detective <@"+str(message.author.id)+">?")
          except KeyError:
              dic[message.guild.id][message.author.name] = point(message.guild.id)
              a = message.guild.name
              f = open('%s.txt' % a, 'a')

              f.write( message.author.display_name+ " "+message.author.name+"#" + message.author.discriminator + " " + str(dic[message.guild.id][message.author.name])+"\n")
              # await message.channel.send("you got " + str(dic[message.guild.id][message.author.name]) +" point :D")
              await message.channel.send("You think it's Angger, Detective <@"+str(message.author.id)+">?")
        elif  message.content.split(flags)[1]=='Y0u-th1inK-it5-A-4u1C1de?}':
            await message.channel.send("You think it's Kelly, Detective <@"+str(message.author.id)+">?")
        elif  message.content.split(flags)[1]=='h3-1s-sUsp1ciOus-1nd33d}':
            await message.channel.send("You think it's Neil, Detective <@"+str(message.author.id)+">?")
        elif  message.content.split(flags)[1]=='1t5-n0t-R0m3o-i5nT-iT?}':
            await message.channel.send("You think it's Reynard, Detective <@"+str(message.author.id)+">?")
        elif  message.content.split(flags)[1]=='4re-Th3Y-3ven-fR13nds?}':
            await message.channel.send("You think it's Jesslyn, Detective <@"+str(message.author.id)+">?")
                    
      else:
        await message.channel.send("Hai, jangan disini ya submitnya :)")

     
client.run(os.getenv('TOKEN'))

    
        
