"""
@Program Name: Yo-Shell V1 Starter Code
@Author: Pavan Kumar Duppala
@Description:
    This code is a barebones snippet to get your shell up and running. It provides the following classes 
    (each of which is not fully implemented):
          historyManager - manages a history of commands
          parserManager - handles parsing of commands into command , arguments, flags
          commandManager - gets commands parsed and then runs appropriate functions for command
          driver - drives the entire shell
"""

import os
import sys
import time
import getpass
"""
@Name: historyManager
@Description:
    Maintains a history of shell commands to be used within a shell environment.
@Methods:
    push_command - add command to history
    get_commands - get all commands from history
    number_commands - get number of commands in history
"""
class historyManager(object):
    def __init__(self):
        self.command_history = []

    """
    @Name: push_command
    @Description:
        Add command to history
    @Params:
        cmd (string) - Command added to history
    @Returns: None
    """
    def push_command(self,cmd):
        self.command_history.append(cmd)
        
    """
    @Name: get_commands
    @Description:
        get all commands from history
    @Params: None
    @Returns: None
    """
    def get_commands(self):
        print(self.command_history)
        return self.command_history
        
    """
    @Name: number_commands
    @Description:
        get number of commands in history
    @Params: None
    @Returns: 
        (int) - number of commands
    """
    def number_commands(self):
        return len(self.command_history)

"""
@Name: parserManager
@Description:
    Handles parsing of commands into command , arguments, flags.
@Methods:
    parse - does actual parsing of command
"""
class parserManager(object):
    def __init__(self):
        self.parts = []
    """
    @Name: parse
    @Description:
        Parses command into a list (right now). 
    @Params: 
        cmd (string) - The command to be parsed
    @Returns: 
        (int) - number of commands
    """
    def parse(self,cmd):
        self.parts = cmd.split(" ")
        return self.parts
          
"""
@Name: commandManager
@Description:
    Maintains a history of shell commands to be used within a shell environment.
@Methods:
    run_command - Runs a parsed command
    ls - Directory_listing
    cat - File dump
"""
class commandManager(parserManager):
    """
    def __init__(self):
        self.command = None	
    """

    """
    @Name: run_command
    @Description:
        Runs a parsed command
    @Params: 
        cmd (string) - The command
    @Returns: 
        (list) - With the command parts (It shouldn't return the list, it should RUN the appropriate command from this method.
    """
    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command
       

    """
    @Name: ls
    @Description:
        Does a directory listing
    @Params: 
        dir (string) - The directory to be listed
    @Returns: None
    """

    def ls(self,str):
       if str is None:
           for dirname, dirnames, filenames in os.walk('.'):
            # print path to all subdirectories first.
               for subdirname in dirnames:
                   print(os.path.join(dirname, subdirname))


            # print path to all filenames.
           for filename in filenames:
                print(os.path.join(dirname, filename))


    """
    @Name: cat
    @Description:
        Dumps a file
    @Params: 
        file (string) - The file to be dumped
    @Returns: None
    """    
    def cat(self,file):
        f = open(file,'r')
        print(f.read())
    """
    @Name: chmod
    @Description:
        changes the filepermissions of a file
    @Params:
        fd-file name
        mode-numeric mode
    @Returns: None
    """
    
    def chmod(self,fd,mode):
        print(fd)
        fd1=os.open(fd,os.O_RDONLY)
        os.fchmod(fd1,mode)
        print('permissions changed as required') 
    """
    @Name: cp
    @Description:
        copies one file into other
    @Params:
        f1 (string) - The file to be copied from
        f2 (string)-  The file to be copied into
    @Returns: None
    """

    def cp(self,f1,f2):
        f2=open(f2,"w")
       
        with open(f1) as openfileobject:
           for line in openfileobject:
               f2.write(line)
    """
    @Name: history
    @Description:
        displays the history of all the commands
    @Params:
        None
    @Returns: None
    """

    def history(self):
        self.commands = commandManager()
        username=getpass.getuser()
        path='/home/'+username+'/.bash_history'
        self.commands.cat(path)
    def touch(self,fname):
        try:
            os.utime(fname, None)
            print('file created')
            return fname
        except:
            open(fname, 'a').close()    
    """
    @Name: mv
    @Description:
        moves  a file ,removes the origin file,retains the destination file
    @Params:
        org (string) - The file to be moved from
        dest (string)-  The file to be moved into

    @Returns: None
    """
    
    def mv(self,org,dest):
        self.commands = commandManager()
 
        self.dest1=self.commands.touch(dest)
        os.rename(org,self.dest1)
    """
    @Name: wc
    @Description:
         gives the word count of a file     
    @Params:
        filename:the file is given as input for which the word count is done

    @Returns: None
    """

    def wc(self,filename):
        count=0
        with open(filename) as fileobject:
            for line in fileobject:
                count+=1
        print(count)
    """
    @Name: wcl
    @Description:
         gives the line count of a file
    @Params:
        filename:the file is given as input for which the line count is done

    @Returns: None
    """


    def wcl(self,str,f1):
        count=0
        with open(f1) as fileobject:
            for word in fileobject:
                words=word.split()
        #print(words)
                count=count+len(words)+1
        print(count)
    """
    @Name: rm
    @Description:
        removes a filefrom a directory
    @Params:
        filename (string) - The file to be removed
    @Returns: None
    """

    def rm(self,filename):
        os.remove(filename) 
        print('file is removed')
    """
    @Name: cd
    @Description:
        changes or moves into a directory mentioned
    @Params:
        dirname(string) - the directory into which to be moved in
    @Returns: None
    """

    def cd(self,dirname):
        username=getpass.getuser()
        cwd=os.getcwd()
        
        path=cwd+'/'+dirname
        print(path)
        os.chdir(path)
        cwd=os.getcwd()
        print(cwd)
    """
    @Name: cdp
    @Description:
        changes or moves into a previous directory 
    @Params:
        None
    @Returns: None
    """
    def cdp(self):
        os.chdir('..')
        cwd=os.getcwd()
        print(cwd)
	
    """
    @Name: cdh
    @Description:
        changes or moves into a home  directory 
    @Params:
        None
    @Returns: None
    """	
    def cdh(self):
        os.chdir('/home')
        cwd.os.getcwd()
        print(cwd)
    """
	@Name: lsf
    @Description:
        used to return the directory listing   
    @Params:
        None
    @Returns: return the list(directory listing)
    """

    def lsf(self):
        username=getpass.getuser()
        cwd=os.getcwd()

        path=cwd

        
        dirs = os.listdir( path )
        f1=[]
# This would print all the files and directories
        for file in dirs:
            f=[]
            f.append(file)

            fileinfo=os.stat(file)
            filesize=fileinfo.st_size
            f.append(filesize)
            mode=oct(os.stat(file).st_mode)[4:]
            f.append(mode)
   
            accesstime=os.stat(file).st_atime
            actime=time.strftime("%a, %d %b %Y %H:%M:%S ",time.localtime(accesstime))
            f.append(actime)
            modifiedtime=os.stat(file).st_mtime
            mdtime=time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(modifiedtime))
            f  .append(mdtime)
            changedtime=os.stat(file).st_ctime
            cdtime=time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime(changedtime))
            f.append(cdtime)

            f1.append(f)

        return f1
    """
    @Name: lsl
    @Description:
        used to perform directory listing
    @Params:
        str(string):flag 
        listt:the list on which directory listing to be performed
    @Returns: None
    """

    def lsl(self,str,listt):
        print("filename\t"+"size\t\t"+"permissions\t"+"accessed time\t\t\t\t"+"modified time\t\t\t\t"+"changed time")
        for f in listt:
            for x in f:

                print(x,end="\t\t")
        print()
    """
    @Name: lss
    @Description:
        used to perform sorted  directory listing based on size
    @Params:
        
        listt:the list on sorting to be performed
    @Returns: None
    """

    def lss(self,listt):
        list1=sorted(listt,key=lambda l:l[1])
        print()
        print()
        print("filename\t"+"size\t\t"+"permissions\t"+"accessed time\t\t\t\t"+"modified time\t\t\t\t"+"changed time")

        for f in list1:
            for x in f:
                print(x,end="\t\t")
    """
    @Name: lsa
    @Description:
        used to perform sorted  directory listing based on acess time
    @Params:

        listt:the list on sorting to be performed
    @Returns: None
    """
 
    def lsa(self,listt):
        list1=sorted(listt,key=lambda l:l[3])
        print()
        print()
        print("filename\t"+"size\t\t"+"permissions\t"+"accessed time\t\t\t\t"+"modified time\t\t\t\t"+"changed time")

        print("the sorted list according to access time  is :")
        for f in list1:
            for x in f:
                print(x,end="\t\t")
    """
    @Name: lsm
    @Description:
        used to perform sorted  directory listing based on modified time
    @Params:

        listt:the list on sorting to be performed
    @Returns: None
    """

    def lsm(self,listt):
        list1=sorted(listt,key=lambda l:l[4])
        print()
        print()
        print("filename\t"+"size\t\t"+"permissions\t"+"accessed time\t\t\t\t"+"modified time\t\t\t\t"+"changed time")

        print("the sorted list according to access time  is :")
        for f in list1:
            for x in f:
                print(x,end="\t\t")
    """
    @Name: lsc
    @Description:
        used to perform sorted  directory listing based on changed time
    @Params:

        listt:the list on sorting to be performed
    @Returns: None
    """

    def lsc(self,listt):
        list1=sorted(listt,key=lambda l:l[5])
        print()
        print()
        print("filename\t"+"size\t\t"+"permissions\t"+"accessed time\t\t\t\t"+"modified time\t\t\t\t"+"changed time")
        for f in list1:
            for x in f:
                print(x,end="\t\t")

"""
@Name: driver
@Description:
    Drives the entire shell environment
@Methods:
    run_shell - Loop that drives the shel environment
"""
class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0
        
    """
    @Name: runShell
    @Description:
        Loop that drives the shel environment
    @Params: None
    @Returns: None
    """ 
    def runShell(self):
        number_commands = 0
        while True:
            self.input = input("parser-$ ")         # get command
            self.history.push_command(self.input)   # put in history
            parts = self.commands.run_command(self.input)
            for x in parts:
                if x=='cat':
                    i=parts.index(x)
                    i+=1
                    self.commands.cat(parts[i])
                elif x=='ls':
                    i=len(parts)
                    j=parts.index(x)
                    if(i==1):
                        self.commands.ls(None)
                    else:
                        j+=1
                        str=parts[j]
                        print(str)
                        if(str=='-l'):
                                 
                            list1=self.commands.lsf()
                            self.commands.lsl(str,list1)
                        elif str=='-s':
                              list1=self.commands.lsf()
                              self.commands.lss(list1)
                        elif str=='-a':
                              list1=self.commands.lsf()
                              self.commands.lsa(list1)
                        elif str=='-m':
                             list1=self.commands.lsf()
                             self.commands.lsm(list1)
                        elif str=='-c':
                             list1=self.commands.lsf()
                             self.commands.lsc(list1)
                elif x=='chmod':
                    j=parts.index(x)
                    j+=1
                    mod=parts[j]
                    mod1=int(mod,8)
                    j+=1
                    fil=parts[j]
                    self.commands.chmod(fil,mod1)
                elif x=='cp':
                    j=parts.index(x)
                    j+=1
                    f1=parts[j]
                    j+=1
                    f2=parts[j]
                    self.commands.cp(f1,f2)
                elif x=='mv':
                    j=parts.index(x)
                    j+=1
                    f1=parts[j]
                    j+=1
                    f2=parts[j]
                    self.commands.mv(f1,f2)
                elif x=='history':
                    self.commands.history() 
                elif x=='wc':
           
                    j=parts.index(x)
                    j+=1
                    str=parts[j]
                    if(str=='-l'):
                        j+=1
                        f2=parts[j]
                        print(f2)
                        self.commands.wcl(str,f2)
                    else:
                        self.commands.wc(str)   
                elif x=='rm':
                    j=parts.index(x)
                    j+=1
                    str=parts[j]
                    self.commands.rm(str) 
                elif x=='cd':
                    j=parts.index(x)
                    j+=1
                    str=parts[j]
                    self.commands.cd(str)
               	elif x =='cd..':
                    self.commands.cdp()
                elif x == 'cd~':
                    self.commands.cdh()
            print(parts)


if __name__=="__main__":
    d = driver()    
    d.runShell()

