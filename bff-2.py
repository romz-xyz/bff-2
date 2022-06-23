import sys, os, subprocess

bff_2 = open(os.devnull, "w")
my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
bff_2.close()
if my_music !=0:
	os.system('pkg install play-audio')

M = ('\x1b[1;91m')
O = ('\x1b[1;96m')

if sys.version_info.major != 3:
  exit("\n%s!%s gunakan versi python3 "%(M,O))

if __name__=='__main__':
    try:
        __import__("cracks").Menu()
    except Exception as e:
        exit(str(e))
