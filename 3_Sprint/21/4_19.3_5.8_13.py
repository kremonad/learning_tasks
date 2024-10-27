def is_correct_bracket_seq(seq):
    seq_list = [x for x in seq]
    open_brackets = '{[('
    closed_brackets = ')]}'
    bracket_dict = {')': '(', '}': '{', ']': '['}
    if seq == '':
        return True
    closed_stack = []
    opened_stack = []
    if seq_list[-1] in open_brackets:
        return False
    for _ in range(len(seq_list)):
        last_bracket = seq_list.pop()
        if last_bracket in closed_brackets:
            correct = False
            closed_stack.append(last_bracket)
        elif last_bracket in open_brackets:
            opened_stack.append(last_bracket)
            try: 
                if bracket_dict[closed_stack.pop()] == opened_stack.pop():
                    correct = True
                else:
                    return False
            except IndexError:
                return False
    return correct


if __name__ == '__main__':
    seq = input()
    print(is_correct_bracket_seq(seq))