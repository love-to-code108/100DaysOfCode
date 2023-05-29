import collections

n = int(input())
ordered_count = collections.OrderedDict()
uniq_words = 0
for i in range(n):
    word_list = input()
    if (word_list in ordered_count):
        ordered_count[word_list] += 1
    else:
        ordered_count[word_list] = 1
        uniq_words += 1

print (uniq_words)
val_lst = list(ordered_count.values())
print (*val_lst)
