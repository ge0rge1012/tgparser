# tgparser
What will you need to make the script work? 

First of all, **python 3.5+** is required.

Then you need to install the library with the command:

    'pip3 install telethon' 
    
Now you need fo fill **config.ini**:
1. In *api_id*  and *api_hash* just write values from telegram developer tools 
2. *username* can be whatever you want. It is just used to save telegram session like *username.session*. Remember, if you delete this file, you will have to log in account again. 
3. *my_channel* is the channel, where you want to redirect updates. Your account must have an opportunity to post there. 

To **channels.txt** file you need to write down a list of channel IDs whose updates need to be checked. Your bot account must be subscribed to these channels in order to receive notifications. You can find out the id of a particular channel by sending a link or any message from it to the bot *@get_id_bot*. Write each id from a new line. 

To **keywords.txt** file write the keywords in the presence of which the message should be forwarded. Each keyword must be written from a new line. All worlds in validation function are made lower_case, so there is no need to be case sensitive.

If everything is done, run the script and log in to your account by phone number. To work, the script must be executed.
