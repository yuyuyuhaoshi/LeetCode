chars = ["a","a","b","c"]

chars_len = len(chars)

count = 0
l = list()
latest_char = chars[0]

for index, char in enumerate(chars[:-1]):
    count += 1
    if char != chars[index + 1] :
    
        
        if count == 1:
            l.append(latest_char)
        else:
            l.append(latest_char)
            l.append(count)
            count = 0
    latest_char = char
print(latest_char)        
if latest_char == chars[-1]:
    print(latest_char)
    count += 1
    l.append(char)
    l.append(count)
else:
    l.append(chars[-1])

print(l)