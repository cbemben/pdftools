import PyPDF2
import Pathlib

class PdfMerge:
    def _init_(self, source_dir: str, target_dir: os.PathLike, target_filename: os.PathLike):
        self._source_dir = source_dir
        self._target_dir = target_dir

    def get_pdf_files_from_dir(self):
    #pull pdf files from the target directory
    pdfList=[pdf for pdf in os.listdir() if pdf.endswith(".pdf")]
    for fil in pdfList:
        obj.append(PdfFileReader(fil, 'rb')) 
        obj.write("Merged.pdf") 

    #read in pdf files
    pdf_obj = PyPDF2.PdfFileReader(stream='files/iris8.pdf')
    pdf_obj2 = PyPDF2.PdfFileReader(stream='files/iris4.pdf')

    #use object to append
    pm = PyPDF2.PdfFileMerger()
    pm.append(pdf_obj)
    pm.append(pdf_obj2)

    #write merged pdf
    pm.write(target directory)
    pm.close()

if __name__=='__main__':
    test_dir = '/Users/FBIMAC/projectrepos/pdftools/files'
    PM = PdfMerge()