def compress_string(s):
    if not s:
        return ""

    res = ""
    count = 0
    current_char = s[0]

    for char in s:
        if char == current_char:
            count += 1
        else:
            res += current_char + (str(count) if count > 1 else "")
            current_char = char
            count = 1

    # Add the last accumulated character and count
    res += current_char + (str(count) if count > 1 else "")

    return res


s = "bbbcaaccccdd"
print(compress_string(s))
