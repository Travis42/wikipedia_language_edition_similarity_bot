import configparser
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

config = configparser.ConfigParser()
config.read("config.cnf")

# setting an envionmental variable
os.environ["SENDGRID_API_KEY"] = config.get('Sendgrid', 'API')


with open('wiki-bot.log', 'r') as f:
    log = f.read()

os.rename('wiki-bot.log', 'wiki-bot.log-old')

message = Mail(
    from_email=config.get('Sendgrid', 'from_email'),
    to_emails=(config.get('Sendgrid', 'to_email'))
    subject='Wiki-bot status',
    html_content="<div>Today's log:</div>",
                "<div>", log,"</div>")


try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    #print(response.status_code)
    #print(response.body)
    #print(response.headers)
except Exception as e:
    #print(str(e))
