"""функция по переводу строк в верхний регистр"""
def upper_str():
    user_input = input()
    return user_input.upper


"""функция по переводу первой буквы слова в заглавную"""
def upcase_first_letter(s):
    return s[0].upper() + s[1:]