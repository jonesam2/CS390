def compress(chars):

    i = 0
    count = 1

    for j in range(1, len(chars) + 1):
        if j < len(chars) and chars[j] == chars[j - 1]:  # check  char at index j is same as the one before if so increase count
            count += 1
        else:
            chars[i] = chars[j - 1]  # if not the same, switch to next different char
            i += 1
            if count > 1:
                for k in str(count):  # allows more than one digit #s to be separated into sep chars
                    chars[i] = k
                    i += 1
            count = 1
    return i


print(compress(["a", "a", "b", "b", "c", "c", "c"]))

print(compress(["c","c","c","c","e","e","f","t","t"]))