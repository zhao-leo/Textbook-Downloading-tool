import bnu
import pep

print("Welcome to the textbook downloader!")
print("Now support the following sources:")
print("1. PEP (https://jc.pep.com.cn)")
print("2. BNU (http://www.100875.com.cn/show/resource.html)")
print("3. Exit (Exit the program.)")
source = input("Please input the source of the book (1/2/3):")
while True:
    if source == "3":
        print("Goodbye!")
        break
    elif source == "1":
        pep.pep_main()
    elif source == "2":
        bnu.bnu_main()
    else:
        print("Invalid source!")
    if source == "1":
        pressname = "PEP"
        another = "BNU"
    elif source == "2":
        pressname = "BNU"
        another = "PEP"
    print("Do you want to download another book?")
    print(f"If you still want to download {pressname} book,please input Enter,")
    print(f"if you want to download {another} book,please input 1,")
    print("if you want to exit,please input 3.")
    sourcex = input("Please input your choice:")
    if sourcex == "3":
        source = "3"
    elif sourcex == "1":
        if source == "1":
            source = "2"
        elif source == "2":
            source = "1"