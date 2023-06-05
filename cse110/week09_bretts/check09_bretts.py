
friends = []
name = ""

# while friend != "end":
#     friend = input("Type the name of a friend: ").lower()
#     friends.append(friend)
# for i in range(0, len(friends) - 1):
#     print("Your friends are:")
#     print(friends[i].capitalize())


while name != "end":
    name = input("Type the name of a friend: ").lower()

    if name != "end":
        friends.append(name)
print()
print("Your friends are:")

for friend in friends:
    print(friend.capitalize())
