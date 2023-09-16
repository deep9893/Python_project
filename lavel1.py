from docx2pdf import convert
import os,sys


def convert_word_to_pdf(input_path, output_path):
    try:
        convert(input_path, output_path)
        
        print(f"conversion completed . pdf saved as {output_path}")
    
    except Exception as e:
        print(f"an error occurred while converting: {str(e)}")


if __name__ == "__main__":
    input_path ='Interview.docx'
    
    output_path =r"d:\Study\ml_pipeline\Python_project\output.pdf"
    
    
    if os.path.exists(input_path):
        convert_word_to_pdf(input_path, output_path)
        
    else:
        print(f"input word document file'{input_path}' does not exist")