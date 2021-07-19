import json
from os import getcwd, urandom
from kivy.uix.screenmanager import Screen
import sys 
from kivy.uix.screenmanager import  Screen
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivymd.toast import toast
import helper
from concurrent.futures import ThreadPoolExecutor
from random import choice

#A  classs to run all the backgroung functions(compile and save code)
class back(object):
    #to initialize the path variables dir and read the last time  code
    def __init__(self):
        f= open('data.json','r')
        self.jdata = json.load(f)
        f.close()
        self.code = self.jdata['code']
        self.dir = str(getcwd())
        self.path_output = self.dir+"/output.txt"
    #to save the code
    def savedata(self,value,key):
        file = open("data.json",'w')
        self.jdata[str(key)] = str(value)
        j  = json.dumps(self.jdata,indent=4)
        file.write(str(j))
        file.close()
        print("Code saved sucessfully")

    #running code and giving output
    def compile_code(self,path_output,string):
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

#have functionalities of compiling the program 
#it is the main one 
#main screen class to make things happen
class MainScreen(Screen,back):
    
    def folder(self):
        x = files()
        x.file_manager_open() 
        self.ids.input.text = x.code
    
    def compile(self):
        print(" run button pressed")
        #initilize the object that contain the all functions
        runner = back()
        #retrive the code from the input widget
        string = self.ids.input.text
        #displaying message for user to wait if compilation takes more time
        self.ids.output.text = "Code is started compiling"
        #opening the terminal to show the output of program
        self.ids.backdrop.open()
        #compile the code and send output as stringths string is assigned to the output widget
        # using concurrent.future.Threadpoolexecutionor for multiprocessing
        #multiprcess is used so that the execution process doesnt effect the the kivy gui
        E = ThreadPoolExecutor()
        out = E.submit(runner.compile_code,self.path_output,string)
        self.ids.output.text = str(out.result())
        #self.ids.output.text = self.compile_code(self.path_output,string)
        #save the present code for next time when the useer open the code 
        runner.savedata(string,'code')
       




class python(MDApp,back):


#for changing color pallets 
    def teme(self):
        c = choice(['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray'])    
        self.theme_cls.primary_palette = c
        self.savedata(c,'color')
#main building function from the helper string
    def build(self):
        self.theme_cls.primary_palette = self.jdata['color']
        self.theme_cls.theme_style = "Light"
        Builder.load_string(helper.helper)
        return MainScreen()



if __name__  == '__main__':
    python().run()
