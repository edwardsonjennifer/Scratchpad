import pathlib

# def stuff_that_errors(fh):
#     print(fh)
#     raise NotImplementedError()
    
# path = pathlib.Path('resources/darth_plagueis_tragedy.txt')
# fh = open(path)
# try:
# 	stuff_that_errors(fh)
# #No matter what happens even if an exception occurs, this will be ran
# finally:
#     print("this still happens")
#     fh.close()

# print('the end')

path = pathlib.Path("01resources/test01.txt")


numbers = []
for num in range(10):
    numbers.append(str(num) + '\n')

print(numbers)

with open(path, 'w') as writer:
    writer.writelines(numbers)

print(writer.closed)