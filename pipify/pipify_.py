from pipify import imp_scn
import time
import argparse
from pipify import pkg

__version__ = pkg.get_info()["version"]

def main(fp):
    st = time.time()
    fi = imp_scn.PyFileItr(fp)
    i_s = imp_scn.ImportScanner(fi)
    i_s.scan_all()
    v = i_s.write()
    et = time.time()
    print('requirements.txt file generated successfully in %ss'%(et-st)) if v else print('No dependencies found.')
    

def run_main():
    argp = argparse.ArgumentParser(
        description="Utility tool to generate requirements.txt file for Python projects",
        usage="usage: python pipify -P Project_Path"
        )
    argp.add_argument("-P", "--path",action="store", type=str, help="Path to Python project")
    argp.add_argument("-V", "--version", action='version', version='%(prog)s ' + __version__)
    args = argp.parse_args()
    if not args.path:
        print(argp.usage)
    else:
        main(args.path)