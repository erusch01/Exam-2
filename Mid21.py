#Emily Rusch

def count_hashtags(string):
    index = 0
    total = 0
    while index < len(string):
        for char in string:
            if char == "#":
                total += 1
                index += 1
            else:
                index += 1
    return total

print(count_hashtags("#Today is going to be a good day. #Thursday. #Programming"))
