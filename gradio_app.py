import gradio as gr
from utils.convert_helper import convert_word_to_pdf
from gradio import components

def gradio_convert_word_to_pdf(input_word):
    try:
        input_word_path = input_word.name
        output_pdf_path = r"d:\Study\ml_pipeline\Python_project\output2.pdf"
        
        result_message = convert_word_to_pdf(input_word_path, output_pdf_path)
        
        return result_message
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Create Gradio-based user interface
iface = gr.Interface(
    fn=gradio_convert_word_to_pdf,
    inputs=components.File(label='Input Word document', type='file'),
    outputs=components.Textbox(label='Conversion status'),
    live=True,
    title='Word to PDF converter',
    description='Convert Word document to PDF files'
)

if __name__ == "__main__":
    iface.launch()
