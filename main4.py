# square = 0
# num = int(input("Enter your num --> "))
# try:
#     if num < 0:
#         raise ValueError("Number must be higher than zero")
#     square = num ** 0.5
# except:
#     print("Invalid input")
# print(square)

# def sqaureNum(num):
#     return num ** 0.5
# try:
#     if num < 0:
#         raise ValueError("Number must be higher than zero")
#     sqaureNum(num)
# except:
#     print("Invalid input")

# def squareNumV2(num):
#     try:
#         if num < 0:
#             return ValueError("Number bust be higher than zero")
#         return num ** 0.5
#     except:
#         return "invalid input"

dictionary = {}
key = ""
word = ""
isFinished = False
while(isFinished == False):
    key = input("Enter key to a word in dictionary (Enter 0 to quit) --> ")
    word = input("Enter word  -->")
    if key == "0":
        isFinished = True
    else:
        dictionary[key] = word

chose = int(input("Choose what to do:\n1)Show Dictionary\n2)Find word\n3)Replace word\n4)Show word\n5)Revome word\n"))
match chose:
    case 1:
        print(dictionary)
    case 2:
        try:
            key = input("Enter key which you want to find --> ")
            print(dictionary[key])
        except:
            print("Invalid word or key")
        
    case 3:
        try:
            key = input("Enter key which will be replaced --> ")
            word = input("Enter new word --> ")
            dictionary.pop(key)
            dictionary[key] = word
        except:
            print("Invalid word or key")
        print(dictionary)
    case 4:
        try:
            key = input("Enter key what to find --> ")
            print(dictionary[key])
        except:
            print("Invalid word or key")
    case 5:
        try:
            key = input("Enter key which will be replaced --> ")
            dictionary.pop(key)
        except:
            print("Invalid word or key")
        print(dictionary)

def createDictionaryV2():
    dictionary = {}
    key = ""
    word = ""
    isFinished = False
    while(isFinished == False):
        key = input("Enter key to a word in dictionary (Enter 0 to quit) --> ")
        word = input("Enter word  -->")
        if key == "0":
            isFinished = True
        else:
            dictionary[key] = word

    chose = int(input("Choose what to do:\n1)Show Dictionary\n2)Find word\n3)Replace word\n4)Show word\n5)Revome word\n"))
    match chose:
        case 1:
            print(dictionary)
        case 2:
            try:
                key = input("Enter key which you want to find --> ")
                print(dictionary[key])
            except:
                print("Invalid word or key")
            
        case 3:
            try:
                key = input("Enter key which will be replaced --> ")
                word = input("Enter new word --> ")
                dictionary.pop(key)
                dictionary[key] = word
            except:
                print("Invalid word or key")
            print(dictionary)
        case 4:
            try:
                key = input("Enter key what to find --> ")
                print(dictionary[key])
            except:
                print("Invalid word or key")
        case 5:
            try:
                key = input("Enter key which will be replaced --> ")
                dictionary.pop(key)
            except:
                print("Invalid word or key")
            print(dictionary)

createDictionaryV2()




