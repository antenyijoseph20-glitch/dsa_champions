
def balanced_brackets(text):
    stack = []

    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in text:
        if character in "([{":
            stack.append(character)

        elif character in ")]}":
            if not stack:
                return False

            if stack[-1] != matching[character]:
                return False

            stack.pop()

    return len(stack) == 0


print(balanced_brackets("(hello)"))
print(balanced_brackets("{[()]}"))
print(balanced_brackets("([)]"))
print(balanced_brackets("((hello)"))
