import socket
import sys

class Client:
    def __init__(self):
        self.target_host = 'localhost'
        self.target_port = 9998

    def runClient(self,data:'register or login'):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.target_host, self.target_port))

        client.send(data)

        recvFromServer = client.recv(4096)

        recvFromServer= recvFromServer.decode('utf-8')
        print(type(recvFromServer))
        # print(recvFromServer)
        status , message , amount = recvFromServer.split(' ')
        # print(status,message,amount)
        if status == '201':
            print(status,message)
        elif status == '404':
            print(status,message)
        elif status == '202':
            print(status,message)
        elif status == '300':
            print(status,message,amount)
        elif status == '200':
            print('')
            print("Your info name >:{0} amount >:{1}".format(message,amount))
            print("Menu :")
            while True:
                option = input("Press 3 to deposit :\nPress 4 to Withdraw :\nPress 5 to Transfer :\nPress 6 to Exit :\nPress 7 to go back RG & LG :")
                if option == '3':
                    d_amount = input("Please Enter amount :")
                    data = option+' '+message+' '+amount+' '+d_amount+' '+'0'
                elif option == '4':
                    w_amount = input("Please enter amount to withdraw :")
                    option = '4'
                    data = option+' '+message+' '+amount+' '+w_amount+' '+'0'
                elif option == '5':
                    t_username = input("Please enter username to transfer :")
                    t_useramount = input("Please enter amount to transfer :")
                    data = option+' '+message+' '+amount+' '+t_useramount+' '+t_username
                elif option == '6':
                    sys.exit("Thank_For_Using")
                elif option == '7':
                     break
                try:
                    data = bytes(data,'utf-8')
                    self.runClient(data)
                except Exception as err:
                    print(err)
                    print('')

        client.close()

    def option(self):
        print('')
        option = input("[+]Press-1 to Register:\n[+]Press-2 to Login:\n[+]Press-3 to exit :")
        if option=='1':
            r_name = input("Enter username to Register=>:")
            r_pw = input("Enter password to Register=>:")
            r_pw2 = input("Enter password again to confirm=>:")
            if r_pw == r_pw2:
                r_amount = input("Please enter your money :")
                r_allData=option+' '+r_name+' '+r_pw+' '+r_amount+' '+'0'
                r_allData:bytes = bytes(r_allData,'utf-8')
                self.runClient(r_allData)
        elif option=='2':
            l_name = input("Enter username to Login=>:")
            l_pw = input("Enter password to Login=>:")
            l_all_data= option+' '+l_name+' '+l_pw+' '+'0'+' '+'0'
            l_all_data:bytes = bytes(l_all_data,'utf-8')
            self.runClient(l_all_data)
        elif option=='3':
            sys.exit("Thank_For_Using")

if __name__ == "__main__":
    tcpClient:Client=Client()
    while True:
        tcpClient.option()