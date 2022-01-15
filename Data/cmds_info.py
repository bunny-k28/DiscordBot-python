help = """-This command helps you to know what all commands are present for the Me.\n
-There's another command which works same is !ls_cmds\n
-Till yet in total the bot serves 16 commands.\n
-This command do not take any argument or extra detail."""


user_id = """-This is a very useful command provided by Me\n
-This command helps you to know your user ID or your username with your user tag.\n
-In case you forgot your user ID and unable to find, Just type this command and the bot will help you.\n
-This command do not take any argument or extra detail."""


events = """-This command prints or displays all up-comming events of the server or college.\n
-Till yet I can only display the up-comming events, later on it will give you a reminder too.\n
-This command do not take any argument or extra detail.\n"""


students = """-This command prints or displays data of all students logged into the server.\n
-I display student's Name, Roll No., Branch and username or user ID.\n
-The data I display will be in the form of a table.\n
-This command do not take any argument or extra detail.\n"""


teachers = """-This command prints or displays data of all teachers logged into the server.\n
-I display teacher's Name, teaching subject, and username or user ID.\n
-The data I display will be in the form of a table.\n
-This command do not take any argument or extra detail.\n"""


p = """-This is a very useful and powerful command I provid to you all.\n
-This command gives you a good explaination and a example about the command you'r unable to understand.\n
-just type -p and the command you wanna know about.\n
-This command takes argument."""


cc = """-This UI command helps you to deletes the no. of recent messages mentioned.\n
-This command takes 1 argument i.e. no. of messages to be deleted.\n
"""


p_ex = """Syntax:- !p <query>\n
Example:- 1) !p b.help\n
          2) !p b.add_event\n
          3) !p b.s_login\n
"""


add_event = """-This is a UI command provided by me to add college events to the database.\n
-This command add the mentioned event to the database & in my next version I'll also remind you about it.\n
-This commad add the event data in the bot database not into the server database.\n
-This command takes 2 argument, 1st is event date & 2nd is the event.\n
-You can also add events from the GUI feature provided by Discord. You can find it above the INFORMATION category.\n
"""

add_event_ex = """Syntax:- b.add_event <event date(DD/MM/YY)>-<event>\n
Example:- 1) b.add_event 25/12/22-christmas\n
          2) b.add_event 09/04/55-word sports day\n
"""


del_event = """-This is UI command provided by me is to delete college events from the database.\n
-This command deletes the mentioned event from the database & in my next version I'll automatically delete the event once it's done.\n
-This commad deletes the event data from the bot database not from the server database.\n
-This command takes 2 argument, 1st is event date & 2nd is the event.\n
-This command only works if you add a event by using -add_event command.
"""

del_event_ex = """Syntax:- b.del_event <event date(DD/MM/YY)>-<event>\n
Example:- 1) b.del_event 25/12/22-christmas\n
          2) b.del_event 09/04/55-word sports day\n
"""


s_login = """-This login UI command is for students which will give them access to few main channels.\n
-The moment you'll use this commad, I'll give you the student pass of this server.\n
-With this command, I'll be needing 3 more details regarding your college info.\n
-I'll store all the info in my database which can be accessed by everyone anytime using the command !students .\n
-This command take 3 argument, 1st is student's full name, 2nd is the college roll no. & 3rd is the branch name.
"""

s_login_ex = """Syntax:- b.s_login <First Name> <Surname [Optional]>-<college Roll no.>-<Branch Name>\n
Example:- 1) b.s_login Bhagyashree Rout-2110519-C.Sc\n
          2) b.s_login Aniruddha Saha-2110509-C.Sc\n
"""


t_login = """-This login UI command is for teachers which will give them access to all the channels.\n
-The moment you'll use this commad, I'll give you the teacher pass of this server.\n
-With this command, I'll be needing 3 more details regarding you.\n
-I'll store all the info in my database which can be accessed by everyone anytime using the command !teachers .\n
-This command take 2 argument, 1st is teacher's full name, 2nd is the subject name they teach.
"""

t_login_ex = """Syntax:- b.t_login <First Name> <Surname [Optional]>-<teaching subject>\n
Example:- 1) b.t_login Chinmayee Mahapatra-English\n
          2) b.t_login Swagatika-C.Sc\n
"""
                


fdb = """-This UI command helps you to send the feedback to the server's database, and we improve the server with your feedback.\n
-After you give your feedback, we'll work on it and send you the results within 1 week.\n
-This command takes 3 arguments, 1st feedback subject, 2nd your feedback, 3rd your user ID which will be automatically collected by the me.
"""

fdb_ex = """Syntax:- b.fdb <feedback>\n
Example:- 1) b.fdb the bot is not assigning the roles/passes properly\n
          2) b.fdb this server can have a different channel for programming projects.\n
          3) b.fdb a attendence taking feature can be added to the bot.\n
"""


clean_data_from = """-This command helps you to clean all data from the mentioned database table name.\n
-This command can only be accessed by the teachers and admins.\n
-This command takes only 1 argument i.e. the name of the table from the database.
"""

clean_data_from_ex = """Syntax:- b.clear_data <tabel name>\n
Example:- 1) b.clear_data Events
          2) b.clear_data students
"""


verify = """-This command will give you VERIFIED-ID pass which will allow you to join the voice channel(S).\n
-This command is compulsory for all students.\n
-If your verification is invalid, I will take all your passes and return the Visitor pass.\n
-This command takes only 1 argument i.e. your login ID given by college. 
"""

verify_ex = """Syntax:- b.verify <login ID given by college>\n
Example:- 1) b.verify <college roll no.>@kp.kiit.ac.in
"""


remove_mem = """
"""

remove_mem_ex = """
"""


update_marks = """
"""

update_marks_ex = """
"""


marks = """
"""

marks_ex = """
"""