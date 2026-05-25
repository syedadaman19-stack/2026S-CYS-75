
def check_type(a):
    if a.isalpha():
        print("String")
    elif "." in a:
        print("Float")
    elif  a.isdigit():
        print("Integer")
    return a
a=(input("Enter Something : "))
b=(check_type(a))
