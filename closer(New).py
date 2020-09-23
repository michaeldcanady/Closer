# python 3.8
import subprocess
import os
import datetime
from distutils.version import StrictVersion
from pathlib import Path

#Global Variables

_date = ''
_dateAge = ''
version = StrictVersion("0.1.10")
_filePath = os.path.splitext(__file__)[0]+'.exe'
_scriptname = Path(__file__).stem+'.exe'
_downloadDIR = '/scripts/Python'
_desktop = expanduser('~') + '\\Desktop\\'
_daniel = '543debcb6f2b02c0b075abcf9f3ee429' # Unused
_reimageBool = 0

#Methods

# Checks if the current version is great than the server version
def checkVersion():
    # checks if updater is on the desktop
    if os.path.exists(_desktop+'updater.exe'):
        os.remove(_desktop + 'updater.exe')
        return
    else:
        dl_Python('v.ersion')
        # gets current file naem
        filename = os.path.basename(__file__).split('.')
        # Checks if script is in v.ersion (server versions)
        with open('v.ersion',"r") as version_file:
            try:
                # gets current version + name
                versionLine = next(line for line in version_file if filename[0] in line)
            except StopIteration:
                print("please add {0} to v.ersion".format(__file__))
                return
            
        # removes name and converts version to a comparable format
        versionLine = StrictVersion(versionLine.split(' ')[1])
        if versionLine > version:
            if platform.system() == 'Windows':
                wUpdate()
            #else:
               #uUpdate() unused method

# Checks if device has been reimages in last 90 days
def reimage():
    global _date
    global _reimageBool
    # returns date OS was installed in format (yyyymmddHHMMSS)
    result = subprocess.check_output('WMIC OS GET installdate', universal_newlines=True)
    # Extracts date from return
    date = result.split('\n')[2].split(".")[0]
    datetime_obj = datetime.datetime.strptime(date, '%Y%m%d%H%M%S')
    print(datetime_obj)
    if datetime_obj < datetime.datetime.now() - datetime.timedelta(days=90):
        os.system('color 4f')
        print('----')
        print('  DEVICE NEEDS REIMAGE!')
        print('    Last imaged on ' + _date)
        _reimageBool = 1
        # Potential start to IPU script HERE

# deletes dir_name
def cleanup(dir_name='C:\\HelpdeskTools'):
    shutil.rmtree(dir_name)
    endFooter()

# clears screen
def clear():
    try:
        os.system('cls')
    except:
        os.system('clear')

# Checks if HelpdeskTools dir exists, creates if needed
def setup(dir_name='C:\\HelpdeskTools'):
    if os.path.isdir(dir_name) == False:
        os.mkdir(dir_name)
        print(os.path.abspath(dir_name))

# Opening to the script
def header(program_name=_scriptname):
    clear()
    line()
    print('  ' + program_name)
    print('  Designed and Written for use in Liberty IT Helpdesk')
    line()
    newLine()

# retrieves files listed in v.ersion and downloads them on to device under C:\\HelpdeskTools
def dl_Python(file_name, dir_name='C:\\HelpdeskTools'):
    urllib.urlretrieve('http://helpdesk.liberty.edu/hdtools/scripts/python/' + file_name, dir_name + '\\' + file_name)

# unused method
def wait():
    while 1:
        if kbhit():
            getch()

    return getch()

# to be removed next update
def line(num=72):
    print('-' * num)

# to be removed next update
def newLine(num=1):
    print('\n' * num)

# 
def endFooter(completion_color='a0'):
    newLine(3)
    line()
    print('  Questions / Recommendations? Talk to a T1+')
    input('  Press any key to exit')
    try:
        os.system('color ' + completion_color)
    except:
        pass
    else:
        sys.exit()

if __name__ == "__main__":
    reimage()
