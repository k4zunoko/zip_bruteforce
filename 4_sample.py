import itertools

password_length = 3
charset = "abcdefghijklmnopqrstuvwxyz"
passwords = list(itertools.product(charset, repeat=password_length))

print(passwords)