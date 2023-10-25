# .csv comma seperated file ==for data stored
# .txt text file

# take input in a file, jeta ekhane nai
# with open('message.txt','w') as file:
#     file.write('i love you,python')
# w==write kora
# a==append kora , lekhagulo jog kora. bar bar write kora 
# with open('message.txt','a') as file:
#     file.write('i love you,python\n')

with open('message.txt','r')as file:
    text=file.read()
    print(text)