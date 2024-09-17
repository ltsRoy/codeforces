
def split_by_same_char(s):
    result = []
    i = 0
    while i < len(s):
        start_char = s[i]
        j = i + 1
        while j < len(s) and s[j] != start_char:
            j += 1
        result.append(s[i:j+1])
        i = j + 1
    return result
w = int(input())
for _ in range(w):
    n = int(input())
    s = input()
    split_strings = split_by_same_char(s)
    total_length = sum(len(substring) for substring in split_strings)
    if total_length == len(s):
        print("YES")
    else:
        print("NO")

        
        