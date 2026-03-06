usernames = ["absurdhere", "shirishpandey123", "neupanerajan", "sureshchaudhary"]
while True:
    create_username = input("create your username: ")
    # check username exist on usernames or not and  give either true or false(bolean `value)
    check_username = create_username in usernames
    if check_username:
        print("username already exist try another username")
    else:
        usernames.append(create_username)
        print("username  is successfully created!!")
        break
print(usernames)