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

from util import PyiUiLoader


class WidgetWrapper:
    def __init__(self, file_path, parent=None):
        self._widget = self._load(file_path, parent)

    @property
    def widget(self):
        return self._widget

    def _load(self, file_path, parent):
        loader = PyiUiLoader()
        _widget = loader.load(file_path, parent)
        self.after_load()
        return _widget

    def after_load(self):
        """ Add UI setup logic here """
        pass

    def show(self):
        """ Calls show() on the wrapped widget """
        self.before_show()
        self.widget.show()
        self.after_show()

    def before_show(self):
        """ Add pre-show logic here """
        pass

    def after_show(self):
        """ Add post-show logic here """
        pass
