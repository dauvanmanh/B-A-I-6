class StringManipulation:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        words = self.input_string.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words

# Dữ liệu vào
input_string = 'hello .py'
manipulator = StringManipulation(input_string)

# Đầu ra
print("Chuỗi đảo ngược:", manipulator.reverse_words())
