def reapeting_character(str):
    sub_string = {}
    cur_sub_start = 0
    cur_lenght = 0
    longest = 0 
    for i, letter in enumerate(str):
        if letter in sub_string and sub_string[letter] >= cur_sub_start:
            cur_sub_start = sub_string[letter] + 1
            cur_lenght = i - sub_string[letter]
            sub_string[letter] = i
        else:
            sub_string[letter] = i
            cur_lenght += 1
            if cur_lenght > longest:
                longest = cur_lenght
    return longest

print(reapeting_character("abcabcbb"))