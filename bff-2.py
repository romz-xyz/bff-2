import sys, os

M = ('\x1b[1;91m')
O = ('\x1b[1;96m')

if sys.version_info.major != 3:
  exit("\n%s!%s gunakan versi python3 "%(M,O))

if __name__=='__main__':
    try:
        os.system('git pull')
        __import__("cracks").Masuk()
    except Exception as e:
        exit(str(e))
