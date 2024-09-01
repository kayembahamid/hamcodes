import cmd

import paramiko

def ssh_command(ip, port, user, passwd, cmd):   #1
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #2
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd) #3
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- output ---')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    import getpass  # 4
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()

    ip = input('Enter server IP: ') or '192.168.1.203'
    port = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)




