
import argparse
import os
import sys
import time
def first():
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')
    parser.add_argument('-e', action='store', dest='environment',help='Specified environment')
    parser.add_argument('-p', action='store', dest='platform',help='Specified a platform')
    parser.add_argument('-job', action='store',dest='project', help='Specified a project name')
    parser.add_argument('-version', action='version', version='%(prog)s 1.0')
    results = parser.parse_args()
    environment = results.environment
    platform = results.platform
    project = results.project

class Tomcat(object):

    def __init__(self,path,name,command):
        self.path = path
        self.name = name
        self.command = command

    def Start(self):
        print('%s %s %s' % (self.path, self.name, self.command))
        dir = os.path.join(self.path,self.name,'bin\catalina.sh')
        try:
            os.popen(dir + self.command).readlines()
        except os.error as cc:
            print('Exception:',cc)

        return 1

    def Stop(self):
        print('%s %s %s' % (self.path, self.name,self.command))
        dir = os.path.join(self.path, self.name, 'bin\catalina.sh')
        try:
            os.popen('ps -ef|grep %s/conf|grep -v grep|xargs kill -9 ' %(dir))
        except os.error as cc:
            print(cc)

        return 1

    def Restart(self):
        print('%s %s %s' % (self.path, self.name,self.command))
        StopTom.Stop()
        StopTom.Start()

        return 1

    def backUPapp(self):
        print('%s %s' % (self.path, self.name))
        source = os.path.join(self.path, self.name)
        target = 'E:\win-10\caches\\'
        uptime = time.strftime("%Y%m%d_%H:%M:%S", time.localtime())
        zip_command = "zip -qr %s%s.zip %s" % (target,uptime,source)
        os.popen(zip_command)

if __name__ == '__main__':

    StopTom = Tomcat('E:\win-10\\','caches','stop')
    StopTom.Start()