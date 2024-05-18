import PyPDF2

def main():
    path = "D:\\Roba da autodidatta\\Videogames\\Game Audio Programming\\thinkdsp.pdf"
    # Open the PDF file
    pdf_file_obj = open(path, 'rb')
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    # Initialize an empty string to hold the extracted text
    text = ''
    # Loop through each page in the PDF and extract the text
    for page in pdf_reader.pages:
        text += page.extract_text()
    # Close the PDF file object
    pdf_file_obj.close()
    # Write the text to a text file
    with open("D:\\Roba da autodidatta\\Videogames\\Game Audio Programming\\thinkdsp.txt", 'w', encoding='utf-8') as f:
        f.write(text)
    print("Conversion completed!")

main()















