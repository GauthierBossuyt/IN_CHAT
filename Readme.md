# IN_CHAT :rocket:
by @GauthierBossuyt

IN_CHAT is an application that converts twitch chat messages to keyboard output.
[DEMO](https://youtu.be/AeEMbmAhDR8)

## Installation (VSCode)
_Make sure you have the Python plugin installed on VSCode._

1. Install the environment and select it as your interpreter. It should be familiar to: *.\\.env\Scripts\python.exe*
2. Request an Oauth token on the following website: [Oauth Token](https://twitchapps.com/tmi/)
3. Fill in the Oauth token in the credentials.txt file (PATH: ./settings/credentials.txt).
4. Go to the main.py and start the script.

## Can I use other commands?
If you want to use something else instead of the default emotes. You can change the if statements between the lines 100 and 156 in the main.py file. Later on an extra file will be added to the settings folder to easily change commands.

## Bugs

* Messages that contain *:* will not be properly analysed.

## Planned Features

- [x] settings file to easily change Oauth token.
- [x] statistics shown within the console.
- [ ] file to easily change default commands. 

## Sources used for this code:

* [Tutorial: How to stream text from Twitch](https://www.learndatasci.com/tutorials/how-stream-text-data-twitch-sockets-python/)
* [Guide: Twitch Dev Guide for Python](https://dev.twitch.tv/docs/irc/guide)
* [Code: used for keyboard output](https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game)

