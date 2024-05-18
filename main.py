from stack import Stack


def is_balanced(brackets_input):
    stack = Stack()
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for char in brackets_input:
        if char in brackets:
            stack.push(char)
        elif not stack.is_empty() and brackets[stack.peek()] == char:
            stack.pop()
        else:
            return False

    return stack.is_empty()


if __name__ == '__main__':
    brackets_input = input('Введите набор скобок: ')
    if is_balanced(brackets_input):
        print('Сбалансированно')
    else:
        print('Несбалансированно')
