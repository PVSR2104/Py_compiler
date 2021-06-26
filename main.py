import json
from os import getcwd, urandom
from kivy.uix.screenmanager import Screen
import sys 
from kivy.uix.screenmanager import  Screen
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivmob import KivMob, TestIds
from kivy.uix.label import Label
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
import helper
from random import choice



#A  classs to run all the backgroung functions(compile and save code)
class back(object):
    #to initialize the path variables dir and read the last time  code
    def __init__(self):
        self.dir = str(getcwd())
        self.code =  str(open(self.dir+"/code.txt","r",encoding="utf8",errors="ignore").read())
        self.path_output = self.dir+"/filename.txt"
    #to save the code
    def savecode(self,string,path):
        v = open(path,"w",encoding="utf8",errors="ignore")
        v.write(string)
        v.close()
        print("Code saved sucessfully")
        
    #running code and giving output
    def compile(self,path_output,string):
        try:
            ori = sys.stdout
            sys.stdout= open(path_output,"w",encoding = "utf8",errors="ignore")
            exec(string)
            sys.stdout.close()
            output = str(open(path_output,"r").read())
            sys.stdout = ori 
            print("compilation succesful")
        except Exception as e:
            #sys.stdout = ori
            output = str(e)
            print("error occured while compiling")
        try:
            out =">> "+ output.replace("\n","\n>> ")
        except:
            out= str(output)
        return out
#file manager class for saving python files in any platform
#can be used to read to
class files(back):
    def __init__(self):
        super().__init__()
        self.manager_open = False
        self.file_manager = MDFileManager(
         exit_manager=self.exit_manager,
         select_path=self.select_path,
        )
    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True
#After selecting the path if its a file it writes the content to it file
#if a folder is selected it will create a file code.py  and write the content in it into the code.py
#must  
    def select_path(self, path):
        self.exit_manager()
        toast(path)
        try:
            self.ids.input.text = str(open(path,"r",encoding="utf8",errors="ignore").read())  
            toast("openinf the file "+path)
        except IsADirectoryError:
            self.savecode(self.code,path+"/code.py")
            toast("file saved"+path+"/code.py")
        
    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()
    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
#have functionalities of compiling the program 
#it is the main one 
#main screen class to make things happen
class MainScreen(Screen,files):
    def __init__(self):
        super().__init__()

    
    def compile(self):
        print(" run button pressed")
        #initilize the object that contain the all functions
        runner = back()
        #retrive the code from the input widget
        string = self.ids.input.text
        #compile the code and send output as string , ths string is assigned to the output widget
        self.ids.output.text = runner.compile(self.path_output,string)
        #opening the terminal to show the output of program
        self.ids.backdrop.open()
        #save the present code for next time when the useer open the code 
        runner.savecode(string,self.dir+"/code.txt")




class python(MDApp):

#for changing color pallets 
    def teme(self):
        c  = choice(['Indigo', 'LightBlue', 'Teal', 'LightGreen', 'Lime', 'Amber',  'Brown', 'Gray', 'BlueGray'])
        self.theme_cls.primary_palette = c
        x = open("color.txt","w",encoding="utf8",errors="ignore")
        x.write(c)
        x.close
#main building function from the helper string
    def build(self):
        self.theme_cls.primary_palette = str(open('color.txt','r').read())
        self.theme_cls.theme_style = "Light"
        Builder.load_string(helper.helper)
        return MainScreen()



if __name__  == '__main__':
    python().run()
