import discord
import asyncio

client = discord.Client()
qDetect = False
willMemeDetect = False

#ID of user who is spamming
userID = 'User ID here'
dynoID = 'Dyno ID here'

version = '1.1'

def fileRead():
    file = open('/home/pi/jackwrangler/counter.txt','r')
    counter = int(file.read())
    file.close()
    return counter

def fileWrite(str):
    file = open('/home/pi/jackwrangler/counter.txt','w')
    file.write(str)
    file.close
    return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global qDetect
    global willMemeDetect
    global userID
    global dynoID
    

    if message.content.startswith('!help'):
        counter = fileRead()
        helpMessage = "I'm here to personally tard wrangle Jack Wright-Smith." + "\n\n" + "Jack has been wrangled {} times!".format(counter) + "\n\n" + "Bot Version: " + version
        await client.send_message(message.channel, helpMessage)
#Prevent Jack from q spamming
    elif message.content.startswith('?q') and message.author.id == userID:
        qDetect = True
        await client.delete_message(message)
        counter = fileRead()
        counter += 1
        #await client.send_message(message.channel, "{}".format(counter))
        fileWrite(str(counter))
#Prevent Jack from spamming Will meme
    elif message.content.startswith('?whydidthishappen'):
        if message.author.id == userID:
            willMemeDetect = True
            await client.delete_message(message)
            counter = fileRead()
            counter = counter + 1
            fileWrite(str(counter))
        else:
            await client.send_message(message.channel, "Because of Will")

#Delete Dyno Messages
    if message.author.id == dynoID and qDetect == True:
        await client.delete_message(message)
        qDetect = False

    if message.author.id == dynoID and willMemeDetect == True:
        await client.delete_message(message)
        willMemeDetect = False
    
	
client.run('BOT token here')
