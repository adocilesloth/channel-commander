import discord
import cc_audio
import pyaudio
import time

#Discord Info
#TODO - Set this to pull from a config file
#TOKEN = 'NTE5MjIwMDc3OTgwMjg2OTg4.DucLCA.qx2zlHGoypsMuGUELh_tnL5JzRY'
#cc_id = '0'
#cc_channel = 'Channel Commander'
#cc_key = 'alt'

with open('channel_commander.txt', "r") as cc_txt:
	lines = cc_txt.readlines()
cc_txt.close()

TOKEN = lines[0][6:].strip()
cc_id = lines[1][6:].strip()
cc_channel = lines[2][11:].strip()
cc_key = lines[3][7:].strip()

#Placeholders
voice = None        #Voice stream
audio_in = None     #Audio in

#Make client
client = discord.Client()

#Audio Out Stuff
CHANNELS = 2
RATE = 48000
pAudio = pyaudio.PyAudio()
stream = pAudio.open(format=pyaudio.paInt16,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    input=False)

@client.event
async def on_message(message):
    global voice
    global audio_in
    global stream
    global pAudio
    if message.author == client.user:
        #Ignore own messages
        return
        
    elif message.content == '!cc help':
        #Print help, only for even numbered bots to prevent too much spam
        if int(cc_id)%2 == 0:
            msg = "Channel Commander Functions:\n";
            msg += "\t!cc help\t\t\t\t\t\t\t\t- Shows this help list\n";
            msg += "\t!cc list ids\t\t\t\t\t\t\t- Shows CC id #\n";
            msg += "\t!cc rename # new_name - Renames CC # to new_name\n";
            msg += "\t!cc shutdown #\t\t\t\t  - Shuts down CC #\n";
            msg += "\t!cc start #\t\t\t\t\t\t\t- Connect # to CC voice channel\n";
            msg += "\t!cc stop #\t\t\t\t\t\t\t- Disconnect # from CC voice channel\n";
            await message.channel.send(msg)
            
    elif message.content == '!cc list ids':
        #Print Channel Commander cc_id
        await message.channel.send("#="+cc_id)
        
    elif message.content.startswith('!cc rename'):
        #Change nickname of the Channel Commander
        if message.content[11:11+len(cc_id)] == cc_id:
            new_name = message.content[12+len(cc_id):]
            me = message.guild.me
            await me.edit(nick=new_name)
    
    elif message.content.startswith('!cc shutdown'):
        #Shuts down Channel Commander
        if message.content[-len(cc_id):] == cc_id:
            audio_in.shutdown()
            stream.close()
            pAudio.terminate()
            await client.logout()
            
    elif message.content.startswith('!cc start'):
        #Connect to Channel Commander voice channel
        if message.content[-len(cc_id):] == cc_id:
            if voice is None:
                channel = discord.utils.get(message.guild.channels, name=cc_channel)#,
                if channel is None:
                    message.channel.send(cc_channel+" does not exist")
                voice = await discord.VoiceChannel.connect(channel)
                audio_in.get_voice(voice)
                audio_in.set_in_channel(True)
            else:
                msg = "CC "+cc_id+" is already started!"
                await message.channel.send(msg)
                
    elif message.content.startswith('!cc stop'):
        #Disconnect from Channel Commander voice channel
        if message.content[-len(cc_id):] == cc_id:
            if voice is None:
                msg = "CC "+cc_id+" is not started!"
                await message.channel.send(msg)
            else:
                audio_in.get_voice(None)
                audio_in.set_in_channel(False)
                await voice.disconnect(force=True)
                voice = None
        
    return

@client.event
async def on_pcm_data_receive(voice_client, voice_packet):
    #Get data from voice channel and output it to speakers
    global stream
    stream.write(voice_packet.pcm)

@client.event
async def on_ready():
    print('client.user.name', client.user.name)
    print('client.user.id', client.user.id)
    global audio_in
    audio_in = cc_audio.audio_input(cc_key)
    print("Audio output at {0}Hz with {1} channels".format(RATE, CHANNELS))
    
client.run(TOKEN)

