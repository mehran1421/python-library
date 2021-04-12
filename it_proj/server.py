import socket
import threading
import json


class Server:
    def __init__(self):
        """
        constractor
        """
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connections = list()
        self.__nicknames = list()
        self.__isActive=list()

    def __user_thread(self, user_id):
        """
        for join user
        :param user_id: user_id
        """
        connection = self.__connections[user_id]
        nickname = self.__nicknames[user_id]
        print('[Server] Hello', nickname)
        # length ==-1 for welcome to member
        self.__broadcast(user_id=user_id,message= str(nickname) + ' join the chat room',length=0)

        # Listen for ever
        while True:
            # noinspection PyBroadException
            try:
                buffer = connection.recv(1024).decode()
                # Parse into json data
                obj = json.loads(buffer)
                chat_list=''
                # If it is a broadcast instruction
                if obj['type'] == 'broadcast' and obj['message'] == 'please send the list of attendees':
                    self.__broadcast(obj['sender_id'], 'Here is the list of attendees',length=-1)
                    for j in range(len(self.__nicknames)):
                        chat_list+=str(self.__nicknames[j])+','

                    self.__broadcast(obj['sender_id'], chat_list,length=-1)

                elif obj['type'] == 'Bye':
                    self.__nicknames.remove(obj['nickname'])
                    self.__broadcast(message=str(obj['nickname']) + ' left the chat room', length=0)
                    self.__isActive[obj['id']]=0

                elif obj['type'] == 'broadcast' and obj['bo']==True:
                    self.__broadcast(obj['sender_id'], obj['message'],obj['number_message'])
                elif obj['type'] == 'broadcast' and obj['bo'] == False and obj['po']==True:
                    self.__broadcast(obj['sender_id'], obj['message'],obj['number_message'],bo=False,lister=obj['list_mem'],po=obj['po'])
                else:
                    print('[Server] Unable to parse json packet:', connection.getsockname(), connection.fileno())
            except Exception:
                print('[Server] Connection failure:', connection.getsockname(), connection.fileno())
                self.__connections[user_id].close()
                self.__connections[user_id] = None
                self.__nicknames[user_id] = None

    def __broadcast(self, user_id=0, message='',length=0,bo=False,lister=[],po=False):
        """
        broadcast
        :param user_id
        :param message
        """
        for i in range(1, len(self.__connections)):
            if self.__isActive[i]==1:
                if ((length >=0 or bo==True) and po==False):
                    self.__connections[i].send(json.dumps({
                        'sender_id': user_id,
                        'sender_nickname': self.__nicknames[user_id],
                        'bo':bo,
                        'message': message,
                        'number_message': length,
                        'list_mem':lister,
                        'po':po
                    }).encode())
                elif length>=0 and po==True:
                    if self.__nicknames[i] in lister:
                        self.__connections[i].send(json.dumps({
                            'sender_id': user_id,
                            'sender_nickname': self.__nicknames[user_id],
                            'bo':bo,
                            'message': message,
                            'number_message': length,
                            'list_mem': lister,
                            'po': po
                        }).encode())

                else:
                    if user_id == i:
                        self.__connections[i].send(json.dumps({
                            'sender_id': user_id,
                            'sender_nickname': self.__nicknames[user_id],
                            'message': message,
                            'number_message': length,
                            'bo':bo,
                            'list_mem': lister,
                            'po': po
                        }).encode())

    def start(self):
        """
        Start the server
        """
        # Binding port
        self.__socket.bind(('127.0.0.1', 8888))
        # Enable monitoring
        self.__socket.listen(10)
        print('[Server] Server is running......')

        # Clear connection
        self.__connections.clear()
        self.__nicknames.clear()
        self.__isActive.clear()
        self.__connections.append(None)
        self.__isActive.append(1)
        self.__nicknames.append('System')

        # Start listening
        while True:
            connection, address = self.__socket.accept()
            print('[Server] Received a new connection', connection.getsockname(), connection.fileno())

            # noinspection PyBroadException
            try:
                buffer = connection.recv(1024).decode()
                # Parse into json data
                obj = json.loads(buffer)
                # If it is a connection instruction, then a new user number is returned to receive the user connection
                if obj['type'] == 'Hello':
                    self.__connections.append(connection)
                    self.__nicknames.append(obj['nickname'])
                    self.__isActive.append(1)
                    connection.send(json.dumps({
                        'id': len(self.__connections) - 1
                    }).encode())

                    # Open a new thread
                    thread = threading.Thread(target=self.__user_thread, args=(len(self.__connections) - 1, ))
                    thread.setDaemon(True)
                    thread.start()
                else:
                    print('[Server] Unable to parse json packet:', connection.getsockname(), connection.fileno())
            except Exception:
                print('[Server] Unable to accept data:', connection.getsockname(), connection.fileno())
