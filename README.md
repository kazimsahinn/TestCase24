# TestDownloadInvoice Dökümantasyonu

Bu sınıf, kullanıcı kayıt işlemini, ürün ekleyip sepet işlemlerini, sipariş verme süreçlerini ve fatura indirme işlemlerini otomatikleştiren bir pytest testidir. Test, kullanıcı kaydını oluşturur, bir ürün ekler, sepete ekleme ve ödeme işlemlerini yapar, fatura indirir ve sonunda kullanıcı hesabını siler.

## Kullanılan Sınıflar ve Yöntemler
HomePage: Ana sayfa öğelerini temsil eden sınıf. <br/>
CartPage: Sepet ve ödeme işlemleriyle ilgili sayfa öğelerini temsil eden sınıf.<br/>
SignupPage: Kayıt sayfası öğelerini temsil eden sınıf.<br/>
AccountPage: Hesap bilgilerini temsil eden sınıf.<br/>
## Test İş Akışı
**1. Giriş ve Sayfa Yüklemeleri**<br/>
Test, belirli bir web sayfasına (http://automationexercise.com) gider.<br/>
Ana sayfada logonun görünürlüğü doğrulanır.<br/>
**2. Ürün Sepete Ekleme**<br/>
Ana sayfada aşağı kaydırılır.<br/>
Ürün üzerine gelinir ve ürün sepete eklenir.<br/>
Ürünün başarıyla sepete eklendiği mesajı doğrulanır.<br/>
Alışverişe devam edilir ve sepet açılır.<br/>
**3. Sepet ve Ödeme İşlemleri**<br/>
Sepet menüsünün görünürlüğü doğrulanır.<br/>
Ödeme işlemine geçilir.<br/>
Kayıt ekranına yönlendirilir.<br/>
Yeni kullanıcı oluşturma formu doldurulur ve hesap oluşturulur.<br/>
Hesap bilgilerinin girildiği form doldurulur ve hesap oluşturma işlemi tamamlanır.<br/>
Hesabın başarıyla oluşturulduğu mesajı doğrulanır.<br/>
Kullanıcı hesabına giriş yapılır ve sepet tekrar açılır.<br/>
Teslimat ve fatura adreslerinin aynı olduğu doğrulanır.<br/>
Sipariş detayı girilir ve ödeme yapılır.<br/>
Ödeme işleminin başarılı olduğu doğrulanır.<br/>
**4. Fatura İndirme**<br/>
Fatura indirilir ve fatura indirme işleminin başarılı olduğu doğrulanır.<br/>
**5. Hesap Silme ve Çıkış**<br/>
Kullanıcı hesabı silinir ve silme işleminin başarılı olduğu doğrulanır.
