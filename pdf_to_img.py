import os
from pdf2image import convert_from_path
file_list = os.listdir("./")
print(file_list)
#pages = convert_from_path('pdf_file', 500)
#for page in pages:
#    page.save('out.png', 'PNG')