
def good_password(password):
    good_trios = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn', 'mno', 'nop',
                  'opq', 'pgr', 'qrs', 'rst', 'stu', 'tuv', 'uvx', 'vxy', 'xyz']
    good_duos = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq',
                 'rr', 'ss', 'tt', 'uu', 'vv', 'xx', 'yy', 'zz']
    trio_check = any(True if x in password else False for x in good_trios)
    duo_check = [1 if x in password else 0 for x in good_duos]
    char_check = all(True if x not in password else False for x in ['i', 'o', 'l'])
    if (sum(duo_check) > 1) and trio_check and char_check and (len(password) == 8):
        return True
    return False


pas = 'hxbxxzzz'
counter = 0


while not good_password(pas):
    pas = list(pas)

    for i in range(len(pas) - 1, -1, -1):
        pas[i] = chr((ord(pas[i]) - ord('a') + 1) % 26 + ord('a'))
        if pas[i] != 'a':
            break
    pas = ''.join(pas)

print(pas)

