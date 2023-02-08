# make sure you have the ingredients to bake the cake. Use pip or !pip (for cloud environments) to download the modules. 

import os
from textblob import TextBlob
from PyPDF2 import PdfReader

# get that file
file_path = 'path/to/file.pdf'

# now you can define... 'stuff' ()

def correct_spelling(file_path):
    try:
        filename, file_extension = os.path.splitext(file_path)
        corrected_file = filename + '_copy' + file_extension
        
        # remember it can read just text or pdf files. The 'if-else' condition allows you to do so. Elif is just 'else if'. So basically two 'if's, or as many as you like. Reminds me of someone I knew.  
        if file_extension == '.txt':
            with open(file_path, 'r') as file:
                text = file.read()
                corrected_text = str(TextBlob(text).correct())
                
            with open(corrected_file, 'w') as file:
                file.write(corrected_text)
        # I am commenting the following block as the output pdf doesn't open for some reason
        # Feel free to uncomment and edit

#         elif file_extension == '.pdf':
#             reader = PdfReader(file_path)
#             text = ''
#             for page_number in range(len(reader.pages)):
#                 text += reader.pages[page_number].extract_text()
            
#             corrected_text = str(TextBlob(text).correct())
            
#             with open(corrected_file, 'w') as file:
#                 file.write(corrected_text)
        
  # this is just a reminder that the file is horses**t
        else:
            print(f'Error: Unsupported file format: {file_extension}')
    except Exception as e:
        print(f'Error: {e}')

correct_spelling(file_path)
