# from quantam import all_cmds
import pandas as pd
import random as r


TOKEN = 'your bot token'


error_points = []


hello = """Welcome to this official discord server of `KIIT PolyTechnic C.Sc`
If you're a Tutor mentor teacher or Guest then pick your role/pass from #welcome
If you're a student or subject teacher then take your roles/pass using commands in #command-section

The bot prefix for this server is: ``b.``
The help command to see all commands is ``b.cmd``
To elaborate a command use ``!help <command>``

Have a good day here in `KIIT PolyTechnic C.Sc` :slight_smile:"""


# message links
role_assigning_mesg = 'https://discord.com/channels/919843529470144592/919843529470144595/922042070095507457'
rule_mesg_link = 'https://discord.com/channels/919843529470144592/919852854636838952/923105020218589224'
nickname_policy_link = 'https://discord.com/channels/919843529470144592/919852854636838952/923129543416496158'


# reply messages
fdb_reply_1 = """-Thank you for sending your feedback
-Your feedback has been successfully send to the database.
-Our feedback team will review the feedback and will work on it.
"""

fdb_reply_2 = "-Your feedback will help us to improve this server's performance and your experience with KIIT PolyTechnic C.Sc server."

no_cmd_use_mesg = 'You can not use commands in this channel. Head towards #command-section to use these commands'


# error messages
db_connection_error = 'unable to connect to the database'


# database python variables
line = '-'*50
    
available_tables = {'events': ['Events', 'DROP TABLE Events'], 
                    'students': ['Students', 'DROP TABLE Students', 
                                 r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\students_userID_list.txt'],
                    'teachers': ['Teachers', 'DROP TABLE Teachers', 
                                 r'E:\Programming\Python\Python Projects\PythonBots\DiscordBots\Data\teachers_userID_list.txt']}

table_c_cmd = {'events': 'Events(Eve_ID TEXT, Date TEXT, Event TEXT)', 
                'students': 'Students(SGUID Text, Name Text, Roll_No Int, userID Text)',
                'teachers': 'Teachers(TGUID Text, Name Text, Subject Text, userID Text)'}

roll_nums = [2110501, 2110502, 2110503, 2110504, 2110505, 2110506, 2110507, 2110508, 2110509, 2110510, 
            2110511, 2110512, 2110513, 2110514, 2110515, 2110516, 2110517, 2110518, 2110519, 2110520, 
            2110521, 2110522, 2110523, 2110524, 2110525, 2110526, 2110527, 2110528, 2110529, 2110530, 
            2110531, 2110532, 2110533, 2110534, 2110535, 2110536, 2110537, 2110538, 2110539, 2110540, 
            2110541, 2110542, 2110543, 2110544, 2110545, 2110546, 2110547, 2110548, 2110549, 2110550, 
            2110551, 2110552, 2110553, 2110554, 2110555, 2110556, 2110557, 2110558, 2110559, 2110560, 
            2110561, 2110562, 2110563, 2110564, 2110565]   

all_cmds = ['cmd', 'info', 
            'students', 'teachers', 'events', 
            'userID', 'marks', 
            'add_event', 'del_event', 
            'clean_data_from', 'kick', 'put_marks', 
            'help', 
            'fdb', 
            's_login', 't_login', 
            'verify', 
            '$reboot$', 'update_fdb', 'cc', 'do']

channels = ['🎫-general', '🚙-tutor-mentor-class', '🚗-off-topic', 
            '📒-guest-room', '📕-staff-room', '📙-teacher-guest-general', 
            '➕-cpp-official']

student_clg_login_IDs = ['2110501@kp.kiit.ac.in', '2110502@kp.kiit.ac.in', '2110503@kp.kiit.ac.in', '2110504@kp.kiit.ac.in', 
                     '2110505@kp.kiit.ac.in', '2110506@kp.kiit.ac.in', '2110507@kp.kiit.ac.in', '2110508@kp.kiit.ac.in', 
                     '2110509@kp.kiit.ac.in', '2110510@kp.kiit.ac.in', '2110511@kp.kiit.ac.in', '2110512@kp.kiit.ac.in', 
                     '2110513@kp.kiit.ac.in', '2110514@kp.kiit.ac.in', '2110515@kp.kiit.ac.in', '2110516@kp.kiit.ac.in', 
                     '2110517@kp.kiit.ac.in', '2110518@kp.kiit.ac.in', '2110519@kp.kiit.ac.in', '2110520@kp.kiit.ac.in', 
                     '2110521@kp.kiit.ac.in', '2110522@kp.kiit.ac.in', '2110523@kp.kiit.ac.in', '2110524@kp.kiit.ac.in', 
                     '2110525@kp.kiit.ac.in', '2110526@kp.kiit.ac.in', '2110527@kp.kiit.ac.in', '2110528@kp.kiit.ac.in', 
                     '2110529@kp.kiit.ac.in', '2110530@kp.kiit.ac.in', '2110531@kp.kiit.ac.in', '2110532@kp.kiit.ac.in', 
                     '2110533@kp.kiit.ac.in', '2110534@kp.kiit.ac.in', '2110535@kp.kiit.ac.in', '2110536@kp.kiit.ac.in', 
                     '2110537@kp.kiit.ac.in', '2110538@kp.kiit.ac.in', '2110539@kp.kiit.ac.in', '2110540@kp.kiit.ac.in', 
                     '2110541@kp.kiit.ac.in', '2110542@kp.kiit.ac.in', '2110543@kp.kiit.ac.in', '2110544@kp.kiit.ac.in', 
                     '2110545@kp.kiit.ac.in', '2110546@kp.kiit.ac.in', '2110547@kp.kiit.ac.in', '2110548@kp.kiit.ac.in', 
                     '2110549@kp.kiit.ac.in', '2110550@kp.kiit.ac.in', '2110551@kp.kiit.ac.in', '2110552@kp.kiit.ac.in', 
                     '2110553@kp.kiit.ac.in', '2110554@kp.kiit.ac.in', '2110555@kp.kiit.ac.in', '2110556@kp.kiit.ac.in', 
                     '2110557@kp.kiit.ac.in', '2110558@kp.kiit.ac.in', '2110559@kp.kiit.ac.in', '2110560@kp.kiit.ac.in', 
                     '2110561@kp.kiit.ac.in', '2110562@kp.kiit.ac.in', '2110563@kp.kiit.ac.in', '2110564@kp.kiit.ac.in', 
                     '2110565@kp.kiit.ac.in']

server_rules = ["Follow:-\n-College Website: https://kiit.ac.in/ \n-Server Rules: #rules \n-Server Roles: #roles \n-Server's code of conduct: #code-of-conduct", 
                'Verify yourself or your user ID with your college login ID using `b.verify` in #command-section',
                'Login to your posts accordingly ASAP you join **KIIT PolyTechnic C.Sc Discord**', 
                'Respect staff members and listen to their instruction', 
                'Do not provide or request help on projects that may break laws, breach terms of services, or are malicious or inappropriate.', 
                'Do not post unapproved advertising.', 
                "Keep discussions relevant to the channel topic. Each channel's description tells you the topic.", 
                "Use all commands in command-section only. Don't spam other channels with bot commands.", 
                'Do not help with ongoing exams. When helping with homework, help people learn how to do the assignment without doing it for them.', 
                'Change your server profile according to your college detail.', 
                'Teachers are requested to remove/ban a student using bot command.'
                ]


# backend functions
def formatData(data: list, dirt: str):    # done
    
    for index, value in enumerate(data):
        if dirt in value:
            data[index] = value.replace(dirt, '')
            
        else:
            pass

def showTable(_data: list, cols: list):    # done
    table_data = []
    
    for row in _data:
        table_data += [row]
        
    df = pd.DataFrame(table_data, columns=cols)
    
    return df

def createID(id_len: int, dtype: str):    # done
    
    _id = ""
    
    if (dtype == 'student') or (dtype in 's'):
        _id += 'St'
        
    elif (dtype == 'event') or (dtype in 'e'):
        _id += 'E'
        
    elif (dtype == 'fdb') or (dtype in 'f'):
        _id += 'fdb'
        
    elif (dtype == 'teacher') or (dtype in 't'):
        _id += 'T'
    
    for i in range(id_len):
        _id += str(r.randint(a=0, b=9))
        
    return _id

def checkCMD(command):    # done
    
    validity = False
    
    for cmd in all_cmds:
        if command.startswith(cmd):
            validity = True
            break
            
        else:
            pass
        
    return validity
