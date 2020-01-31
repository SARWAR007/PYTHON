def char_frequency(str1):
    dict = {}
    for n in str1:
        print(n)
        keys = dict.keys()
        print("dictionary",keys)
        if n in keys:
            dict[n] += 1
            print("Dictionary data",dict[n])
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))
