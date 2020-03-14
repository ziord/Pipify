from pyps import PyFileItr
import importlib
import os
import re
from dep_ind_mod import DEP_IND_BAD_CACHE

class ImportScanner:
    def __init__(self, pyfileitr):
        self._pyfileitr = pyfileitr
        self._modules = []
        self._ext_modules = {}
        self._module_lines = []

    def proc_norm_imp(self, line):
        has_cm = False
        has_cl = False
        nline = ''
        if ',' in line:
            has_cm = True
            nline = line.split(',')
        else:
            nline = line.split()
        if has_cm:
            nline[0] = nline[0].split('import')[1].strip()
            for pt in nline:
                pt = pt.strip()
                if '.' in pt:
                    self._modules.append(pt.split('.')[0])
                else:
                    self._modules.append(pt)
        else:
            for pt in nline[1:]: #s.o. import
                pt = pt.strip()
                if '.' in pt:
                    self._modules.append(pt.split('.')[0])
                else:
                    self._modules.append(pt)

    def proc_from_imp(self, line):
        nline = line.split()[1:]
        for pt in nline:
            pt = pt.strip()
            if pt == 'import': break
            if '.' in pt:
                self._modules.append(pt.split('.')[0])
            else:
                self._modules.append(pt)

    def proc_imp(self):
        tmp = self._module_lines[:]
        for line in tmp:
            if ';' in line:
                lst = line.split(';')
                self._module_lines.extend(lst)
        for line in self._module_lines:
            if line.startswith('from'):
                self.proc_from_imp(line)
            elif line.startswith('import'):
                self.proc_norm_imp(line)

    def scan(self, fn):
        try:
            f = open(fn)
            lines = f.readlines()
        except:
            f.close()
            return
        f.close()
        #ptn = ["\nimport .+", "from .+"]
        kw = ['from', 'import']
        for line in lines:
            line = line.strip()
            if line.startswith(kw[0]) or line.startswith(kw[1]):
                self._module_lines.append(line.strip())
        self.proc_imp()
        for mod in self._modules:
            try:
                m = importlib.import_module(mod)
                if 'built-in' in str(m): continue
                if 'site-packages' in str(m):
                    if m.__package__ in DEP_IND_BAD_CACHE:
                        self._ext_modules[m.__package__] = ''
                    else:
                        self._ext_modules[m.__package__] = m.__version__
            except:
                continue

    
    def scan_all(self):
        for fn in self._pyfileitr:
            print('scanning--', fn)
            self.scan(fn)

    def write(self):
        if self._ext_modules:
            fp = os.path.join(self._pyfileitr._path, 'requirements.txt')
            with open(fp, 'w') as file:
                for k, v in self._ext_modules.items():
                    if len(v):
                        file.write("%s==%s\n"%(k, v))
                    else:
                        file.write("%s\n"%(k))
            return True
        return False

