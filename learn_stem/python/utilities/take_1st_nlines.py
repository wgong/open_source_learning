num_lines=10000
import sys
import os.path
if len(sys.argv) <= 1:
    print("Usage: python ", sys.argv[0], " <file_in.csv> [<num_lines (def=", num_lines, ")>]")
    exit(-1)
if len(sys.argv) > 1:
    file_in = sys.argv[1]
if len(sys.argv) > 2:
    num_lines = int(sys.argv[2])

if not os.path.exists(file_in):
    print('File ', file_in, ' not found' )
    exit(-2)

file_name, file_ext = os.path.splitext(file_in)
file_out = "%s_%dk%s" % (file_name,int(num_lines/1000),file_ext)
 
    
fo=open(file_out, "w")
n = 0
with open(file_in, "r") as fi:
    while n < num_lines:
        try:
            try:
                line=fi.readline()
                fo.write(line)
                n += 1
            except UnicodeDecodeError as e1:
                print("[UnicodeDecodeError] ", e1)
        except UnicodeDecodeError as e2:
            print("[UnicodeDecodeError] ", e2)
                
fo.close()
