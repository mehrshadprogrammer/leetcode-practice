str = "mehrshad"
arrWithOutVowels = []
vowlesCharechter = ['a', 'e', 'u', 'i', 'o']
strWithOutVowelsCharechter = ''


for ch in str:
    if ch not in vowlesCharechter:
        arrWithOutVowels.append(ch)
        strWithOutVowelsCharechter = ''.join(arrWithOutVowels)
    else:
        pass

print(strWithOutVowelsCharechter)