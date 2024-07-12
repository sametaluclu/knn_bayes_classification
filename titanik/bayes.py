class CustomInt(int):
    def __add__(self, other):
        return self * other

# int sınıfını değiştirelim
int = CustomInt

# Kullanımı
a = int(8)
b = int(5)
c = a + b
print(c)  # Bu noktada 40 çıktısını alırsınız
