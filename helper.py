helper = """
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
 
<MyBackdropBackLayer@ScrollView>
<MyBackdropFrontLayer@Screen>
<MainScreen>:
    id:main
    MDBackdrop:
        padding  : [10,10,10,10]
        id: backdrop    
        right_action_items:[['play',lambda x:root.compile(),"run "]]   
        title: "python_compiler"
        radius_left: "30dp"

        radius_right: "30dp"
        header_text: "Editor"
#this is my terminal
        MyBackdropBackLayer:
          
            MyBackdropBackLayer:
                id: backlayer
                ScrollView:
                    id:srlvb
                    TextInput:
                        id:output
                        text:">> "
                        allow_copy:False
                        multiline:True
                        readonly:True
                        height : self.minimum_height
                        size_hint_y:None

                 
#this is my  editor
        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                backdrop: backdrop
                ScrollView:
                    ScrollView:
                        id:srl
                        CodeInput:
                            id:input
                            multiline:True
                            text :root.code
                            height : root.height
                            size_hint_y:None
                           


"""
