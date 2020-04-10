Discord Channel Commander Bot
=============================
Many large FPS and MMO groups use a Channel Commander (CC) or whisper function
to communicate between squads in game. Most gaming VOIP tools have a CC or
whisper function. Except Discord. So this bot adds CC functionality (sort of).

You will need ONE (1) CC bot per user in CC and a channel for all the CC bots
(and only the CC bots) to sit in. The bot **_MUST_** be run locally on the
computer of the person who wants to be in CC.

Installation
------------
This bot runs on Python. It works on Python 3.6 but Python 3.5.3 or better
should work. If you need Python, [Anaconda](https://www.anaconda.com/download/)
is an easy way to get it for Windows, Mac and Linux.

For Windows specifically, it may be easier to get python from the
[Microsoft Store](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l?activetab=pivot:overviewtab).
You may also need Microsoft Visual C++ 14.0, which can be found with
[Microsoft Visual C++ Build Tools](https://visualstudio.microsoft.com/downloads/)
or with this
[Direct Download Link](https://aka.ms/vs/16/release/vs_buildtools.exe).

Once you have Python, download or clone this repository.

You'll also need the Discord Python API. The origional is avaliable via pip or
[GitHub](https://github.com/Rapptz/discord.py) but this bot needs some features
that are in a pull request of the rewite but not merged and the pull request is
behind the branch. So I forked discord.py and added the changes. You will need
to download that from 
[my GitHub](https://github.com/adocilesloth/discord.py/tree/rewrite). Credit to
[Bottersnike](https://github.com/Bottersnike) for the edits.

Once downloaded, drop the discord folder (the one inside the folder you download)
into the same folder as channel_commander.py. For some reason, installing the
library seems to break things but using it like this doesn't. Your
channel-commander folder should look like this:

```
discord (folder)
cc_audio.py
channel_commander.py
channel_commander.txt
...
```

You will need to install some Python packages: *aiohttp*, *websockets*, *pyaudio*
and *keyboard*. You can use **pip** to install these. *pyaudio* also need
*portaudio*

**Windows**

* Open the start menu, type **cmd** and click on "Command Prompt".
* Change directory to where you have downloaded the bot by typing
**cd C:\path\to\bot**
* If you installed Anaconda, type **conda install portaudio** and hit ENTER
* If you did not install Anaconda, you will have to build *portaudio* from
source (sorry). Instructions are on
[portaudio's webpages](http://portaudio.com/docs/v19-doxydocs/tutorial_start.html)
* Type **pip install -r requirements.txt** and hit ENTER

**MAC**

* Open the launchpad, type **terminal** and click on "Terminal".
* Change directory to where you have downloaded the bot by typeing
**cd /path/to/bot**
* If you installed Anaconda, type **conda install portaudio** and hit ENTER
* If you did not install Anaconda but have Homebrew, type
**brew install portaudio** and hit ENTER.
* If you don't have Anaconda or homebrew, type
**/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"**
and hit ENTER to install homebrew. Then type **brew install portaudio** and
hit ENTER.
* Type **pip install -r requirements.txt** and hit ENTER

**Linux**

* Open the launchpad, type **terminal** and click on "Terminal".
* Change directory to where you have downloaded the bot by typeing
**cd /path/to/bot**
* If you installed Anaconda, type **conda install portaudio** and hit ENTER
* If you did not install Anaconda, type **sudo apt install portaudio19-dev** and
hit ENTER.
* Type **pip install -r requirements.txt** and hit ENTER

Setting Up
----------
The settings you will need to finalise are in *channel_commander.txt*. It has
four values **TOKEN**, **cc_name**, **cc_channel**, **cc_key**.

* **cc_name** (I'll get back to **TOKEN**): The name that you use in the server
you want to use the bot in. This allows only you to control the bot.

* **cc_channel**: The name of the channel you will be using for CC. This channel
is where all the CC bots will sit and talk to each other.

* **cc_key**: Hot key for talking over CC. I think only keyboard keys will work.
Using mouse keys is something I should look into at some point.

* **TOKEN** (I said I'd get back to it): This is the unique token for your bot.
Get if from your bot's page on
[Discord's Applications](https://discordapp.com/developers/applications/). If
you don't have a bot, or forgot how to find its token, see below.

Getting a Bot Token
-------------------
If you need a bot, follow this:
1. Go to
[Discord's Applications](https://discordapp.com/developers/applications/) page
and click on "Create Application". This will, as the name suggests, create an
application that can use Discord's API. Give it a name and a nice avatar.
2. Click on "Bot" and then "Add Bot"
3. Click on "Copy" under "Token" to copy your token and paste it into the
**TOKEN** field in *channel_commander.txt*

Getting CC Bot into your server
-------------------------------
The CC bot is only useful if it's in a server. You'll need to get an invite
link to invite it. This is generated in the OAuth2 tab of your bot's page on
[Discord's Applications](https://discordapp.com/developers/applications/).
In the "Scopes" area, check "bot" and copy the generated link. If you own or
are an admin on your server, paste the link into your browser and invite the
bot. If you aren't, send the link to someone who is.

Using CC Bot
------------
Now you've installed everything, updated *channel_commander.txt* and got the
bot onto your server, it's time to use it!

To run the bot, open a command prompt/terminal. For Windows, open the start
menu, type **cmd** and click on "Command Prompt". For Mac and Linux, open the
terminal. Change directory to where you have downloaded the bot by typing
**cd C:\path\to\bot** in Windows or **cd /path/to/bot** in Mac or Linux. Then
type **python channel_commander.py** and hit ENTER.

If all goes well, after a moment the command prompt/terminal should now read:
```
client.user.name <Name_of_Bot>
client.user.id <some numbers>
Owned by <cc_name>
Audio input at 48000Hz with 2 channels
Audio output at 48000Hz with 2 channels
```
If it doesn't something has gone wrong. Try it all again maybe? I dunno...

Once it's running, there are only a couple of commands. These are typed into
any of the channels of the server the bot is in and they all start with **!cc**

* **!cc help**: Shows the help list incase you forget anything
* **!cc rename new_name**: Changes CC bot's nickname to new_name
* **!cc shutdown**: Shuts down CC bot
* **!cc start**: Connects CC bot to cc_channel so it/you can speak and hear CC
* **!cc stop**: Disconnects CC bot from cc_channel. May cause the bot to crash
and I don't know why (yet).

That's it. Get to it and rule the battlefield with your chums!
