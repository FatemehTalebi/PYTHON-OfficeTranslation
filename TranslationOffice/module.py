import enum
import datetime
from abc import ABC, abstractmethod

class BookStatus(enum.Enum):
    UNSELECTED=1
    SELECTED=2
    TRANSLATED=3
    # -------------------------------------
class Text(ABC):
    unselected=[]
    selected=[]
    finished=[]
    def __init__(self,code,lang, translationDays):
        self.code=code
        self.lang=lang
        self.translationDays=translationDays
        self.dateTime=datetime.datetime.now()
        self.textStatus=BookStatus.UNSELECTED
    
    def __str__(self) :
        return f"{self.lang}\t{self.translationDays}\t{self.dateTime}\t{self.textStatus}"
    
    @abstractmethod   
    def calculate_fee(self):
        pass
    
    def get_lang(self):
        return self.lang
    
    def changeStatus(self,newStatus):
        self.textStatus=newStatus
        
    
# -------------------------------------------
class PlainText(Text):
    def __init__(self,code, lang, translationDays,shortWords, longWords):
        super().__init__(code, lang, translationDays)
        self.shortWords=shortWords
        self.longWords=longWords
        Text.unselected.append(self.code)
    def calculate_fee(self):
        fee=(self.shortWords*0.2)+(self.longWords*0.5)
        return fee
    # -----------------------------------
class ScienceText(Text):
    def __init__(self,code, lang, translationDays,generalWords, technicalWords):
        super().__init__(code,lang, translationDays)
        self.generalWords=generalWords
        self.technicalWords=technicalWords
        Text.unselected.append(self.code)
    def calculate_fee(self):
        fee=(self.generalWords*0.3)+(self.technicalWords*0.6)
        return fee
    # ----------------------------------
class PictureText(Text):
    def __init__(self,code, lang, translationDays,imageNumbers):
        super().__init__(lang, translationDays)
        self.imageNumberss=imageNumbers
    def calculate_fee(self):
        fee=self.imageNumberss*10
        return fee
    # -------------------------------------
class MultiText(Text):
    def __init__(self,code, lang, translationDays):
        super().__init__(lang, translationDays)
        self.textList=[]
        
    def add_text(self,text):
        self.textList.append(text)
    
    def calculate_fee(self):
        fee=0
        for text in self.textList:
            fee+= text.calculate_fee()
        return fee
        # -----------------------------------
  
class Translator():
    def __init__(self, name, mobile):
        self.name=name
        self.mobile=mobile
        self.status=False
        self.langList=[]
            
    def add_lang(self,lang):
        self.langList.append(lang)
            
    def __str__(self):
        temp=self.name +"\t"+str(self.mobile)+"\t"+str(self.status)+"\n"
        for lang in self.langList:
            temp+=lang+"\n"
            return temp
    def select_text(self,text):
        if self.status==False:
            if text.textStatus==BookStatus.UNSELECTED:
                self.status=True
                text.changeStatus(BookStatus.SELECTED)
                Text.unselected.remove(text.code)
                Text.selected.append(text.code)
            else:
                print("the text has been taken")
        else:
            print("you already have takes a text")
                
    def finish_translation(self,text):
        self.status=False
        text.changeStatus(BookStatus.TRANSLATED)
        Text.selected.remove(text.code)
        Text.finished.append(text.code)
            
                
                
    #  ------------------
      # main App
text1=ScienceText("3","EN",25,300,150)

print(text1.calculate_fee())
print(text1)

print(text1.textStatus)
translator1=Translator("Fatemeh","123456789")
translator1.add_lang("EN")
print(translator1)
print(Text.selected)

translator1.select_text(text1)
print(text1)
print(translator1)
translator1.finish_translation(text1)
print(translator1)
print(text1)
print(Text.finished)
print(Text.unselected)






