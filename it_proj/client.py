import socket
import threading
import json
from cmd import Cmd

class Client(Cmd):
    prompt = ''
    intro = 'Welcome to my chatroom\n' + '\help you for use program \n'

    def __init__(self):
        
        super().__init__()
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__id = None
        self.__nickname = None

    def __receive_message_thread(self):
        """
        Accept message thread
        """
        while True:
            # noinspection PyBroadException
            try:
                buffer = self.__socket.recv(1024).decode()
                obj = json.loads(buffer)
                m=''

                if ((obj['number_message'] > 0 or obj['bo'] == True) and obj['po']==False):
                    print('public message from '+str(obj['sender_nickname'])+',length='+str(obj['number_message'])+'\r\n'+obj['message'])
                elif obj['number_message'] > 0 and obj['bo']==False and obj['po']==True:
                    for i in obj['list_mem']:
                        m+=str(i)+', '
                    private_message='private message, length='+str(obj['number_message'])+' from '+ str(obj['sender_nickname'])+' to '+ m + ':\r\n'+str(obj['message'])
                    print(private_message)
                else:
                    print(obj['message'])

            except Exception:
                print('[Client] has error')

    def __send_message_thread(self, message,bo,number_message,list_mem,po=False):
        """
        :param message
        """
        self.__socket.send(json.dumps({
            'type': 'broadcast',
            'bo':bo,
            'po':po,
            'list_mem':list_mem,
            'number_message':number_message,
            'sender_id': self.__id,
            'message': message
        }).encode())

    def start(self):
        """
        Start the client
        """
        self.__socket.connect(('127.0.0.1', 8888))
        self.cmdloop()

    def do_Bye(self,args):
        self.__socket.send(json.dumps({
            'type': 'Bye',
            'nickname': self.__nickname,
            'id':self.__id
        }).encode())




    def do_Hello(self, args):
        """
        :param args
        """
        nickname = args.split(' ')[0]

        # Send the nickname to the server to get the user id
        self.__socket.send(json.dumps({
            'type': 'Hello',
            'nickname': nickname
        }).encode())
        # Try to accept data
        # noinspection PyBroadException

        try:
            buffer = self.__socket.recv(1024).decode()
            obj = json.loads(buffer)
            if obj['id']:
                self.__nickname = nickname
                self.__id = obj['id']

                # Open the child thread for receiving data
                thread = threading.Thread(target=self.__receive_message_thread)
                thread.setDaemon(True)
                thread.start()
                print('Hi ' + str(nickname) + ' welcome to the chat room')
            else:
                print('[Client] Can not log in to chat room')
        except Exception:
            print('[Client] Unable to get data from the server')

    def do_send(self, args):
        """
        :param args
        """
        message = args
        last=len(message)-1
        number = ''
        number_message=0
        lines=[]
        bo=False
        po=False
        number2=0
        member_private=''
        list_mem=[]

        if message =='please send the list of attendees':
            bo=False
        elif message[last]==':' and message[22]=='=':
            bo=True
            for i in range(len(message)):
                if i>=23 and i<last:
                    number+=message[i]

            number_message=int(number)
            number2=int(number)

            while number_message >0:
                line=input()
                if line and number_message> 0:
                    number_message=number_message - len(line)
                    lines.append(line)
                else:
                    break
            message='\n'.join(lines)
        elif message[last]==':' and message[23]=='=':
            bo = False
            po=True
            to=int(message.index('to'))-1
            for i in range(len(message)):
                if i >= 24 and i < to:
                    number += message[i]

            number_message = int(number)
            number2 = int(number)
            for i in range(len(message)):
                if i > to+3 and i < last:
                    member_private += message[i]


            list_mem=member_private.split(',')

            while number_message > 0:
                line = input()
                if line and number_message > 0:
                    number_message = number_message - len(line)
                    lines.append(line)
                else:
                    break
            message = '\n'.join(lines)

        else:
            bo=True


        # Open the child thread for sending data
        thread = threading.Thread(target=self.__send_message_thread, args=(message,bo,number2,list_mem,po ))
        thread.setDaemon(True)
        thread.start()

    def do_help(self, arg):
        """
        :param arg
        """
        command = arg.split(' ')[0]
        if command == '':
            print('[Help] Hello nickname - Log in to the chat room, nickname is your chosen nickname')
            print('you can write <<Hello your_name>> for login in to chat room ')
            print('and <<send message>> send message for users\nand <<Bye>> for left the chat room')
        elif command == 'Hello':
            print('[Help] Hello nickname -Log in to the chat room, nickname is your chosen nickname')
        elif command == 'send':
            print('[Help] send message - send public or private message for user')
            print('for public message you should write <<send public message, length=<your_length_message>:\n<your message>')
            print('for private message you should write <<send private message, length=<your_length_message> to <user>,<user>,...:')
            print('for show you member list you should write <<send please send the list of attendees>>')
        else:
            print('[Help] Did not find the instruction you want to know')
