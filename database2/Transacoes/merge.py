import os

fout=open("out.csv","a")
for num in range(0,99):
    if(os.path.isfile("raw_part-"+str(num).zfill(5)+".csv")):
      for line in open("raw_part-"+str(num).zfill(5)+".csv", errors='ignore'):
           if not(line.startswith("encrypted_domain") or line.strip()==""):
              fout.write(line)    
fout.close()
