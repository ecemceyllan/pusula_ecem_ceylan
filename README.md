# pusula_ecem_ceylan
ecem ceylan
ecemceyllan12@gmail.com 
Bu proje, fiziksel tıp ve rehabilitasyon verilerini içeren bir veri seti üzerinde  veri analizi  ve veri ön işleme çalışmasını kapsamaktadır. Amaç, tedavi süresi hedef değişkenine odaklanarak veriyi modellemeye hazır hâle getirmektir.
Veri Seti
Gözlem Sayısı: 2235
Özellikler: 13 (Yaş, Cinsiyet, Kan Grubu, Uyruk, Kronik Hastalık, Bölüm, Alerji, Tanılar, Tedavi Adı, Tedavi Süresi, Uygulama Yerleri, Uygulama Süresi, HastaNo)
Yapılan İşlemler:
1-Sayısal sütunların temizlenmesi:
Yaş, UygulamaSuresi, TedaviSuresi sütunlarındaki metin verilerden sayısal değerler çıkarıldı.
2-Eksik değerlerin doldurulması:
Sayısal sütunlar için ortalama değer kullanıldı.
Kategorik sütunlar için mod (en sık görülen değer) kullanıldı.
3-Kategorik verilerin OneHotEncoder ile dönüştürülmesi:
Cinsiyet, KanGrubu, Uyruk, Bolum, TedaviAdi, UygulamaYerleri, KronikHastalik, Alerji, Tanilar sütunları dönüştürüldü.
Veri görselleştirme:
Yaş ve Tedavi Süresi dağılımları histogramlarla gösterildi.
Veri seti klasörle aynı dosyada bulunmalıdır,çalıştırdıktan sonra variable explorer kısmından verileri inceleyebilirsiniz.
