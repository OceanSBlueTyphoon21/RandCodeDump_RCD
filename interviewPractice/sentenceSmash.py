def smash(words):
    smashword = ""
    for i in range(0,len(words)):
        if words[i] != words[len(words)-1]:
            smashword+=words[i] + " "
        else:
            smashword+=words[i]
    return smashword


word_arr = ['hello', 'world', 'this', 'is', 'great']
#print(word_arr[len(word_arr)-1])
print(smash(word_arr))
