#  MIT License
#
#  Copyright (c) 2020 Doug Saylor
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

from PySide2.QtUiTools import QUiLoader
import sys
from os import path


"""
Runtime utility package to help in resolving paths in development in the same way when files are added as data objects
in frozen packages (single-file or single-folder).
Currently works with PyInstaller v3.6.
"""


def frozen_path(file_path: str) -> str:
    """
    The docs recommend using `path.dirname(getattr(sys, '_MEIPASS'))`, but it doesn't seem to work correctly because
    it backs up the path too far.
    :param file_path: Path string that should be translated to be relative to the bundle location in the case of
    operating in a frozen environment.
    :return: The translated string.
    """
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        bundle_dir = getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
        return path.join(bundle_dir, file_path)
    else:
        return file_path


class PyiUiLoader:
    """
    A wrapper around PySide2.QtUiTools.QUiLoader that handles loading from a PyInstaller archive.
    There are a few things to ensure success of the PyInstaller build and runtime behavior
    * Ensure that *.ui files are added to your pyinstaller spec in the `datas` section
    * Ensure that 'PySide2.QtXml' is added as a hidden import
    * The `--debug all` command line switch is incompatible with `-w`
      * Ensure that `('v', None, 'OPTION')` is not present in your spec file, or you will get a failure on startup
      * https://github.com/pyinstaller/pyinstaller/issues/4213#issuecomment-569381968
    """
    def __init__(self):
        self._loader = QUiLoader()

    def load(self, file_path, parent):
        actual_path = frozen_path(file_path)
        return self._loader.load(actual_path, parent)