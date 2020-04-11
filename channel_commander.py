import discord
import cc_audio
import pyaudio
import time

#Discord Info
with open('channel_commander.txt', "r") as cc_txt:
    lines = cc_txt.readlines()
cc_txt.close()

TOKEN = lines[0][6:].strip()
cc_name = lines[1][8:].strip()
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

    elif message.author.display_name != cc_name:
        #Ignore anything not from owner
        return

    elif message.content == '!cc help':
        #Print help
        msg = "Channel Commander Functions:\n"
        msg += "\t!cc help\t\t\t\t\t\t\t- Shows this help list\n"
        msg += "\t!cc rename new_name - Renames CC bot to new_name\n"
        msg += "\t!cc shutdown\t\t\t\t  - Shuts down CC bot\n"
        msg += "\t!cc start\t\t\t\t\t\t\t- Connect to CC voice channel\n"
        msg += "\t!cc stop\t\t\t\t\t\t\t- Disconnect from CC voice channel\n"
        await message.channel.send(msg)

    elif message.content.startswith('!cc rename'):
        #Change nickname of the Channel Commander
        new_name = message.content[11:]
        me = message.guild.me
        await me.edit(nick=new_name)

    elif message.content == '!cc shutdown':
        #Shuts down Channel Commander
        audio_in.shutdown()
        stream.close()
        pAudio.terminate()
        await client.logout()

    elif message.content == '!cc start':
        #Connect to Channel Commander voice channel
        if voice is None:
            channel = discord.utils.get(message.guild.channels, name=cc_channel)#,
            if channel is None:
                message.channel.send(cc_channel+" does not exist")
            voice = await discord.VoiceChannel.connect(channel)
            audio_in.get_voice(voice)
            audio_in.set_in_channel(True)
        else:
            msg = "CC for "+cc_name+" is already started!"
            await message.channel.send(msg)

    elif message.content == '!cc stop':
        #Disconnect from Channel Commander voice channel
        if voice is None:
            msg = "CC for "+cc_name+" is not started!"
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
    print('Owned by', cc_name)
    global audio_in
    audio_in = cc_audio.audio_input(cc_key)
    print("Audio output at {0}Hz with {1} channels".format(RATE, CHANNELS))

client.run(TOKEN)

