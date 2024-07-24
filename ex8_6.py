"""
Đây là bài đọc. Ví dụ inheritance
sử dụng super để gọi method từ class parent.

Trong ví dụ này có override cả init, lẫn keu.

"""


class Cat:
    def __init__(self, name, age, c):
        self.name = name
        self.age = age
        self.color = c

    def __str__(self):
        return f"{self.name} {self.age} {self.color}"

    def keu(self):
        print("Meo meo")


class DogCat(Cat):
    def __init__(self, name, age, c, toy):
        super().__init__(name, age, c)
        self.toy = toy

    def key(self):
        super().keu()
        print("gau gau")


print("=== Here is Cat ===")
c = Cat("Meo", 2, "yellow")
print(c)
c.keu()

print("=== Here is DogCat ===")
dc = DogCat("Meogau", 3, "black", "ball")
print(dc)
dc.keu()
