inp_comments_amount = int(input())
for num in range(1, inp_comments_amount + 1):
    inp_comment = input()
    if inp_comment.isspace() or inp_comment == '':
        print(f'{num}: COMMENT SHOULD BE DELETED')
    else:
        print(f'{num}: {inp_comment}')
