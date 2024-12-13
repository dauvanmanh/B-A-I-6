class Hinhchunhat:
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong

    def area(self):
        return self.chieudai * self.chieurong

# Tạo đối tượng Hinhchunhat với chiều dài 5 và chiều rộng 4
hinhchunhat = Hinhchunhat(5, 4)
print("Diện tích hình chữ nhật là:", hinhchunhat.area())
