class Nguoi:
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Tạo đối tượng Nam và Nu
aNam = Nam()
aNu = Nu()

print("Giới tính của aNam:", aNam.getGender())
print("Giới tính của aNu:", aNu.getGender())
