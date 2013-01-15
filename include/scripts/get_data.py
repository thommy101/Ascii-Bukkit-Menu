#!/usr/bin/env python2

from minecraft_query import MinecraftQuery

query = MinecraftQuery("localhost", 25565)
data = query.get_rules()

string =str((data['map']))+"|"
string +=str((data['motd']))+"|"
string +=str((data['hostport']))+"|"
string +=str((data['numplayers']))+"|"
string +=str((data['gametype']))+"|"
string +=str((data['players']))+"|"
string +=str((data['version']))+"|"
string +=str((data['maxplayers']))+"|"
string +=str((data['plugins']))+"|"
string +=str((data['raw_plugins']))+"|"
string +=str((data['game_id']))+"|"
string +=str((data['hostip']))+"|"
string +=str((data['software']))

print string
