import os
import glob
import fitz
import xml.etree.ElementTree as ET

def count_pages(file_path):
    doc = fitz.open(file_path)
    return len(doc)

def search_pdf_files(path):
    return glob.glob(path + '/**/*.pdf', recursive=True)

def create_xml(pdf_files):
    root = ET.Element('pdfs')

    for file_path in pdf_files:
        file_name = os.path.basename(file_path)
        num_pages = count_pages(file_path)

        pdf = ET.SubElement(root, 'pdf')
        ET.SubElement(pdf, 'filename').text = file_name
        ET.SubElement(pdf, 'pages').text = str(num_pages)

    tree = ET.ElementTree(root)
    tree.write('pdf_pages.xml')
    
def main(path):
    pdf_files = search_pdf_files(path)
    create_xml(pdf_files)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
