class StringHandler:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Nhập chuỗi: ")

    def print_String(self):
        print("Chuỗi in hoa:", self.string.upper())

# Tạo đối tượng StringHandler
handler = StringHandler()

# Gọi phương thức get_String và print_String
handler.get_String()
handler.print_String()
