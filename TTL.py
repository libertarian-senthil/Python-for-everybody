fname = input('Enter the file name: ')
txt = open(f'{fname}'+'.txt').read().rstrip().upper()
print(txt)