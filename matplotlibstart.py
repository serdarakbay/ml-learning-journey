import matplotlib.pyplot as plt
# artış azaış grafikleri
# x = [1, 2, 3, 4, 5]
# y = [10, 25, 15, 30, 20]    
# plt.plot(x, y)
# plt.title("Weekly Sales")
# plt.xlabel("Week")
# plt.ylabel("Sales")
# plt.show()
#----------------------------------------------------
# farklı kategorilerin değerlerii gösterir
# kategoriler = ["Fire", "Water", "Grass", "Psychic"]
# adet = [12, 18, 9, 7]

# plt.bar(kategoriler, adet)
# plt.title("Tipe Göre Pokemon Sayısı")
# plt.xlabel("Tip")
# plt.ylabel("Adet")
# plt.show()
#--------------------------------------------------------
#iki değişken arasındaki ilişkiyi gösterir
# boy = [1.2, 1.5, 0.7, 2.0, 1.8, 0.5]
# kilo = [9.0, 30.0, 6.5, 90.0, 60.0, 4.0]

# plt.scatter(boy, kilo)
# plt.title("Boy - Kilo İlişkisi")
# plt.xlabel("Boy")
# plt.ylabel("Kilo")
# plt.show()
# ---------------------------------------------------------
#verinin dağılımını gösterir
# import numpy as np
# veriler = np.random.randn(1000)

# plt.hist(veriler, bins=30)
# plt.title("Normal Dağılım")
# plt.xlabel("Değer")
# plt.ylabel("Frekans")
# plt.show()
#---------------------------------------------------------
#bir bütünün parçalarının oranını gösterir
# pokemon_type=["Fire","Water","Grass","Psychic"]
# total=[12,18,9,7]
# plt.pie(total,labels=pokemon_type,autopct="%1.1f%%")
# plt.title("Pokemon Type Distribution")
# plt.show()