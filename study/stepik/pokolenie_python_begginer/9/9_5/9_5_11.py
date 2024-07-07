inp_nickname = input()
if inp_nickname[0] == '@' and inp_nickname[1:].isalnum() and (5 <= len(inp_nickname) <= 15) and (
        inp_nickname.islower() or inp_nickname[1:].isdigit()):
    print('Correct')
else:
    print('Incorrect')
