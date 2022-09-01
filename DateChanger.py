## To showcase one of the utilities I have, I created a set of files that ranged from 0 to a given value, and then randomly changed 
## The creation date of such files

from random import randint
import filedate

## This will take care of the task of creating given files.

for i in range(10000):
    fp = open('Path to destination' + str(i) + "File Extension", 'w')
    fp.close()


## Another for loop in this case to change the date of the files. Everything is pseudo-random but it works for the given task
## You could change the first seeding of randint to the desired range. It will also only go up to 28 days in case February is parsed.


for i in range(10000):
    a = 'Enter path the folder' + str(i) + 'File Extension'
    a_file = filedate.File(a)

    a_file.set(
        created = str(randint(2000, 2022)) + "." + str(randint(1, 12)) + "." + str(randint(1, 28)) + " " + str(randint(0, 23)) + ":" + str(randint(0, 59)) + ":" + str(randint(0, 59)),
        modified = str(randint(2000, 2022)) + "." + str(randint(1, 12)) + "." + str(randint(1, 28)) + " " + str(randint(0, 23)) + ":" + str(randint(0, 59)) + ":" + str(randint(0, 59)),
        accessed = str(randint(2000, 2022)) + "." + str(randint(1, 12)) + "." + str(randint(1, 28)) + " " + str(randint(0, 23)) + ":" + str(randint(0, 59)) + ":" + str(randint(0, 59))
    )
        
    after = filedate.File(a)

