from utils.helper import WordToPDFConverter
import os


def convert_word_to_pdf(input_path, output_path):
    try:
        WordToPDFConverter.convert_word_to_pdf(input_path, output_path)

        return f"conversion completed . pdf saved as {output_path}"

    
    except Exception as e:
        return f" an error occurred: {str(e)}"