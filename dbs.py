#dbs.py 
#will be used as a module 

#import required modules
from pathlib import Path 
import csv

#can use these to check what is cwd or home
print(Path.cwd())

#setup filepath using variable fp using version(1) or (2):
  #use version(1): for current working directionary:

fp_read=Path.cwd()/"csv.reports\dbs_data_1.csv"
fp_write=Path.cwd()/"dbs_avg_cp.txt"
fp_write.touch()

print(fp_read.exists())
print(fp_write.exists())
