from posixpath import split


def get_default_file ():
    return open('data/competencia.txt').readlines()

def open_another_file (dir: str):
    try: 
        if (not '.txt' in dir):
            print('You passed a not .txt file, please check it')

        file = open(dir)
        for f in file:
            if len(split(f.readline(), ',')) != 10:
                print('Some data in your file is incomplete, please try again')
                break
        file.close()
        
        return open(dir, 'r').readlines()
    except:
        print('something went wrong')