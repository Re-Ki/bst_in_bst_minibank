import socket
class Node:
    def __init__(self,data):
        self.CharAlphbet=data
        self.c_right=None
        self.c_left=None

def dataInsertion():
    root = Node('p')

    root.c_left = Node('h')
    root.c_left.c_left = Node('d')
    root.c_left.c_right = Node('l')
    root.c_left.c_left.c_left = Node('b')
    root.c_left.c_left.c_right = Node('f')
    root.c_left.c_right.c_left = Node('j')
    root.c_left.c_right.c_right = Node('n')
    root.c_left.c_left.c_left.c_left = Node('a')
    root.c_left.c_left.c_left.c_right = Node('c')
    root.c_left.c_left.c_right.c_left = Node('e')
    root.c_left.c_left.c_right.c_right = Node('g')

    root.c_left.c_right.c_left.c_left = Node('i')
    root.c_left.c_right.c_left.c_right = Node('k')
    root.c_left.c_right.c_right.c_left = Node('m')
    root.c_left.c_right.c_right.c_right = Node('o')

    root.c_right = Node('t')
    root.c_right.c_left = Node('r')

    root.c_right.c_right = Node('x')

    root.c_right.c_left.c_left = Node('q')
    root.c_right.c_left.c_right = Node('s')

    root.c_right.c_right.c_left = Node('v')
    root.c_right.c_right.c_right = Node('y')

    root.c_right.c_right.c_left.c_left = Node('u')
    root.c_right.c_right.c_left.c_right = Node('w')

    root.c_right.c_right.c_right.c_right = Node('z')
    return root

class LenghtBST:
    def __init__(self,data):
        self.data=data
        self.info=[]
        self.infoPw=[]
        self.amount_info=[]
        self.left=None
        self.right=None

def RootLengthTree():
    root=None
    list_length=[16,8,24,4,12,20,28,2,6,10,14,18,22,26,29,1,3,5,7,9,11,13,15,17,19,21,23,25,27,30]
    length=len(list_length)
    print(length)

    for i in range(0,length):
        print("data",list_length[i])
        root = insert(root,list_length[i])
    return root

def insert(node, key):
    # Return a new node if the tree is empty
    if node is None:
        return LenghtBST(key)
    # Traverse to the right place and insert the node
    if key < node.data:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

class TCPserver:
    def __init__(self):
        self.server_ip='localhost'
        self.server_port = 9998
        self.sock = None
        self.AlphaRoot = dataInsertion()
        self.RLTroot = RootLengthTree()
        if self.AlphaRoot:
            print('AlphaDatabase created!')
            self.inorderForAlpha(self.AlphaRoot)
            print('\n')
        if self.RLTroot:
            print('[+][+] Root length tree created')
            self.inorderForRLT(self.RLTroot)
            print('\n')

    def inorderForRLT(self,RLTroot):
        if RLTroot is not None:
            self.inorderForRLT(RLTroot.left)
            print(RLTroot.data,' >',end=' ')
            self.inorderForRLT(RLTroot.right)

    def inorderForAlpha(self,AlphaRoot):
        if AlphaRoot is not None:
            self.inorderForAlpha(AlphaRoot.c_left)
            print(AlphaRoot.CharAlphbet,' >',end=' ')
            self.inorderForAlpha(AlphaRoot.c_right)


    def main(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen(1)
        print(f'[*] Listening on {self.server_ip}:{self.server_port} >:')
        while True:
            client, address = server.accept()
            print(f'[*] Accepted connection from {address[0]}:{address[1]}')
            self.handle_client(client)

    def handle_client(self,client):
        with client as self.sock:
            request = self.sock.recv(4096)
            client_sms=request.decode("utf-8")
            print(f'[*] Received:',client_sms)
            option , c_uname , c_pw , c_amount ,tran_name = client_sms.split(' ')
            if option=='1':
                print("This is for registration")
                success = self.forRegistration(c_uname,c_pw,c_amount)
                print('Testing for :',success)
                if success == 'notsuccess':
                    data = '201'+' '+'Your_Data_is_Already_exit_!'+' '+'0'
                    data = bytes(data,'utf-8')

                    self.sock.send(data)
                else:
                    data = '201' + ' ' + 'SuccessRegistration'+' '+'0'
                    data = bytes(data, 'utf-8')

                    self.sock.send(data)
            elif option == '2':
                self.loginAlpha(c_uname,c_pw)
            elif option == '3':
                self.Deposit(self.RLTroot,c_uname,c_pw,c_amount)
            elif option == '4':
                self.Withdraw(self.RLTroot,c_uname,c_pw,c_amount)
            elif option == '5':
                self.transfer(self.RLTroot,c_uname,c_pw,c_amount,tran_name)
            elif option == '6':
                self.delete(self.RLTroot,tran_name)


    def forRegistration(self,uname , pw,amount):

        uname  = uname.lower()
        firstData =uname[0]

        Length =len(uname)
        success =self.searchInAlpha(self.AlphaRoot, uname, firstData,Length,pw,amount)
        print('for registartion function',success)
        return success
    def searchInAlpha(self,AlphaRoot, uname , firstData , Lenght , pw , amount):
        success = None
        alphaNo =ord(AlphaRoot.CharAlphbet)
        firstNo = ord(firstData)
        if AlphaRoot is None:
            print('Alpha root is empty cannot be proceed!')
        if AlphaRoot.CharAlphbet == firstData:
            print("Alpha was found : ",AlphaRoot.CharAlphbet)
            success =self.insertInRLT(self.RLTroot,Lenght,uname,pw,amount)
            print('Return from insertInRLT:',success)
            success = success
            return success
        elif alphaNo < firstNo :
            return self.searchInAlpha(AlphaRoot.c_right , uname , firstData , Lenght ,pw,amount)
        elif alphaNo > firstNo:
            return self.searchInAlpha(AlphaRoot.c_left, uname, firstData, Lenght, pw,amount)

    def insertInRLT(self,RLTroot , Lenght , uname , pw ,amount):
        flag = None
        if RLTroot is None:
            print('RLT root is empty cannot be proceed!')
        if RLTroot.data == Lenght:
            infoLength = len(RLTroot.info)
            print("infoLength :",infoLength)
            if infoLength == 0:
                RLTroot.info.append(uname)
                RLTroot.infoPw.append(pw)
                RLTroot.amount_info.append(amount)
                print(RLTroot.info)
                print(RLTroot.infoPw)
                print(RLTroot.amount_info)
                user_amount = RLTroot.amount_info
                flag = 'success'
                return flag
            else:
                for i in RLTroot.info:
                    if i == uname:
                        print("Your Data is Already exit !")
                        flag = 'notsuccess'
                        return flag
                RLTroot.info.append(uname)
                RLTroot.infoPw.append(pw)
                RLTroot.amount_info.append(amount)
                print(RLTroot.info)
                print(RLTroot.infoPw)
                print(RLTroot.amount_info)
                user_amount = RLTroot.amount_info
                flag = 'success'
                return flag
        if RLTroot.data < Lenght :
            return self.insertInRLT(RLTroot.right, Lenght , uname ,pw ,amount)
        elif RLTroot.data > Lenght:
            return self.insertInRLT(RLTroot.left, Lenght , uname ,pw , amount)

    def loginAlpha(self,uname , pw ):
        uname  = uname.lower()
        firstData =uname[0]
        Length = len(uname)
        self.login_SearchInAlpha(self.AlphaRoot , uname , firstData , Length ,pw )

    def login_SearchInAlpha(self,AlphaRoot , uname , firstData , Lenght , pw):
        alphaNo = ord(AlphaRoot.CharAlphbet)
        firstNo = ord(firstData)
        if AlphaRoot is None:
            print('Alpha root is empty cannot be proceed!in Login!')
        if AlphaRoot.CharAlphbet == firstData:
            print("Alpha was found : ", AlphaRoot.CharAlphbet)
            self.login_serachinRLT(self.RLTroot, Lenght, uname, pw)

        elif alphaNo < firstNo:
            return self.login_SearchInAlpha(AlphaRoot.c_right, uname, firstData, Lenght, pw)
        elif alphaNo > firstNo:
            return self.login_SearchInAlpha(AlphaRoot.c_left, uname, firstData, Lenght, pw)

    def login_serachinRLT(self,RLTroot , Length , uname , pw ):
        flag =None
        if RLTroot is None:
            print('RLT root is empty cannot be proceed! in Login!')
        if RLTroot.data == Length:
            print('from Login_searchinRLT:',RLTroot.data )
            InfoNameLength = len(RLTroot.info)
            for i in range(0,InfoNameLength):
                if RLTroot.info[i] == uname and RLTroot.infoPw[i]==pw :
                    print("Login Success for User:",RLTroot.info[i])
                    print(RLTroot.info[i])
                    print(RLTroot.amount_info[i])
                    data = '200'+' '+RLTroot.info[i]+' '+RLTroot.amount_info[i]
                    data = bytes(data,'utf-8')
                    print(data)
                    flag=True
                    break

            if flag:
                self.sock.send(data)
            else:
                data = '404' + ' ' + 'Login_Failed' + ' ' + '0'
                data = bytes(data, 'utf-8')
                self.sock.send(data)

        elif RLTroot.data < Length :
            return self.login_serachinRLT(RLTroot.right, Length , uname ,pw )
        elif RLTroot.data > Length:
            return self.login_serachinRLT(RLTroot.left, Length , uname ,pw )

    def Deposit(self,RLTroot,o_name,o_amount,d_amount):
        length = len(o_name)
        if RLTroot is None:
            return RLTroot
        if RLTroot.data == length:
            InfoNameLength = len(RLTroot.info)
            for i in range(0,InfoNameLength):
                if RLTroot.info[i] == o_name:
                    o_amount = int(o_amount)
                    d_amount = int(d_amount)
                    temp = o_amount + d_amount
                    RLTroot.amount_info[i] = str(temp)
                    print("testing_D :",RLTroot.amount_info[i])
                    result = RLTroot.amount_info[i]
                    data = '300' + ' ' +o_name+ ' ' + result
                    data = bytes(data, 'utf-8')
                    self.sock.send(data)
        elif RLTroot.data < length:
            return self.Deposit(RLTroot.right,o_name,o_amount,d_amount)
        elif RLTroot.data > length:
            return self.Deposit(RLTroot.left,o_name,o_amount,d_amount)

    def Withdraw(self,RLTroot,o_name,o_amount,w_amount):
        length = len(o_name)
        o_amount = int(o_amount)
        w_amount = int(w_amount)
        if RLTroot is not None:
            if RLTroot.data == length:
                info_nameLength = len(RLTroot.info)
                for i in range(0, info_nameLength):
                    if RLTroot.info[i] == o_name:
                        if o_amount >= w_amount:
                            temp=o_amount - w_amount
                            print("temp :",temp)
                            RLTroot.amount_info[i] = str(temp)
                            print("testing_W :", RLTroot.amount_info[i])
                            result = RLTroot.amount_info[i]
                            data = '300' + ' ' + o_name + ' ' + result
                            data = bytes(data, 'utf-8')
                            self.sock.send(data)
                        else:
                            o_amount = str(o_amount)
                            data = '300'+' '+'Your_have_not_enough_money'+' '+o_amount
                            data = bytes(data,'utf-8')
                            self.sock.send(data)
            elif RLTroot.data < length:
                return self.Withdraw(RLTroot.right, o_name, o_amount, w_amount)
            elif RLTroot.data > length:
                return self.Withdraw(RLTroot.left, o_name, o_amount, w_amount)

    def transfer(self,RLTroot,o_name,o_amount,t_amount,t_name):
        o_length = len(o_name)
        o_amount = int(o_amount)
        t_amount = int(t_amount)
        if RLTroot is not None:
            if RLTroot.data == o_length:
                info_nameLength = len(RLTroot.info)
                for i in range(0,info_nameLength):
                    if RLTroot.info[i] == o_name:
                        if o_amount >= t_amount:
                            temp = o_amount-t_amount
                            print("temp :",temp)
                            RLTroot.amount_info[i] = str(temp)
                            print("testing_T :",RLTroot.amount_info[i])
                            update = self.update_transfer_user(self.RLTroot, t_amount, t_name)
                            print("transfer user_amount :",update)
                            result = RLTroot.amount_info[i]
                            data = '300'+' '+o_name+' '+result
                            data = bytes(data,'utf-8')
                            self.sock.send(data)
                        else:
                            o_amount = str(o_amount)
                            data = '300'+' '+'Your_have_not_enough_money'+' '+o_amount
                            data = bytes(data,'utf-8')
                            self.sock.send(data)
            elif RLTroot.data < o_length:
                return self.transfer(RLTroot.right,o_name,o_amount,t_amount,t_name)
            elif RLTroot.data > o_length:
                return self.transfer(RLTroot.left,o_name,o_amount,t_amount,t_name)

    def update_transfer_user(self,RLTroot,t_amount,t_name):
        Length = len(t_name)
        t_amount = int(t_amount)
        if RLTroot is not None:
            if RLTroot.data == Length:
                info_nameLength = len(RLTroot.info)
                for i in range(0,info_nameLength):
                    if RLTroot.info[i] == t_name:
                        amount = RLTroot.amount_info[i]
                        amount = int(amount)
                        print("old amount :",amount)
                        print("add amount :",t_amount)
                        amount = t_amount+amount
                        RLTroot.amount_info[i] = str(amount)
                        return amount
            elif RLTroot.data < Length:
                return self.update_transfer_user(RLTroot.right,t_amount,t_name)
            elif RLTroot.data > Length:
                return self.update_transfer_user(RLTroot.left,t_amount,t_name)

if __name__ == "__main__":
    tcpServer :TCPserver =TCPserver()
    tcpServer.main()