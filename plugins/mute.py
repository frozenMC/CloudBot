# mute plugin by lukeroge and neersighted
from util import hook

def mute_chan(chan, db):
    db.execute("insert or replace into mute(channel, activated) values(?, ?)", (chan, 1))
    db.commit()

def unmute_chan(chan, db):
    db.execute("create table if not exists mute(channel, activated)")
    db.execute("insert or replace into mute(channel, activated) values(?, ?)", (chan, 0))
    db.commit()

def is_muted(chan, db):
    indb = db.execute("select activated from mute where channel=lower(?)", [chan]).fetchone();
    if indb == 0:
        if activated == 1:
            return True
        else:
            return False
    else:
        db.execute("insert or replace into mute(channel, activated) values(?, ?)", (chan, "0"))
        db.commit()
        return False

@hook.sieve
def mutesieve(bot, input, func, type, args):
    print "sieve fired" 
    db = bot.get_db_connection(input.conn)
    db.execute("create table if not exists mute(channel, activated)")
#    if type == "event":
#       print "type: event, dying"
#       return input
    if is_muted(input.chan, db):
        print "is_muted success"
        if input.command == "PRIVMSG" and input.lastparam[1:] == "unmute":
            return "debug: unmuted"
#           return input
        else:
            return "debug: muted"
#           return None
    return input

@hook.command(autohelp=False)
def mute(inp, input=None, db=None):
    ".mute <channel> -- Mutes the bot in <channel>. If no channel is specified, it is muted in the current channel."
    if inp:
        channel = inp
    else:
        channel = input.chan
        
    if input.nick not in input.bot.config["admins"]:
        input.notice("Only bot admins can use this command!")
        return
    else:
        if is_muted(channel, db):
            input.notice("Already Muted")
        else:
           mute_chan(channel, db)
           input.notice("Muted")

@hook.command(autohelp=False)
def unmute(inp, input=None, db=None):
    ".unmute <channel> -- Unmutes the bot in <channel>. If no channel is specified, it is unmuted in the current channel."
    if inp:
        channel = inp
    else:
        channel = input.chan
        
    if input.nick not in input.bot.config["admins"]:
        input.notice("Only bot admins can use this command!")
        return
    else:
        if is_muted(channel, db):
           unmute_chan(channel, db)
           input.notice("Unuted")
        else:
           input.notice("Not Muted")
