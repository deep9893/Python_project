from utils.helper import WordToPDFConverter
import os

class WordToPDFApp:
    def __init__(self,input_path,output_path):
        self.input_path = input_path
        self.output_path = output_path
        
    def convert(self):
             
        if os.path.exists(self.input_path):
            WordToPDFConverter.convert_word_to_pdf(self.input_path, self.output_path)
            
        else:
            print(f"input word document file'{self.input_path}' does not exist")
            


if __name__ == "__main__":
    input_path ='Interview.docx'
    
    output_path =r"d:\Study\ml_pipeline\Python_project\output1.pdf"
    
    app = WordToPDFApp(input_path, output_path)
    app.convert()