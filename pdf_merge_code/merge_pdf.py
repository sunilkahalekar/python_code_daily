# This will use to merge pdf file locally

from PyPDF2 import PdfMerger

def merge_pdf(file1, file2, output_file):
    merger = PdfMerger()
    
    # Open the first PDF file
    with open(file1, 'rb') as f1:
        merger.append(f1)
    
    # Open the second PDF file
    with open(file2, 'rb') as f2:
        merger.append(f2)
    
    # Write the merged PDF to the output file
    with open(output_file, 'wb') as output:
        merger.write(output)

# Example usage
file1 = 'one.pdf'
file2 = 'two.pdf'
output_file = 'merged_file.pdf'

merge_pdf(file1, file2, output_file)
