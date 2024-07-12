# Orijinal print fonksiyonunu sakla
original_print = print

# Yeni bir print fonksiyonu tanımla
def custom_print(*args, **kwargs):
    # Burada istediğiniz özel işlemleri gerçekleştirin
    reversed_args = [str(arg)[::-1] for arg in args]
    # Orijinal print fonksiyonunu çağır
    original_print(*reversed_args, **kwargs)

# Yeni print fonksiyonunu kullanıma al
print = custom_print

# Test et
print("merhaba")  # Çıktı: abahrem