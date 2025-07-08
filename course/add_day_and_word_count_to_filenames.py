import os 
from datetime import datetime 

directory = 'files'

filenames = os.listdir(directory)
#file names are inside this-we are simply naming them
#when doing refractor it will change all with that same name

for filename in filenames:
    filepath = os.path.join(directory, filename)

    with open(filepath, 'r') as file:
        content = file.read()
        words = content.split()
        word_count =len(words)

    # day = datetime.now().strftime("%A")
    # when looking at datetime and using only %A that is the spelled out version while on the other hand using %d is basically number version
    day = datetime.now().strftime("%d")
    month = datetime.now().strftime("%m")
    year = datetime.now().strftime("%Y")



    new_filename = f'{filename[:-13]}-{year}-{month}-{day}.txt'

    # we are looking for 'a-6-Thursday.txt' from 'a.txt'

    # in this later example I simply switched it from 'a-6-Thursday.txt' directly to ' a-2025-07-07.txt'

    # we are going from last index and subtracting everything so basically the .txt is deleted to account for last 4 and second example last 13

    new_filepath = os.path.join(directory,new_filename)
    os.rename(filepath, new_filepath)

    # print statement to check

    print(f"Renamed {filename} to {new_filename}")

print("File renaming completed")