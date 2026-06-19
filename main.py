from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
Builder.load_file("calc.kv")
Window.clearcolor=(0,0,0,1)
class Calculator(FloatLayout):
    def clear(self):
        content=self.ids.expression.text
        if content=="0":
            pass
        else:
            self.ids.expression.text="0"
    def button(self,btn_content):
        content=self.ids.expression.text
        if content=="0" and btn_content==".":
            self.ids.expression.text+=btn_content
        elif content=="0" or content=="Nabeel" or content=="Error":
            self.ids.expression.text=""
            self.ids.expression.text=btn_content
        else:
            self.ids.expression.text+=btn_content
    def remove_last(self):
        content=self.ids.expression.text
        if content=="Nabeel" or content=="Error":
            self.ids.expression.text="0"
        elif content=="0":
            pass
        else:
            content=content[:-1]
            self.ids.expression.text=content
            if content=="":
                self.ids.expression.text="0"
    def developer(self):
        content=self.ids.expression.text
        if content=="0":
            self.ids.expression.text="Nabeel"
        else:
            pass
    def equal(self):
        content=self.ids.expression.text
        answer=0.0
        try:
            answer=eval(content)
            self.ids.expression.text=f"{answer:.4f}".rstrip("0").rstrip(".")
        except:
            self.ids.expression.text="Error"
class Main(App):
    def build(self):
        return Calculator()
if __name__=="__main__":
    app=Main()
    app.run()
