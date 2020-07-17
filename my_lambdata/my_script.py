# my_script.py

from pandas import DataFrame
from my_mod import enlarge 
from my_files.beat import Beat
from my_files.beat import Hip_Hop

print('Hello')

df = DataFrame({'a':[1,2,3], 'b':[4,5,6]})
print(df.head)

x = 11
print(enlarge(x))

print(Hip_Hop.keys)
print(Beat.keys)



