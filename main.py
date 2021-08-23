import discord
import os
from keep_alive import keep_alive
keep_alive()
client = discord.Client()
poin = 101
dic = {}

class Person :
  def __init__(self, poin):
    self.poin = poin

def helps():
  command = "need help?"
  return command

def point():
  global poin
  poin -=1
  return poin

def prints():
  output=""
  a=1;
  sort_orders = sorted(dic.items(), key=lambda x: x[1], reverse=True)
  for i in sort_orders:
    output += str(a)+". "+str(i[0]) +" "+ str(i[1])+"\n"
    a+=1
      
  return output

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('$help'):
      sendhelps = helps()
      await message.channel.send('{}'.format(sendhelps))

    elif message.content.startswith('$hello'):
     await message.channel.send('Hello {}!'.format(message.author.name))

    elif message.content.startswith('flag'):
        try:
          dic[message.author.name]
          await message.channel.send("you got " + str(dic[message.author.name]) +" point :D")
        except KeyError:
            dic[message.author.name] = point()
            await message.channel.send("you got " + str(dic[message.author.name]) +" point :D")
    
        
    elif message.content.startswith('scoreboard'):
      a=prints()
      await message.channel.send(a)
  

client.run(os.getenv('TOKEN'))

    
        
