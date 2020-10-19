import os
import PyPDF2

from pathlib import PurePath, Path

class PdfMerge:
    """This class allows the user to merge multiple pdf files into a single file.

    :param str source_dir: the directory containing the pdf files.

    :param str target_dir: the directory where the merged output should be saved.

    :param str target_filename: the unique name of the new, merged pdf file.

    """
    def __init__(self, source_dir: str, target_dir: str, target_filename: os.PathLike):
        self._source_dir = source_dir
        self._target_dir = target_dir
        self._target_filename = target_filename
        self._obj = PyPDF2.PdfFileMerger()

    def get_filename(self):
    """Filename handling based on the class inputs. Joins the target directory with
    the filename and coerces to a PurePath object and attached pdf file extension.
    """
        filename = self._target_filename + '.pdf'
        target_dir = PurePath(self._target_dir)
        filepath = PurePath(target_dir).joinpath(filename)
        return filepath

    def merge_pdf_files_from_dir(self):
        """get pdf files from the source directory, merge and save as new pdf.
        """
        outfile = str(self.get_filename())
        for fil in Path(self._source_dir).glob('*.pdf'):
            fil = str(fil)
            self._obj.append(PyPDF2.PdfFileReader(fil, 'rb'))
        self._obj.write(outfile)
        self._obj.close()

if __name__=='__main__':
    test_dir = '/Users/FBIMAC/projectrepos/pdftools/files'
    PM = PdfMerge(source_dir=test_dir, target_dir=test_dir, target_filename='merged')
    #PM.get_pdf_files_from_dir()