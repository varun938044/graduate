word1 = input()
word2 = input()
 
word1 = sorted(word1)
word2 = sorted(word2)
if word1 == word2:
    print("Anagrams")
else:
    print("Not a anagrams")
 
