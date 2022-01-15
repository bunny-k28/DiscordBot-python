"""
Bot ID- KIIT_C.Sc BOT#0739
"""


print('\n\nACTION: Importing required data... STATUS: ', end='')
import datetime as dt
import os
import sqlite3 as sql
from time import sleep as wait

import discord
from discord import Colour as c
from discord.utils import get

import Data.cmds_info as ci
from Data.quantam import *
from Data.quantam import showTable

print('Done')


print('ACTION: Connecting to the server database... STATUS: ', end='')
# connecting to server's general database
try:
    db = sql.connect('Data\\Database\\database.db')
    cursor = db.cursor()
    db_status = True
    print('Connected')
    
except Exception:
    db = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\database.db')
    cursor = db.cursor()
    db_status = True
    print('Connected')

except Exception as E:
    print(f'unable to connect to the database: {E}')
    error_points += ['connection error']
    exit()

print('ACTION: Connecting to the student database... STATUS: ', end='')
# connecting students marks database
try:
    db2 = sql.connect('Data\\Database\\student_marks.db')
    cursor2 = db2.cursor()
    db_status = True
    print('Connected')
    
except Exception:
    db2 = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\student_marks.db')
    cursor2 = db2.cursor()
    db_status = True
    print('Connected')

except Exception as E:
    print(f'unable to connect to the database: {E}')
    error_points += ['connection error']
    exit()


print('ACTION: creating tables in database(s)... STATUS: ', end='')
try:
    # server's general database
    cursor.execute('CREATE TABLE IF NOT EXISTS Events(Eve_ID TEXT, Date TEXT, Event TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Students(SGUID Text, Name Text, Roll_No Int, userID Text)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Teachers(TGUID Text, Name Text, Subject Text, userID Text)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Feedback(fdb_ID Text, Date Text, Member TEXT, feedback TEXT)')
    print('Created')
    
except Exception as E:
    print('Error creating tables in database')
    error_points += ['tables not created properly']
    print(E)

print('ACTION: final check for database... STATUS: ', end='')
cursor.close()
db.close()

cursor2.close()
db2.close()

if len(error_points) == 0:
    print('All set')

else:
    print(f'Errors occured:- {error_points}')


print('ACTION: preparing bot#0739... STATUS: ', end='')
intents = discord.Intents.default()
intents.members = True

bot = discord.Client(intents=intents)
print('Ready')



if __name__ == '__main__':


    @bot.event
    async def on_ready():
        print('bot#0739 is online...')


    @bot.event
    async def on_message(mesg):
        
        try:
            _cmd = mesg.content.replace('b.', '')
        except Exception:
            pass
                
    
        if (checkCMD(_cmd) is True) or (mesg.content.startswith('!help')) or (mesg.content.startswith('$reboot$')):
            
            if str(mesg.channel.name) in channels :
                # await mesg.channel.send(f'**```@{mesg.author}\n{no_cmd_use_mesg}```**')

                ch = bot.get_channel(921463510775517275)

                mbed = discord.Embed(
                    title=f'**channel not suppoerted for commands**', 
                    description=f'**Rule** :eight: \n{server_rules[7]}\n\n Visit {ch.mention}',
                    color=c.blue()
                )
                
                mbed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                await mesg.channel.send(embed=mbed)
                wait(5.0)
                await mesg.channel.purge(limit=2)
                
            else:
                
                channel = bot.get_channel(919862947034066956)
                
                if mesg.author == bot.user:    # done
                    pass


                elif mesg.content.startswith('b.cmd'):  # done

                    cmds = open('Data\\all_cmds.txt', 'r')
                    cmd_list = cmds.read()
                    cmds.close()

                    await mesg.channel.send(cmd_list)

                
                elif mesg.content.startswith('b.students'):    # done
                    
                    db_status = False

                    try:
                        db = sql.connect('Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True
                        
                    except Exception:
                        db = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True

                    except Exception as E:
                        
                                                
                        try:
                            await channel.send(f'**{db_connection_error} in ``b.students`` command**\n **```{E}```**')
                        except Exception:
                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                        
                        
                    if db_status is True:
                        
                        t_file = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\teachers_userID_list.txt', 'r')
                        t_list = t_file.readlines()
                        t_file.close()
                        
                        formatData(t_list, dirt='\n')
                        
                        if (str(mesg.author) in t_list) or (str(mesg.author) == 'Sleeping💤 Panda🐼#8142'):
                            try:
                                cursor.execute('SELECT * FROM Students')
                                data = cursor.fetchall()
                                
                                cursor.close()
                                db.close()
                            
                            except Exception as E:
                                await mesg.channel.send(f'**```Unable to fetch data```**')
                                
                                try:
                                    link = mesg.jump_url
                                    
                                    mbed = discord.Embed(
                                        title='**Error in ``b.students`` command**\n',
                                        description = f'**```Error: {E}```**\n[Visit]({link})',
                                        color=c.random()
                                    )
                                    await channel.send(embed=mbed)
                                    
                                except Exception:
                                    await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                    
                            if len(data) == 0:
                                await mesg.channel.send('**```No data in the database```**')

                            else:
                                columns = ['GUID', 'Name', 'Roll No.', 'userID']
                                await mesg.channel.send(f'**```{showTable(_data=data, cols=columns)}```**')
                                
                        else:
                            await mesg.channel.send('**```Only teachers can use this command```**')
                            await mesg.channel.purge(limit=2)
                        
                    else:
                        await mesg.channel.send('**```Unable to connect to the database```**')


                elif mesg.content.startswith('b.teachers'):    # done
                            
                            db_status = False

                            try:
                                db = sql.connect('Data\\Database\\database.db')
                                cursor = db.cursor()
                                db_status = True
                                
                            except Exception:
                                db = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\database.db')
                                cursor = db.cursor()
                                db_status = True

                            except Exception as E:
                                
                                                        
                                try:
                                    await channel.send(f'**{db_connection_error} in ``b.teachers`` command**\n **```{E}```**')
                                except Exception:
                                    await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                
                                
                            if db_status is True:
                                
                                try:
                                    cursor.execute('SELECT * FROM Teachers')
                                    data = cursor.fetchall()
                                    
                                    cursor.close()
                                    db.close()
                                
                                except Exception as E:
                                    await mesg.channel.send(f'**```Unable to fetch data```**')
                                    
                                    try:
                                        link = mesg.jump_url
                                
                                        mbed = discord.Embed(
                                            title='**Error in ``b.teachers`` command**\n',
                                            description = f'**```Error: {E}```**\n[Visit]({link})',
                                            color=c.random()
                                        )
                                        
                                        await channel.send(embed=mbed)

                                    except Exception:
                                        await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                    
                                if len(data) == 0:
                                    await mesg.channel.send('```No data in the database```')

                                else:
                                    columns = ['GUID', 'Name', 'Subject', 'userID']
                                    await mesg.channel.send(f'**```{showTable(_data=data, cols=columns)}```**')
                            
                            else:
                                await mesg.channel.send('```Unable to connect to the database```')
                
                
                elif mesg.content.startswith('b.userID'):    # done
                    member = mesg.author
                    # member_mail_ID = mesg.author.mail_id -> \nYour E-Main ID is: **``{member_mail_ID}``**
                    await mesg.channel.send(f'Your user ID is: **``{member}``**')

                
                elif mesg.content.startswith('b.events'):  # done
                    
                    db_status = False

                    try:
                        db = sql.connect('Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True
                        
                    except Exception:
                        db = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True

                    except Exception as E:
                        
                                                
                        try:
                            await channel.send(f'**{db_connection_error} in ``b.events`` command**\n **```{E}```**')
                        except Exception:
                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                    
                    
                    if db_status is True:
                        
                        try:
                            cursor.execute('SELECT * FROM Events')
                            data = cursor.fetchall()
                        
                        except Exception as E:
                            await mesg.channel.send(f'**```Unable to fetch data```**')
                            
                            try:
                                link = mesg.jump_url
                                
                                mbed = discord.Embed(
                                    title='**Error in ``b.events`` command**\n',
                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                    color=c.random()
                                )
                                
                                await channel.send(embed=mbed)
                                
                            except Exception:
                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                            
                        finally:
                            cursor.close()
                            db.close()
                            
                        if len(data) == 0:
                            await mesg.channel.send('**```No Events in the database```**')
                            
                        else:                  
                            columns=["UID", "Date", "Event"]
                            await mesg.channel.send(f'**```{showTable(_data=data, cols=columns)}```**')
                        
                    else:
                        await mesg.channel.send('```Unable to connect to the database```')

                
                elif mesg.content.startswith('b.add_event'):    # done
                    
                    db_status = False

                    try:
                        db = sql.connect('Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True
                        
                    except Exception:
                        db = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True

                    except Exception as E:
                        
                                                
                        try:
                            await channel.send(f'**{db_connection_error} in ``b.add_event`` command**\n **```{E}```**')
                        except Exception:
                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                    
                    
                    if db_status is True:
                        
                        try:
                            cursor.execute('CREATE TABLE IF NOT EXISTS Events(Eve_ID TEXT, Date TEXT, Event TEXT)')

                        except Exception as E:
                            
                            try:
                                link = mesg.jump_url
                                
                                mbed = discord.Embed(
                                    title='**Error in ``b.add_event`` command**\n',
                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                    color=c.random()
                                )
                                
                                await channel.send(embed=mbed)
                                
                            except Exception:
                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')

                        data = mesg.content.replace('b.add_event ', '').lower()

                        date, event = data.split('-')
                        
                        date_div = f'{date}'.split('/')
                        
                        if (int(date_div[0]) <= 31) and (int(date_div[1]) <= 12) and len(event) > 0:

                            try:
                                eve_id = createID(id_len=4, dtype='events')
                                cursor.execute('INSERT INTO Events (Eve_ID, Date, Event) VALUES(?, ?, ?)', (eve_id, date, event))
                                db.commit()
                                
                                cursor.close()
                                db.close()
                                
                                await mesg.channel.send(f'**```Event added```**')
                                
                            except Exception as E:
                                
                                await mesg.channel.send(f'**```Unable to add event```**')

                                try:
                                    link = mesg.jump_url
                                
                                    mbed = discord.Embed(
                                        title='**Error in ``b.add_event`` command**\n',
                                        description = f'**```Error: {E}```**\n[Visit]({link})',
                                        color=c.random()
                                    )
                                    
                                    await channel.send(embed=mbed)

                                except Exception:
                                    await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                
                        else:
                            await mesg.channel.send('```Incorrect Format\n\nDate- DD/MM/YY\nEvent- Event Name\nSyntex- b.add_event <date>-<event>```')

                    else:
                        await mesg.channel.send('```Unable to connect to the database```')


                elif mesg.content.startswith('b.del_event'):    # done
                    
                    db_status = False

                    try:
                        db = sql.connect('Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True
                        
                    except Exception:
                        db = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True

                    except Exception as E:
                                                
                        try:
                            await channel.send(f'**{db_connection_error} in ``b.del_event`` command**\n **```{E}```**')
                        except Exception:
                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                        
                        
                    if db_status is True:
                        
                        data = mesg.content.replace('b.del_event ', '').lower()

                        date, event = data.split('-')
                        
                        date_div = f'{date}'.split('/')
                        
                        if (int(date_div[0]) <= 31) and (int(date_div[1]) <= 12) and (len(event) > 0):
                        
                            try:
                                cursor.execute('SELECT * FROM Events')
                                _data = cursor.fetchall()

                            except Exception as E:
                                await mesg.channel.send(f'**```Unable to fetch data```**')
                                
                                try:
                                    link = mesg.jump_url
                                
                                    mbed = discord.Embed(
                                        title='**Error in ``b.del_event`` command**\n',
                                        description = f'**```Error: {E}```**\n[Visit]({link})',
                                        color=c.random()
                                    )
                                    
                                    await channel.send(embed=mbed)

                                except Exception:
                                    await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                                            
                            
                            for i in _data:
                                
                                if (str(date) in str(i[1])):
                                    
                                    if (str(event) in str(i[2])):
                                        
                                        _id = i[0]
                                
                                        try:
                                            
                                            cursor.execute('DELETE FROM Events WHERE Eve_ID=?', (_id,))
                                            db.commit()
                                            
                                            cursor.close()
                                            db.close()
                                            
                                            await mesg.channel.send(f'```Event: {event} was removed from the database```')
                                            
                                        except Exception as E:
                                            await mesg.channel.send(f'**```Unable to delete event from the database```**')
                                            
                                            try:
                                                link = mesg.jump_url
                                
                                                mbed = discord.Embed(
                                                    title='**Error in ``b.del_event`` command**\n',
                                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                                    color=c.random()
                                                )
                                                
                                                await channel.send(embed=mbed)

                                            except Exception:
                                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                        
                                    else:
                                        await mesg.channel.send(f'```No such event registered for date {date} in the database```')
                                        
                                else:
                                    pass
                            
                        else:
                            await mesg.channel.send('```Incorrect Format\n\nDate- DD/MM/YY\nEvent- Event Name\nSyntex- b.del_event <date>-<event>```')
                    
                    else:
                        await mesg.channel.send('```Unable to connect to the database```')


                elif mesg.content.startswith('!help'):    # done
                    
                    query = mesg.content[6:]
                                    
                    if query == 'b.cmd':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.help}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.blue()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                    
                    elif query == 'b.userID':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.user_id}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.blue()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                    
                    elif query == 'b.events':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.events}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.blue()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                    
                    elif query == 'b.students':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.students}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.blue()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                        
                    elif query == 'b.teachers':    # done
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.teachers}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.blue()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')

                    elif query == 'b.cc':    # done
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.cc}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.blue()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                        
                    elif query == '!p':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.p}```\n\n**{line}**\n\n**Syntax and Example:-**\n```{ci.p_ex}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.green()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                    
                    elif query == 'b.add_event':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.add_event}```\n\n**{line}**\n\n**Syntax and Example:-**\n```{ci.add_event_ex}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.green()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                    
                    elif query == 'b.del_event':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.del_event}```\n\n**{line}**\n\n**Syntax and Example:-**\n```{ci.del_event_ex}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.green()      
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                        
                    elif query == 'b.fdb':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.fdb}```\n\n**{line}**\n\n**Syntax and Example:-**\n```{ci.fdb_ex}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.green()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                    
                    elif query == 'b.s_login':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.s_login}```\n\n**{line}**\n\n**Syntax and Example:-**\n```{ci.s_login_ex}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.red()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                    
                    elif query == 'b.t_login':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.t_login}```\n\n**{line}**\n\n**Syntax and Example:-**\n```{ci.t_login_ex}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.red()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                    
                    elif query == 'b.clean_data_from':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.clean_data_from}```\n\n**{line}**\n\n**Syntax and Example:-**\n```{ci.clean_data_from_ex}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.red()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                          
                    elif query == 'b.kick':    # done
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.remove_mem}```\n\n**{line}**\n\n**Syntax and Example:-**\n```{ci.remove_mem_ex}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.red()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                          
                    elif query == 'b.put_marks':    # done
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.update_marks}```\n\n**{line}**\n\n**Syntax and Example:-**\n```{ci.update_marks_ex}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.red()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                        
                    elif query == 'b.verify':    # done
                        
                        embed = discord.Embed(
                            title=f'**query:**  `{query}`', 
                            description=f'```{ci.verify}```\n\n**{line}**\n\n**Syntax and Example:-**\n```{ci.verify_ex}```\n\n**Hope this helped you out with your query** :rolling_eyes:',
                            color=c.red()
                            )
                        
                        embed.set_author(name=mesg.author, icon_url=mesg.author.avatar_url)

                        try:
                            await mesg.channel.send(embed=embed)
                        
                        except Exception:
                            await mesg.channel.send('```Facing some technical issues.``` :sweat_smile:')
                  
                    elif len(query) == 0:
                        
                        await mesg.channel.send("`No query given. This command requiers 1 argument.` :sweat_smile:")
                        
                    else:
                        await mesg.channel.send(f"**No such command `{query}`. Try `b.cmd` command to know about all existing commands.** :slight_smile:")


                elif mesg.content.startswith('b.fdb'):    # done
                    
                    db_status = False

                    try:
                        db = sql.connect('Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True
                        
                    except Exception:
                        db = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True

                    except Exception as E:
                        
                                                
                        try:
                            await channel.send(f'**{db_connection_error} in ``b.fdb`` command**\n **```{E}```**')
                        except Exception:
                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                            
                    
                    if db_status is True:
                        
                        try:
                            cursor.execute('CREATE TABLE IF NOT EXISTS Feedback(fdb_ID Text, Date Text, Member TEXT, feedback TEXT)')
                            # print('table checked')

                        except Exception as E:
                            await mesg.channel.send(f'**```Facing some technical error```**')
                            
                            try:
                                link = mesg.jump_url
                                
                                mbed = discord.Embed(
                                    title='**Error in ``b.fdb`` command**\n',
                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                    color=c.random()
                                )
                                
                                await channel.send(embed=mbed)
                                
                            except Exception:
                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')

                        date = str(dt.datetime.now())[:10]
                        member = mesg.author
                        fdb = mesg.content.replace('b.fdb ', '').lower()
                        
                        
                        try:
                            fdb_id = createID(id_len=6, dtype='fdb')
                            cursor.execute('INSERT INTO Feedback (fdb_ID, Date, Member, feedback) VALUES(?, ?, ?, ?)', (fdb_id, date, str(member), fdb))
                            db.commit()
                            
                            cursor.close()
                            db.close()
                            
                            fdb_status_file = open('E:\\Programming\\Python\Python Projects\\PythonBots\\DiscordBots\\Data\\feedback_status.txt', 'a')
                            fdb_status_file.write(f'{fdb_id}: Queued\n')
                            fdb_status_file.close()
                            
                            await mesg.channel.send('**```Feedback collected```**')
                            
                            try:
                                await bot.get_channel(923527127276584961).send(f'\n{line}\n**bot contributors and bot owner we have a new feedback\n\nFeedback:- `{fdb}` \nFeedback ID:- {fdb_id}\nfrom:- {mesg.author.mention}**')

                            except Exception as E:
                                
                                try:
                                    link = mesg.jump_url
                                
                                    mbed = discord.Embed(
                                        title='**Error in ``b.fdb`` command**\n',
                                        description = f'**```Error: {E}```**\n[Visit]({link})',
                                        color=c.random()
                                    )
                                    
                                    await channel.send(embed=mbed)
                                    
                                except Exception:
                                    pass

                                                          
                        except Exception as E:
                            await mesg.channel.send(f'**```Facing error in sending feedback```**')
                            
                            try:
                                link = mesg.jump_url
                                
                                mbed = discord.Embed(
                                    title='**Error in ``b.fdb`` command**\n',
                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                    color=c.random()
                                )
                                
                                await channel.send(embed=mbed)
                                
                            except Exception:
                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                
                    else:
                        await mesg.channel.send('```Unable to connect to the database```')


                elif mesg.content.startswith('b.s_login'):    # done

                    db_status = False

                    try:
                        db = sql.connect('Data\\Database\\database.db')
                        cursor = db.cursor()
                        
                        db2 = sql.connect('Data\\Database\\student_marks.db')
                        cursor2 = db2.cursor()
                        
                        db_status = True

                    except Exception:
                        db = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\database.db')
                        cursor = db.cursor()

                        db2 = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\student_marks.db')
                        cursor2 = db2.cursor()
                        
                        db_status = True

                    except Exception as E:
                        try:
                            link = mesg.jump_url
                                
                            mbed = discord.Embed(
                                title=f'**{db_connection_error} in ``b.update_marks`` command**\n',
                                description = f'**```Error: {E}```**\n[Visit]({link})',
                                color=c.random()
                            )
                            
                            await channel.send(embed=mbed)

                        except Exception:
                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')


                    if db_status is True:

                        try:
                            cursor.execute('CREATE TABLE IF NOT EXISTS Students(SGUID Text, Name Text, Roll_No Int, userID Text)')
                            # print('table checked')

                        except Exception as E:
                            await mesg.channel.send(f'**```Facing some technical error```**')
                            
                            try:
                                link = mesg.jump_url
                                
                                mbed = discord.Embed(
                                    title='**Error in ``b.s_login`` command**\n',
                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                    color=c.random()
                                )
                                
                                await channel.send(embed=mbed)

                            except Exception:
                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')

                        student_data = mesg.content.replace('b.s_login ', '')

                        userID = mesg.author

                        students_list = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\students_userID_list.txt', 'r')
                        teachers_list = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\teachers_userID_list.txt', 'r')
                        
                        s_userIDs = students_list.readlines()
                        t_userIDs = teachers_list.readlines()

                        students_list.close()
                        teachers_list.close()

                        formatData(s_userIDs, dirt='\n')
                        formatData(t_userIDs, dirt='\n')

                        if str(userID) in s_userIDs:
                            await mesg.channel.send("**```You're already logged in.```** :sweat_smile:")

                        elif str(userID) in t_userIDs:
                            await mesg.channel.send("**```You've already logged in as a teacher here, can't give you students pass```** :sweat_smile:")

                        else:
                            try:
                                name, roll_no, branch = f'{student_data}'.split('-') 

                            except Exception as E:
                                await mesg.channel.send('**```No details given to log you in.```** :slight_frown:')
                                print(E)


                            if (len(name) > 0) and (len(roll_no) == 7) and (len(branch) > 0):
                                if (branch.lower() == 'c.sc') and (int(roll_no) in roll_nums):

                                    St_ID = createID(id_len=5, dtype='s')
                                        
                                    try:
                                        role_to_add = get(userID.guild.roles, name="Students")
                                        await userID.add_roles(role_to_add)
                                        
                                    except Exception as E:
                                        await mesg.channel.send(f'**```Unable to give you students pass```**')
                                        
                                        try:
                                            link = mesg.jump_url
                                
                                            mbed = discord.Embed(
                                                title='**Error in ``b.s_login`` command**\n',
                                                description = f'**```Error: {E}```**\n[Visit]({link})',
                                                color=c.random()
                                            )
                                            
                                            await channel.send(embed=mbed)

                                        except Exception:
                                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                        
                                    try:
                                        cursor.execute('INSERT INTO Students (SGUID, Name, Roll_No, userID) VALUES(?, ?, ?, ?)', (St_ID, str(name), int(roll_no), str(userID)))
                                        db.commit()
                                        
                                        try:
                                            remove_visitor_role = get(userID.guild.roles, name='Visitors')
                                            remove_guest_role = get(userID.guild.roles, name='Guests')

                                            await userID.remove_roles(remove_visitor_role)
                                            await userID.remove_roles(remove_guest_role)
                                            
                                        except Exception as E:
                                            await mesg.channel.send(f'**```Facing some technical error```**')
                                            
                                            try:
                                                link = mesg.jump_url
                                
                                                mbed = discord.Embed(
                                                    title='**Error in ``b.s_login`` command**\n',
                                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                                    color=c.random()
                                                )
                                                
                                                await channel.send(embed=mbed)

                                            except Exception:
                                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')

                                        members_list = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\students_userID_list.txt', 'a')
                                        members_list.write(f'{userID}\n')
                                        members_list.close()
                                        
                                        # await mesg.channel.send(f"**```-Hey {userID}\n-Welcome to KIIT PolyTechnic C.Sc\n-Now you're a official member of this server\n-Your GUID is {St_ID}```**\n**---Have a good day :smiley:**")
                                        await mesg.author.send(f"**```-Hey {userID}\n-Welcome to KIIT PolyTechnic C.Sc\n-Your SGUID is {St_ID}\n-Please keep this Id safe. This SGUID will help you to check your semester marks.\n-Use the command b.marks <your GUID> in #command-section and I'll send you your marks here in the DM.```**")
                                        
                                        try:
                                            cursor2.execute(f'CREATE TABLE IF NOT EXISTS {St_ID}(Exam_Period Text, Subject Text, Marks_Gained Text)')
                                            
                                            cursor2.close()
                                            db2.close()
                                        
                                        except Exception as E:
                                            try:
                                                link = mesg.jump_url
                                
                                                mbed = discord.Embed(
                                                    title='**Error in ``b.s_login`` command**\n',
                                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                                    color=c.random()
                                                )
                                                
                                                await channel.send(embed=mbed)

                                            except Exception:
                                                pass                                        
                                        
                                        try:
                                            await mesg.author.edit(nick=f"{name.replace(' ', '_')}")

                                        except Exception as E:
                                            await mesg.channel.send("**```I'm unable to change your nickname. Please do it manually.```**")
                                            
                                            try:
                                                link = mesg.jump_url
                                
                                                mbed = discord.Embed(
                                                    title='**Error in ``b.s_login`` command**\n',
                                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                                    color=c.random()
                                                )
                                                
                                                await channel.send(embed=mbed)

                                            except Exception:
                                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                                
                                                
                                    except Exception as E:  
                                        await mesg.channel.send(f"**```I'm not able to add your details to the database.\nI've sent the error to the bot manager```**")
                                        
                                        try:
                                            link = mesg.jump_url
                                
                                            mbed = discord.Embed(
                                                title='**Error in ``b.s_login`` command**\n',
                                                description = f'**```Error: {E}```**\n[Visit]({link})',
                                                color=c.random()
                                            )
                                            
                                            await channel.send(embed=mbed)

                                        except Exception:
                                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')

                                    finally:
                                        cursor.close()
                                        db.close()
                                    
                                else:
                                    await mesg.channel.send("**```Your data is not matching with the college database. Sorry I can't give you the students pass.```**:grimacing:")
                
                            else:
                                await mesg.channel.send("**```Incorrect Format\n\nStudent Name- <First name> <Middle name [Optional]> <Last name>\nRoll No.- A 7 digit no. given by college\nBranch- Name of the branch you're in\n\nSyntex- b.s_login <Full name>-<Roll No.>-<Branch>```**")
                                                
                    else:
                        await mesg.channel.send('**```Unable to connect to the database```**')


                elif mesg.content.startswith('b.t_login'):    # done
                    db_status = False

                    try:
                        db = sql.connect('Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True

                    except Exception:
                        db = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True

                    except Exception as E:                 
                        try:
                            await channel.send(f'**{db_connection_error} in ``b.t_login`` command**\n **```{E}```**')
                        except Exception:
                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')


                    if db_status is True:
                        
                        try:
                            cursor.execute('CREATE TABLE IF NOT EXISTS Teachers(TGUID Text, Name Text, Subject Text, userID Text)')
                        
                        except Exception as E:
                            await mesg.channel.send(f'**```Facing some technical error```**')
                            
                            try:
                                link = mesg.jump_url
                                
                                mbed = discord.Embed(
                                    title='**Error in ``b.t_login`` command**\n',
                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                    color=c.random()
                                )
                                
                                await channel.send(embed=mbed)

                            except Exception:
                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                            
                        teacher_data = mesg.content.replace('b.t_login ', '')
                        
                        userID = mesg.author
                        
                        teachers_list = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\teachers_userID_list.txt', 'r')
                        students_list = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\students_userID_list.txt', 'r')

                        s_userIDs = students_list.readlines()
                        t_userIDs = teachers_list.readlines()
                        
                        teachers_list.close()
                        students_list.close()
                        
                        formatData(t_userIDs, dirt='\n')
                        formatData(s_userIDs, dirt='\n')
                        
                        if str(userID) in t_userIDs:
                            await mesg.channel.send("**```You're already logged in as a teacher```** :sweat_smile:")

                        elif str(userID) in s_userIDs:
                            await mesg.channel.send("**```You've already logged in as a student here can't give you teachers pass```** :sweat_smile:")
                        
                        else:
                            try:
                                name, subject = f'{teacher_data}'.split('-')
                                
                            except Exception as E:
                                await mesg.channel.send('**```No details given to log you in.```** :slight_frown:')
                                print(E)
                                
                            
                            if (len(name) > 0) and (len(subject) > 0):
                                
                                t_id = createID(id_len=5, dtype='t')
                                
                                try:
                                    remove_visitor_role = get(userID.guild.roles, name='Visitors')
                                    remove_guest_role = get(userID.guild.roles, name='Guests')

                                    await userID.remove_roles(remove_visitor_role)
                                    await userID.remove_roles(remove_guest_role)
                                
                                except Exception as E:
                                    await mesg.channel.send(f'**```Facing some technical error```**')
                                    
                                    try:
                                        link = mesg.jump_url
                                
                                        mbed = discord.Embed(
                                            title='**Error in ``b.t_login`` command**\n',
                                            description = f'**```Error: {E}```**\n[Visit]({link})',
                                            color=c.random()
                                        )

                                        await channel.send(embed=mbed)

                                    except Exception:
                                        await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                    
                                try:
                                    cursor.execute('INSERT INTO Teachers (TGUID, Name, Subject, userID) VALUES(?, ?, ?, ?)', (t_id, str(name), str(subject), str(userID)))
                                    db.commit()
                                    
                                    try:
                                        role_to_add = get(userID.guild.roles, name='Teachers')
                                        await userID.add_roles(role_to_add)

                                    except Exception as E:
                                        await mesg.channel.send(f'**```Unable to give you teachers pass```**')
                                        
                                        try:
                                            link = mesg.jump_url
                                
                                            mbed = discord.Embed(
                                                title='**Error in ``b.t_login`` command**\n',
                                                description = f'**```Error: {E}```**\n[Visit]({link})',
                                                color=c.random()
                                            )

                                            await channel.send(embed=mbed)

                                        except Exception:
                                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')

                                    members_list = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\teachers_userID_list.txt', 'a')
                                    members_list.write(f'{userID}\n')
                                    members_list.close()
                                    
                                    await mesg.channel.send(f"**```-Hey {userID}\n-Welcome to KIIT PolyTechnic C.Sc\n-Now you're a official member of this server\n-Your GUID is {t_id}```**\n**---Have a good day :smiley:**")

                                except Exception as E:  
                                        await mesg.channel.send(f"**```I'm not able to add your details to the database.\nI've sent the error to the bot manager.```**")                            

                                        try:
                                            link = mesg.jump_url
                                
                                            mbed = discord.Embed(
                                                title='**Error in ``b.t_login`` command**\n',
                                                description = f'**```Error: {E}```**\n[Visit]({link})',
                                                color=c.random()
                                            )

                                            await channel.send(embed=mbed)

                                        except Exception:
                                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')

                                finally:
                                    cursor.close()
                                    db.close()
                                    
                            else:
                                await mesg.channel.send("**```Incorrect Format\n\nTeacher Name- <First name> <Middle name [Optional]> <Last name>\nSubject:- <subject name you're teaching>\n\nSyntex- b.s_login <Full name>-<Roll No.>-<Branch>```**")
                                                
                    else:
                        await mesg.channel.send('**```Unable to connect to the database```**')


                elif mesg.content.startswith('b.verify'):    # done
                    
                    clg_login_id = mesg.content.replace('b.verify ', '')
                    userID = mesg.author
                    
                    if len(clg_login_id) > 0:
                        validity = False
                        
                        for _id in student_clg_login_IDs:
                            if _id == clg_login_id:
                                validity = True
                                break
                                
                            else:
                                validity = False
                                
                        if validity is True:
                            
                            try:
                                role_to_add = get(userID.guild.roles, name="VERIFIED-ID")
                                await userID.add_roles(role_to_add)
                                
                                await mesg.channel.send('**```your college login ID is verified. Now you can access the required Voice Channel(s)```**')

                            except Exception as E:
                                await mesg.channel.send(f'**```Unable to verify your ID```**')
                                
                                try:
                                    link = mesg.jump_url
                                    
                                    mbed = discord.Embed(
                                        title='**Error in ``b.verify`` command**\n',
                                        description = f'**```Error: {E}```**\n[Visit]({link})',
                                        color=c.random()
                                    )

                                    await channel.send(embed=mbed)

                                except Exception:
                                    await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                            
                        elif validity is False:
                            
                            await mesg.channel.send("**```invalid login ID. Taking all your passes and giving Visitors pass```**")
                            wait(1.5)
                            
                            try:
                                remove_students_pass = get(userID.guild.roles, name="Students")
                                remove_bot_cont_pass = get(userID.guild.roles, name="bot-contributor")
                                give_visitor_pass = get(userID.guild.roles, name="Visitors")
                            
                            except Exception as E:
                                await mesg.channel.send(f'**```Facing some technical error```**')
                                
                                try:
                                    link = mesg.jump_url
                                    
                                    mbed = discord.Embed(
                                        title='**Error in ``b.verify`` command**\n',
                                        description = f'**```Error: {E}```**\n[Visit]({link})',
                                        color=c.random()
                                    )

                                    await channel.send(embed=mbed)

                                except Exception:
                                    await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                
                            try:
                                await userID.remove_roles(remove_students_pass)
                                await userID.remove_roles(remove_bot_cont_pass)
                                await userID.add_roles(give_visitor_pass)
                                
                            except Exception as E:
                                await mesg.channel.send(f'**```Facing some technical error```**')
                                
                                try:
                                    link = mesg.jump_url
                                    
                                    mbed = discord.Embed(
                                        title='**Error in ``b.verify`` command**\n',
                                        description = f'**```Error: {E}```**\n[Visit]({link})',
                                        color=c.random()
                                    )

                                    await channel.send(embed=mbed)

                                except Exception:
                                    await mesg.channel.send(f'**```Unable to send the error to bot owner```**')

                    else:
                        await mesg.channel.send(f'**```No details given to verify your ID```**')


                elif mesg.content.startswith('b.marks'):    # done
                    mention = mesg.author.mention
                    
                    await mesg.channel.purge(limit=1)
                    await mesg.channel.send(f"**{mention} I've send your marksheet through the DM. Please check**")
                    
                    db_status = False
                    
                    try:
                        db2 = sql.connect('Data\\Database\\student_marks.db')
                        cursor2 = db2.cursor()
                        db_status = True
                        
                    except Exception:
                        db2 = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\student_marks.db')
                        cursor2 = db2.cursor()
                        db_status = True

                    except Exception as E:
                              
                        try:
                            link = mesg.jump_url
                                
                            mbed = discord.Embed(
                                title=f'**{db_connection_error} in ``b.update_marks`` command**\n',
                                description = f'**```Error: {E}```**\n[Visit]({link})',
                                color=c.random()
                            )
                            
                            await channel.send(embed=mbed)
                            
                        except Exception:
                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')


                    if db_status is True:
                        stm_table = mesg.content.replace('b.marks ', '')

                        try:
                            cursor2.execute(f'SELECT * FROM {stm_table}')
                            data = cursor2.fetchall()
                            
                            cursor2.close()
                            db2.close()
                        
                        except Exception as E:
                            await mesg.channel.send(f'**```Unable to fetch data```**')
                            
                            try:
                                link = mesg.jump_url
                                
                                mbed = discord.Embed(
                                    title='**Error in ``b.marks`` command**\n',
                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                    color=c.random()
                                )
                                await channel.send(embed=mbed)
                                
                            except Exception:
                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')

                        if len(data) == 0:
                            await mesg.channel.send('**```No data in the database```**')

                        else:
                            await mesg.author.send(f'**Your marksheet:- \n**')
                            columns = ['Exam Period', 'Subject', 'Marks']
                            await mesg.author.send(f'**```{showTable(_data=data, cols=columns)}```**')


                elif mesg.content.startswith('b.clean_data_from'):    # (cmd for teachers) done
                    
                    db_status = False
                    
                    try:
                        db = sql.connect('Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True
                        
                    except Exception:
                        db = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\database.db')
                        cursor = db.cursor()
                        db_status = True

                    except Exception as E:
                        try:
                            link = mesg.jump_url
                                
                            mbed = discord.Embed(
                                title=f'**{db_connection_error} in ``b.clean_data_from`` command**\n',
                                description = f'**```Error: {E}```**\n[Visit]({link})',
                                color=c.random()
                            )
                            
                            await channel.send(embed=mbed)

                        except Exception:
                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                            
                    
                    table = mesg.content.replace('b.clean_data_from ', '').lower()

                    if db_status is True:
                        if (f'{table}'.lower()) in ['events', 'students', 'teachers']:
                            
                            teachers_file = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\teachers_userID_list.txt', 'r')
                            teachers_list = teachers_file.readlines()
                            teachers_file.close()
                            
                            formatData(teachers_list, dirt='\n')
                            
                            if (str(mesg.author) in teachers_list) or (str(mesg.author) == 'Sleeping💤 Panda🐼#8142'):
                            
                                await mesg.channel.send(f'**```Command given by: {mesg.author}\nPermission: Granted```**')
                                
                                try:
                                    cursor.execute(f'{available_tables[table][1]}')                      
                                    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_c_cmd[table]}')
                                    db.commit()
                                    
                                    try:
                                        file = open(f'{available_tables[table][2]}', 'w')
                                        file.truncate()
                                        file.close()
                                        
                                        await mesg.channel.send(f'**```Database <{table.title()}> successfully cleaned up.```**')
                                        
                                    except Exception as E:
                                        await mesg.channel.send(f'**```Facing error while cleaning up the database```**')
                                        
                                        try:
                                            link = mesg.jump_url
                                
                                            mbed = discord.Embed(
                                                title=f'**Error in ``b.clean_data_from`` command**\n',
                                                description = f'**```Error: {E}```**\n[Visit]({link})',
                                                color=c.random()
                                            )
                                            
                                            await channel.send(embed=mbed)
                                            
                                        except Exception:
                                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                    
                                except Exception:
                                    cursor.execute(f"DROP TABLE {available_tables[table][0]}")
                                    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_c_cmd[table]}')
                                    db.commit()
                                    
                                    try:
                                        file = open(f'{available_tables[table][2]}', 'w')
                                        file.truncate()
                                        file.close()
                                        
                                        await mesg.channel.send('**```Database <Students> successfully cleaned up.```**')
                                        
                                    except Exception as E:
                                        await mesg.channel.send(f'**```Facing error while cleaning up the database```**')
                                        
                                        try:
                                            link = mesg.jump_url
                                
                                            mbed = discord.Embed(
                                                title='**Error in ``b.clean_data_from`` command**\n',
                                                description = f'**```Error: {E}```**\n[Visit]({link})',
                                                color=c.random()
                                            )

                                            await channel.send(embed=mbed)

                                        except Exception:
                                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                    
                                except Exception as E:
                                        await mesg.channel.send(f'**```Facing error while cleaning up the database```**')
                                        
                                        try:
                                            link = mesg.jump_url
                                
                                            mbed = discord.Embed(
                                                title='**Error in ``b.clean_data_from`` command**\n',
                                                description = f'**```Error: {E}```**\n[Visit]({link})',
                                                color=c.random()
                                            )

                                            await channel.send(embed=mbed)

                                        except Exception:
                                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                    
                                finally:
                                    cursor.close()
                                    db.close()
                                    
                            else:
                                await mesg.channel.send(f'```Command given by: {mesg.author}\nPermission: Denied```')
                                    
                        else:
                            await mesg.channel.send(f'**```No such file or directory in the database of the server```**')
                            
                    else:
                        await mesg.channel.send('**```Unable to connect to the database```**')


                elif mesg.content.startswith('b.kick'):    # (cmd for teachers) done
                    
                    member_details = mesg.content.replace('b.kick ', '')
                    mem_id, reason = member_details.split('-')
                    
                    member = mesg.guild.get_member(int(mem_id))
                    
                    teachers_file = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\teachers_userID_list.txt', 'r')
                    teachers_list = teachers_file.readlines()
                    teachers_file.close()
                    
                    formatData(teachers_list, dirt='\n')
                    
                    if (str(mesg.author) in teachers_list) or str(mesg.author) == 'Sleeping💤 Panda🐼#8142':
                        if (len(mem_id) > 0) and (len(reason) > 0):
                            
                            # member = mesg.guild.get_member(int(mem_id))
                            await bot.get_user(int(mem_id)).send(f"**```You've been kicked out from the KIIT PolyTechnic C.Sc server.\nReason:-{reason}```**")
                            
                            try:
                                await member.kick()
                                await mesg.channel.purge(limit=1)
                                
                            except Exception as E:
                                await mesg.channel.send(f'**```Unable to kick the member```**')
                                
                                try:
                                    link = mesg.jump_url
                                
                                    mbed = discord.Embed(
                                        title='**Error in ``b.kick`` command**\n',
                                        description = f'**```Error: {E}```**\n[Visit]({link})',
                                        color=c.random()
                                    )
                                    
                                    await channel.send(embed=mbed)

                                except Exception:
                                    await mesg.channel.send(f'**```Unable to send the error to bot owner```**')

                        else:
                            await mesg.channel.send('**```No details given```**')
                            
                    else:
                        await mesg.channel.send(f'**```Only teachers can use this command. If you have any issues with {member}, inform Teachers regarding your issue.```**')


                elif mesg.content.startswith('b.put_marks'):    # (cmd for teachers) in progress
                    if str(mesg.channel.name) == '📔-upload-marks':
                        db_status = False
                        
                        try:
                            db2 = sql.connect('Data\\Database\\student_marks.db')
                            cursor2 = db2.cursor()
                            db_status = True
                            
                        except Exception:
                            db2 = sql.connect('E:\\Programming\\Python\\Python Projects\\PythonBots\\DiscordBot\\Data\\Database\\student_marks.db')
                            cursor2 = db2.cursor()
                            db_status = True

                        except Exception as E:
                                
                            try:
                                link = mesg.jump_url
                                    
                                mbed = discord.Embed(
                                    title=f'**{db_connection_error} in ``b.put_marks`` command**\n',
                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                    color=c.random()
                                )
                                
                                await channel.send(embed=mbed)
                                
                            except Exception:
                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')


                        if db_status is True:
                            details = mesg.content.replace('b.put_marks ', '')
                            
                            t_file = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\teachers_userID_list.txt', 'r')
                            t_list = t_file.readlines()
                            t_file.close()
                            
                            formatData(t_list, dirt='\n')
                            
                            if (str(mesg.author) in t_list) or (str(mesg.author) == 'Sleeping💤 Panda🐼#8142'):
                                
                                sguid, exam_per, sub, gmark = details.split('-')
                                
                                if (len(sguid) > 0) and (len(exam_per) > 0) and (len(gmark) > 0) and (len(sub) > 0):
                                    cursor2.execute(f'CREATE TABLE IF NOT EXISTS {sguid}(Exam_Period Text, Subject Text, Marks_Gained Text)')
                                    
                                    try:
                                        cursor2.execute(f'INSERT INTO {sguid} (Exam_Period, Subject, Marks_Gained) VALUES(?, ?, ?)', (exam_per, sub, str(gmark)))
                                        db2.commit()
                                        
                                        cursor2.close()
                                        db2.close()
                                        
                                        await mesg.channel.send('**```Student Marks updated successfully```**')

                                    except Exception as E:
                                        try:
                                            link = mesg.jump_url
                                                
                                            mbed = discord.Embed(
                                                title=f'**Error in ``b.put_marks`` command**\n',
                                                description = f'**```Error: {E}```**\n[Visit]({link})',
                                                color=c.random()
                                            )
                                            
                                            await channel.send(embed=mbed)
                                            
                                        except Exception:
                                            await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                                    
                                else:
                                    await mesg.channel.send('**```No details given to work on```**')

                            else:
                                await mesg.channel.send('**```Only teachers can use this command```**')
                            
                        elif db_status is False:
                            await mesg.channel.send('**```Unable to connect to the database```**')
                            
                            try:
                                link = mesg.jump_url
                                    
                                mbed = discord.Embed(
                                    title=f'**{db_connection_error} in ``b.put_marks`` command**\n',
                                    description = f'**```Error: {E}```**\n[Visit]({link})',
                                    color=c.random()
                                )
                                
                                await channel.send(embed=mbed)
                                
                            except Exception:
                                await mesg.channel.send(f'**```Unable to send the error to bot owner```**')
                    
                    else:
                        
                        ch = bot.get_channel(927225641710006333)
                        
                        mbed = discord.Embed(
                            title='command not supported',
                            description = f"This channel is not supported for this command. You're requested to use this command in {ch.mention} \n[VISIT](https://discord.com/channels/919843529470144592/927225641710006333/927269054526398485)",
                            color=c.blue()
                        )
                        
                        await mesg.channel.send(embed=mbed)
                        wait(8.0)
                        await mesg.channel.purge(limit=2)


                elif mesg.content.startswith('b.update_fdb'):    # (cmd for admin) done
                    
                    member_details = mesg.content.replace('b.update_fdb ', '')
                    fdb_id, id_num, status = member_details.split('-')
                    
                    member = bot.get_user(int(id_num))


                    fdb_file = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\feedback_status.txt', 'r')
                    fdbs = fdb_file.readlines()
                    fdb_file.close()

                    formatData(fdbs, '\n')
                        
                    updation = False

                    for index, _fdb in enumerate(fdbs):
                        
                        if fdb_id in _fdb:
                            updation = True
                            fdbs[index] = f'{fdb_id}: {status}'
                            await mesg.channel.send(f'**```feedback ID: {fdb_id} updated successfully```**')
                            break
                        
                        else:
                            updation = False

                    if updation is True:
                        
                        x = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\feedback_status.txt', 'w')
                        x.truncate()
                        x.close()
                        
                        fdb_status_file = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\feedback_status.txt', 'a')
                        
                        for fdb in fdbs:
                            fdb_status_file.write(f'{fdb}\n')
                            
                        fdb_status_file.close()

                        await member.send(f'**```Hey there, your feedback is {status}```**')

                    elif updation is False:
                        await mesg.channel.send(f'feedback ID: {fdb_id} not found')


                elif mesg.content.startswith('b.cc'):    # (cmd for admin) done
                    limit = mesg.content.replace('b.cc ', '')
                    await mesg.channel.purge(limit=int(limit) + 1)


                elif mesg.content.startswith('$reboot$'):	# (cmd for admin) done
                    
                    userID = mesg.author
                    botID = str(bot.user)
                    
                    if f'{userID}' in ['Sleeping💤 Panda🐼#8142']:
                        
                        await mesg.channel.send(f'**```Command given by: {userID}\nPermission: Granted\n{botID} Will be updated within 5 to 7 seconds...```**')
                        os.system(r'python .\main_bot.py')
                        
                    else:
                        await mesg.channel.send(f'**```Command given by: {userID}\nPermission: Denied```**')


                elif mesg.content == 'do':    # (cmd for admin) done
                    pass


        elif checkCMD(_cmd) is False:
            
            if (mesg.author == bot.user) or (str(mesg.author) == 'MEE6#4876'):
                pass
            
            else:
                
                await mesg.channel.send('**```no such command```**')
                wait(1.0)
                await mesg.channel.purge(limit=2)
                

    @bot.event
    async def on_member_join(member):
        
        channel = bot.get_channel(919862947034066956)
        
        validity = False
        
        users_file = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\left_users.txt', 'r')
        users = users_file.readlines()
        users_file.close()
        
        users_file2 = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\students_userID_list.txt', 'r')
        users2 = users_file2.readlines()
        users_file2.close()
        
        formatData(users2, dirt='\n')
        formatData(users, dirt='\n')
        
        for i in users:
            if str(member) == i:
                validity = True
                
            else:
                validity = False
                
        if (validity is True) and (str(member) in users2):

            await member.send(f'**Welcome back {member} Nice to have you again in our server.\n\nHave a nice day** :slight_smile:')
            
            try:
                role_to_add = get(member.guild.roles, name="Students")
                await member.add_roles(role_to_add)
                
                role_to_remove = get(member.guild.roles, name="Visitors")
                await member.remove_roles(role_to_remove)
                
            except Exception as E:
                await member.send(f'**```Unable to give you students pass. Please login manually```**')
                
                try:
                    await channel.send(f'**Error in ``on_member_join()`` event**\n **```{E}```**')
                    
                except Exception:
                    await member.send(f'**```Unable to send the error to bot owner```**')
                
                # role_to_add = get(member.guild.roles, name="Visitors")
                # await member.add_roles(role_to_add)
                    

        elif validity is False:
            await member.send(f"**Hey there ``{member}``\n\n{hello}**")

            users_file = open(r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\left_users.txt', 'a')
            users_file.write(f'{str(member)}\n')
            users_file.close()
    
    
    bot.run(TOKEN)
