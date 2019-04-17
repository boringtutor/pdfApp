import PyPDF2
import glob

def merger (outputpath):
    print('starting the file merging')
    print('make sure none of the input or output file is open')
    try:
        filepaths = (glob.glob("./test1/*.pdf"))
        pdfmerger(filepaths,outputpath)
    except:
        print('the exception occured...')


def pdfmerger(files,output):
    '''
    You can use PyPDF2 to copy pages from one PDF document to another.
    This allows you to combine multiple PDF files, cut unwanted pages,
    or reorder pages.
    '''
    filereaders=[]
    print('file reader......')
    for i in range(len(files)):
        file = 'pdffile'+'i'
        file = open(files[i], 'rb')
        filereaders.append(file)
    
    pdffilereaders = []
    for i in range (len(files)):
        file = 'pdfReader'+'i'
        file = PyPDF2.PdfFileReader(filereaders[i])
        pdffilereaders.append(file)
    
    pdfWriter = PyPDF2.PdfFileWriter()
    for reader in pdffilereaders:
        for pageNum in range(reader.numPages):
            pageObj = reader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
    
    pdfOutputFile = open(output, 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    for reader in filereaders:
        reader.close()
    print('finished merging the pdfs and writen in the output file '+output)

def rotate_file(filepath):
    '''
    The pages of a PDF can also be rotated in 90-degree increments with the rotateClockwise()
    and rotateCounterClockwise() methods. Pass one of the integers 90, 180, or 270 to these 
    methods. Enter the following into the interactive shell, with the meetingminutes.pdf file
    in the current working directory.
    '''
    minutesFile = open(filepath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(minutesFile)
    page = pdfReader.getPage(0)
    page.rotateClockwise(90)
    
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.addPage(page)
    resultPdfFile = open('rotatedPage.pdf', 'wb')
    pdfWriter.write(resultPdfFile)
    resultPdfFile.close()
    minutesFile.close()

def overlaypages(filepath,overlayfilepath,outputfilepath='watermarkedCover.pdf'):
    '''
    PyPDF2 can also overlay the contents of one page over another, which is useful for adding a logo, 
    timestamp, or watermark to a page. With Python, it’s easy to add watermarks to multiple files and
    only to pages your program specifies.
    '''
    minutesFile = open(filepath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(minutesFile)
    minutesFirstPage = pdfReader.getPage(0)
    pdfWatermarkReader = PyPDF2.PdfFileReader(open(overlayfilepath, 'rb'))
    minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.addPage(minutesFirstPage)

    for pageNum in range(1, pdfReader.numPages):
           pageObj = pdfReader.getPage(pageNum)
           pdfWriter.addPage(pageObj)
    resultPdfFile = open(outputfilepath, 'wb')
    pdfWriter.write(resultPdfFile)
    minutesFile.close()
    resultPdfFile.close()

def encryptingPdf(filepath,outputencryptionfile='encryptedminutes.pdf'):
    '''
    A PdfFileWriter object can also add encryption to a PDF document.
    '''
    pdfFile = open(filepath, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader.numPages):
           pdfWriter.addPage(pdfReader.getPage(pageNum))

    pdfWriter.encrypt('swordfish')
    resultPdf = open(outputencryptionfile, 'wb')
    pdfWriter.write(resultPdf)
    resultPdf.close()

def test(dirs):
    output = "combs.pdf"
    print(dirs)
    ##pdfmerger(dirs,output);

if __name__ == "__main__":
    ##merger('combinedminutes.pdf')
    rotate_file('Page1.pdf')
