import logging
import smtplib
from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)
# email recipients

email_list = ["xxxxxxxxxxxxxxxxxx"]


#function to send emal for help
def send_email(room):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("bxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    msg = "The "+ room + " Room requested assistance using the Amazon Alexa Skill"

    for e in email_list:
        server.sendmail("xxxxxxxx", e, msg)
    #                  send from email           send to email
    #server.sendmail("xxxxxxxxxx", "xxxxxxxx", msg)
    server.quit()
    return


@ask.launch
def greet():
    #greets them
    welcome_msg = """Hello and welcome to the Renaissance Providence Hotel.
                    I can answer questions or send for assistance"""
    return question(welcome_msg)


#{"name": "AssistRoom","type": "LIST_OF_ROOMSTOASSIST"}
@ask.intent("AssistIntent")
def assist(AssistRoom):
    assist_message ="Your request for assistance has been sent. A team member will be in the " + AssistRoom + "  room shortly"
    send_email(AssistRoom)
    return statement(assist_message)

#{"name": "location","type": "LIST_OF_LOCATIONS"}
@ask.intent("FindIntent")

def where_is(location):
    print ('in find')
    if location == "Mozart":
        msg="""The mozart room is on the Mezzanine level.
                     Take any elevator and press the button marked mezzanine"""
    elif location == "Beethoven":
        msg="""The Beethoven room is on the Mezzanine level.
                     Take any elevator and press the button marked mezzanine"""
    elif location == "ball" or location =="the ballroom":
        msg= """The ballroom is located on the ballroom level.
                Take any elevator,  and press the button marked ballroom"""
    elif location== "Hayden":
        msg = "Haydn is located on the temple level. take any elevator and press the button marked temple"
    elif location== "Handel" or location == "handle":
        msg = "the handle room is located on the temple level. take any elevator and press the button marked temple"
    elif location == "symphony a":
        msg = "symphony A is located on the ballroom level. Take any elevator and press the button marked ballroom"
    elif location == "symphony b":
        msg = "symphony B is located on the ballroom level. Take any elevator and press the button marked ballroom"
    elif location == "33rd":
        msg = "the 33rd room is located on the temple level. Take any elevator and press the button marked temple"
    elif location == "capital":
        msg = "the capital room is located on the 7th floor. Take any elevator and press the button marked 7"
    elif location == "club lounge":
        msg = "the club lounge is located on the 7th floor. Take any elevator and press the button marked 7"

    elif location == "dog":
        msg = "bark bark bark"
    else:
         msg="hmmm I heard you say the  ."+ location+".   room.   that does not sound like a meeting room. To speak to a staff member you can ask me to send assistance"
    return statement(msg)




if __name__ == '__main__':

    app.run(debug=True)