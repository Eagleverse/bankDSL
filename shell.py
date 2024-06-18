import banking
from apparatus import string_with_arrows


def main():
    text = ""
    while text.strip() != "exit()":
        text = input('hi > ')
        if text.strip() == "":
            continue
        if text.strip() == "exit()":
            break

        result, error = banking.run('<stdin>', text)


#
#       if error:
#          print(error.as_string())
#     elif result:
#        if len(result.elements) == 1:
#           print(repr(result.elements[0]))
#      else:
#         print(repr(result))


if __name__ == "__main__":
    main()
