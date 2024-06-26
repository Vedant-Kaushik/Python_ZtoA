from PyPDF2 import PdfReader,PdfWriter
import os
files = [ file for file in os.listdir() if file.endswith('.pdf')]
class readwritepdf:
    def __init__(self,pdfname):
        self.reader = PdfReader(f"{pdfname}.pdf")
        print(len(self.reader.pages))

from PyPDF2 import PdfReader, PdfWriter

class ExtractPages:
    def __init__(self, pdfname):
        self.pdfname = pdfname

    def extract_images(self):
        reader = PdfReader(self.pdfname)
        writer = PdfWriter()

        count = 0
        for page_number, page in enumerate(reader.pages, start=1):
            for image_index, image in enumerate(page.images, start=1):
                with open(f"image_{count}.png", "wb") as fp:
                    fp.write(image.stream.get_data())
                    count += 1

            # Add the original page to the new PDF
            writer.add_page(page)

        with open(f"imagetaken_{self.pdfname}", "wb") as f:
            writer.write(f)



class mergepdf:
        merger = PdfWriter()
        
        for pdf in files:
         merger.append(pdf)

        merger.write("merged file.pdf")
        merger.close()
        from PyPDF2 import PdfReader, PdfWriter

        reader = PdfReader("merged file.pdf")
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.add_metadata(reader.metadata)

        with open("compressed merged file.pdf", "wb") as fp:
            writer.write(fp)


a = ExtractPages('C_Experiment_8.pdf')
a.extract_images()