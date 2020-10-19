import os
import PyPDF2

from pathlib import PurePath, Path

class PdfMerge:
    def __init__(self, source_dir: str, target_dir: str, target_filename: os.PathLike):
        self._source_dir = source_dir
        self._target_dir = target_dir
        self._target_filename = target_filename
        self._obj = PyPDF2.PdfFileMerger()

    def get_filename(self):
        filename = self._target_filename + '.pdf'
        target_dir = PurePath(self._target_dir)
        filepath = PurePath(target_dir).joinpath(filename)
        return filepath

    def get_pdf_files_from_dir(self):
        #pull pdf files from the target directory
        outfile = str(self.get_filename())
        for fil in Path(self._source_dir).glob('*.pdf'):
            fil = str(fil)
            self._obj.append(PyPDF2.PdfFileReader(fil, 'rb'))
        self._obj.write(outfile)

    #read in pdf files
    #pdf_obj = PyPDF2.PdfFileReader(stream='files/iris8.pdf')
    #pdf_obj2 = PyPDF2.PdfFileReader(stream='files/iris4.pdf')

    #use object to append
    #pm = PyPDF2.PdfFileMerger()
    #pm.append(pdf_obj)
    #pm.append(pdf_obj2)

    #write merged pdf
    #pm.write(target directory)
    #pm.close()

if __name__=='__main__':
    test_dir = '/Users/FBIMAC/projectrepos/pdftools/files'
    PM = PdfMerge(source_dir=test_dir, target_dir=test_dir, target_filename='merged')