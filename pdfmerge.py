import PyPDF2 
print('\nLet\'s merge pdfs\n')
no_of_pdfs=int(input("Enter number of pdfs you wanna merge = "))
pdfs = [''for _ in range(no_of_pdfs)]
merger = PyPDF2.PdfMerger()
for i in range(no_of_pdfs):
        name=input(f'Enter the name of {i+1} pdf = ')
        pdfs[i]=f'/Users/vedantkaushik/Downloads/{name}'
        # print(pdfs)

for pdf in pdfs:
    pdffile=open(pdf,'rb')
    pdfread=PyPDF2.PdfReader(pdffile)
    merger.append(pdfread)

merger.write("/Users/vedantkaushik/Downloads/resultant_combined.pdf")
merger.close()

