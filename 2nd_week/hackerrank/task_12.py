
# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

# One fine day, a finite number of tourists come to stay at the hotel. 
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of K members per group where K ≠ 1.

# The Captain was given a separate room, and the rest were given one room per group.

# Mr. Anant has an unordered list of randomly arranged room entries. 
# The list consists of the room numbers for all of the tourists. The room numbers 
# will appear K times per group except for the Captain's room.

# Mr. Anant needs you to help him find the Captain's room number. 
# The total number of tourists or the total number of groups of families is not known to you. 
# You only know the value of K and the room number list.

# Input Format

# The first line consists of an integer,K , the size of each group.
# The second line contains the unordered elements of the room number list.

K = int(input())

room_numbers = list(input().split(" "))

quantity_in_room = {}
captian_room_number = ''

for item in room_numbers:
    if item in quantity_in_room:
        quantity_in_room[item] += 1
    else:
        quantity_in_room[item] = 1

for key, value in quantity_in_room.items():
    if value == 1:
        captian_room_number = key

print(captian_room_number)
