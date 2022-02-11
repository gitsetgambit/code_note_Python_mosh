# sentence = "madam"

# # Time complexity : O(n)

# """
# {a : 2
# a : 4
# d : 1
# m : 2}
# """


# number_of_words = {}
# for word in sentence:
#     if word in number_of_words:
#         number_of_words[word] += 1
#     else:
#         number_of_words[word] = 1
# print(number_of_words)

# # a = sorted(number_of_words.items(), key=lambda k: k[1], reverse=True)
# # print(a[0])

# # 27 * 27
# # Time complexity : O(n^2)
# # no description just go through this
# # for i in sentence:
#     # print(i, sentence.count(i))

s = "madam"

visited = [0 for i in range(0, 26)]

for character in s:
    if (visited[ord(character) - 97] == 0):
        visited[ord(character) - 97] = 1
        count = 0
        for c in s:
            if (c == character):
                count += 1
        print(character, " -> ", count)
