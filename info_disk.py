import sys
import subprocess

# получение результатов из командной строки
def console(command):
    reply = subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, encoding='utf-8')
    
    if reply.returncode is not 0:
        return reply.stderr
    else:
        return reply.stdout

file = open(sys.argv[1], 'r').readline().rstrip('\n')
command = ['lsblk', '{}'.format(file), '-d', '-p', '-l', '-n', '-o', 'NAME,TYPE,SIZE']
disk_info = console(command)

if 'disk' in str(disk_info):
    sys.stdout.write(disk_info)
else:
    command = ['df', '-h', '-T', '{}'.format(file)]
    info_extra = console(command)
    non_head = info_extra.split('\n')[1]
    info_array = non_head.split()
    print(disk_info.split('\n')[0] + ' ' +  '{0} {1} {2}'.format(info_array[1], info_array[4], info_array[6]))



