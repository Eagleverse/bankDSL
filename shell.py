import banking_dsl

while True:
    text = input('main > ')
    result, error = banking_dsl.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
