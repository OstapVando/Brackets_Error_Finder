def Err(expression):
    index = 0
    stack = []
    stack_index = []
    ans = True

    for char in expression:

        # stack expand
        if char in ['[', '{', '(']:
            stack.append(char)
            index = index + 1
            stack_index.append(index)

        # any other char in line
        elif char not in ['[', '{', '(',']', '}', ')']:
            index = index + 1

        # stack decrease
        else:
            if char == '}':
                try:
                    if stack.pop() == '{':
                        stack_index.pop()
                        index = index + 1
                    else:
                        index = index + 1
                        ans = False
                        break
                except IndexError:
                    index = index + 1
                    ans = False
                    break

            elif char == ']':
                try:
                    if stack.pop() == '[':
                        stack_index.pop()
                        index = index + 1
                    else:
                        index = index + 1
                        ans = False
                        break
                except IndexError:
                    index = index + 1
                    ans = False
                    break

            elif char == ')':
                try:
                    if stack.pop() == '(':
                        stack_index.pop()
                        index = index + 1
                    else:
                        index = index + 1
                        ans = False
                        break
                except IndexError:
                    index = index + 1
                    ans = False
                    break


    if ans == True:
        if stack == []:
            print('Success')
        else:
            print(stack_index.pop())
    else:
            print(index)  # Error


if __name__ == "__main__":
    Err(input())