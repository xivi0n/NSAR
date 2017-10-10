#SimpleAssemblyRunner
import zipfile
import os
import subprocess


gccPath = ""
nasmPath = ""

def checkNasm():
    global nasmPath
    print "*Checking NASM..."
    try:
        with open('nasm.txt','r') as f: nasmPath=f.read()
    except IOError:
        print "*Configuring NASM..."
        zip_ref = zipfile.ZipFile(os.path.dirname(os.path.abspath(__file__))+"\\NASM.zip", 'r')
        zip_ref.extractall(os.path.dirname(os.path.abspath(__file__)))
        zip_ref.close()
        os.system("del NASM.zip")
        nasmPath='"'+os.path.dirname(os.path.abspath(__file__))+"\\NASM\\nasm.exe"+'"'
        with open('nasm.txt','w') as f: f.write(nasmPath)
    print "NASM Configured!"

def checkGCC():
    global gccPath
    print "*Checking GCC..."
    try:
        with open('gcc.txt','r') as f: gccPath=f.read()
    except IOError:
        print "*Configuring GCC..."
        zip_ref = zipfile.ZipFile(os.path.dirname(os.path.abspath(__file__))+"\\GCC.zip", 'r')
        zip_ref.extractall(os.path.dirname(os.path.abspath(__file__)))
        zip_ref.close()
        os.system("del GCC.zip")
        gccPath='"'+os.path.dirname(os.path.abspath(__file__))+"\\GCC\\bin\\gcc.exe"+'"'
        with open('gcc.txt','w') as f: f.write(gccPath)
    print "GCC Configured!"

checkNasm()
checkGCC()

name = raw_input("Enter source code file name (including .asm): ")

print "Running NASM..."
nasmCommand = nasmPath+' -f win32 '+name
subprocess.check_call(nasmCommand, shell=True)

name = name.replace('.asm','.obj')

print "Running GCC..."
gccCommand = gccPath+' '+name+' driver.c '+'asm_io.obj'
subprocess.check_call(gccCommand, shell=True)

print "Running your program...\n"
os.system("a")
print "\n"

os.system("del a.exe")
raw_input("Press any key to continue...")
