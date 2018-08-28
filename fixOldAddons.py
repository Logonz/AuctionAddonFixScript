#!/usr/bin/python
import os
import sys
mypath = sys.argv[0]
def listdir(d):
    if not os.path.isdir(d):
    	if(d.endswith(".lua")):
    		file = open(d, 'r', encoding="utf-8")
    		if "StartAuction" in file.read():
    			print("Found in " + d)
    			var = input("Would you like to change StartAuction to PostAuction? Y/N  ")
    			if(var.lower() == "y"):
    				file.close();
    				inplace_change(d, "StartAuction", "PostAuction")
    				print("Change done!\n")
    			else:
    				print("Ignoring!\n")

    else:
        for item in os.listdir(d):
            listdir((d + '/' + item) if d != '/' else '/' + item)

def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: listall DIR')
    else:
        listdir(sys.argv[1])
        print("All changes done!")

