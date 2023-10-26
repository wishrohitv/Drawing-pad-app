# Import required library.
import pdfplumber

# Open the file and create a pdf object.
pdf = pdfplumber.open("pd.pdf")

# Get the number of pages.
numPages = len(pdf.pages)

print("Number of Pages:", numPages)

# Iterate over each page and extract the text of each page.
for number, pageText in enumerate(pdf.pages):
    print("Page Number:", number)
    print(pageText.extract_text())

