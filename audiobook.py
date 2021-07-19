import pyttsx3
import PyPDF2
import easygui


file= easygui.fileopenbox()
read = open(file, 'rb') #it is use to read the whole pdf or file

#count the nimber of pages
pdfReader = PyPDF2.PdfFileReader(read)
pages = pdfReader.numPages
print('Total number of pages: ',pages)


speaker = pyttsx3.init()
atpage=int(input('from where to read: '))
startpoint = pdfReader.getPage(atpage)


text = startpoint.extractText()
speaker.say(text)
speaker.runAndWait()



#C:\Users\pushp\anaconda3\bin\pyfile\MultimediaNotes.pdf,  C:\Users\pushp\anaconda3\bin\pyfile\Arihant Computer Aareness.pdf