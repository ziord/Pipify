"""
Simple requirements.txt file generator for Python projects
"""
import os

class PyFileItr:
    def __init__(self, path):
        self._path = path
    
    def __iter__(self):
        return PyFileIterator(self._path)

class ProjectPathError(Exception): pass

class PyFileIterator:
    def __init__(self, path):
        self._path = path
        self._pyfiles = []
        self._cur_file_seq = None
        self._cnt = 0
        self._is_cat = False
    
    def __iter__(self):
        yield self
    
    def __next__(self):
        if not self._is_cat:
            self._is_cat = True
            self._build_itr()
        try:
            self._cur_file_seq = self._pyfiles[self._cnt]
            self._cnt += 1
            return self._cur_file_seq
        except:
            raise StopIteration()

    def _build_itr(self):
        if os.path.exists(self._path):
            self._categorize(self._path)
        else:
            raise ProjectPathError("Invalid Project Path%s"%self._path)
    
    def _proc_abs_fp(self, root, fl):
        for file in fl:
            self._pyfiles.append(os.path.join(root, file)) if file.endswith('.py') else ...

    def _categorize(self, cdir):
        r_ = sds_ = fls = None
        for root, subdir, files in os.walk(cdir):
            r_, sds_, fls = root, subdir, files
            break
        if fls:
            self._proc_abs_fp(r_, fls)
        if sds_:
            for sd_ in sds_:
                sd__ = os.path.join(r_, sd_)
                self._categorize(sd__)






    