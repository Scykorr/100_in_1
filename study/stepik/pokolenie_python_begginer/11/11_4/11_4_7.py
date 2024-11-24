string_amount = int(input())
string_list = list()
for _ in range(string_amount):
    string_list.append(input())
search_word_amount = int(input())
search_word_list = list()
for _ in range(search_word_amount):
    search_word_list.append(input())
for string in string_list:
    counter_in = 0
    for word in search_word_list:
        if word.lower() in string.lower():
            counter_in += 1
    if counter_in == search_word_amount:
        print(string)
