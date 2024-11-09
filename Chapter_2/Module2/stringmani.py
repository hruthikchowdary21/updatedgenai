def string_manipulation():
    string = input("Enter the string to manipulate: ")
    
    print("\nWhat kind of manipulation do you want to do?")
    print("1. Reverse the string")
    print("2. Convert to uppercase")
    print("3. Convert to lowercase")
    print("4. Capitalize the string")
    print("5. Count occurrences of a substring")
    print("6. Replace a substring")
    print("7. Split the string")
    print("8. Join a list of strings")
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        print("Reversed string:", string[::-1])
    elif choice == '2':
        print("Uppercase string:", string.upper())
    elif choice == '3':
        print("Lowercase string:", string.lower())
    elif choice == '4':
        print("Capitalized string:", string.capitalize())
    elif choice == '5':
        substring = input("Enter the substring to count: ")
        print(f"The substring '{substring}' occurs {string.count(substring)} times")
    elif choice == '6':
        old_substr = input("Enter the substring to replace: ")
        new_substr = input("Enter the new substring: ")
        print("String after replacement:", string.replace(old_substr, new_substr))
    elif choice == '7':
        delimiter = input("Enter the delimiter to split by: ")
        print("Splitted string:", string.split(delimiter))
    elif choice == '8':
        lst = input("Enter a list of strings separated by spaces: ").split()
        delimiter = input("Enter the delimiter to join with: ")
        print("Joined string:", delimiter.join(lst))
    else:
        print("Invalid choice!")

string_manipulation()