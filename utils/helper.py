from docx2pdf import convert

class WordToPDFConverter:
    
    def convert_word_to_pdf(input_path, output_path):
        try:
            convert(input_path, output_path)
            
            print(f"conversion completed . pdf saved as {output_path}")
        
        except Exception as e:
            print(f"an error occurred while converting: {str(e)}")
