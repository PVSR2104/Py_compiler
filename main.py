from os import getcwd
from kivy.uix.screenmanager import Screen
import sys 
from kivy.uix.screenmanager import  Screen
from kivymd.app import MDApp
from kivy.lang.builder import Builder
import helper
#A  classs to run all the backgroung functions(compile and save code)
class back(object):
    #to initialize the path variables dir and read the last time  code
    def __init__(self):
        self.dir = str(getcwd())
        self.code =  str(open(self.dir+"/code.txt","r",encoding="utf8",errors="ignore").read())
        self.path_output = self.dir+"/filename.txt"
    #to save the code
    def savecode(self,string):
        v = open(self.dir+"/code.txt","w",encoding="utf8",errors="ignore")
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

class MainScreen(Screen,back):
    def compile(self):
        print(" run button pressed")
        #initilize the object that contain the all functions
        runner = back()
        #retrive the code from the input widget
        string = self.ids.input.text
        #compile the code and send output as string , ths string is assigned to the output widget
        self.ids.output.text = runner.compile(self.path_output,string)
#opening the terminal to show output
        self.ids.backdrop.open()
        #save the present code for next time
        runner.savecode(string)









class saithon(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        Builder.load_string(helper.helper)
        return MainScreen()
if __name__  == '__main__':
    saithon().run()