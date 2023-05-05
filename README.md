# Flask_Upload_File
#EN
  This code creates a web server using the Flask web application framework and provides a simple example for file uploading.
  The code first creates an application object from the Flask library. Then, a function is defined for the home page ("/") of the website, which returns an HTML page using an HTML template named "index.html".
  The file uploading process is defined on the "/upload" route. This function uploads the file when it receives a POST request and saves the file to a folder on the server using the name and path of the uploaded file. Finally, it redirects back to the index page.
  The folder name for file uploads is specified as "upload" in the code and should be created beforehand.
  This code can be used as a web server to receive files from other computers on the same network. By running this code on a server computer, other computers can use their web browsers to upload or download files from the server computer. However, the server computer needs to be accessible on the network, and some security measures should be taken to prevent security vulnerabilities during the file uploading process.

#TR 
  Bu kod, Flask web uygulama çatısını kullanarak bir web sunucusu oluşturur ve dosya yükleme işlemini gerçekleştirmek için basit bir örnek sunar.
  Kodda, Flask kütüphanesinden bir uygulama objesi oluşturulur. Ardından, web sitesinin ana sayfası için ("/" yolunda) bir işlev tanımlanır ve bu işlev, index.html adlı bir HTML şablonunu kullanarak bir HTML sayfası döndürür.
  Dosya yükleme işlemi "/upload" yolunda tanımlanmıştır. Bu işlev, POST isteği aldığında dosyayı yükler ve yüklenen dosyanın adını ve yolunu kullanarak dosyayı sunucuda bir klasöre kaydeder. Son olarak, index sayfasına geri yönlendirme yapılır.
  Kodda, dosyanın yükleneceği klasörün adı "upload" olarak belirtilmiştir. Bu klasör önceden oluşturulmalıdır.
  Bu kod, aynı ağda bulunan bilgisayarlardan dosya alma işlemini gerçekleştirmek için bir web sunucusu olarak kullanılabilir. Sunucu bilgisayarda çalıştırılan bu kod, diğer bilgisayarların web tarayıcılarını kullanarak sunucu bilgisayardaki dosyaları yükleyebilir veya indirebilir. Bunun için sunucu bilgisayarın ağa açık olması gerekmektedir. Ayrıca, dosya yükleme işlemi sırasında güvenlik açıklarını önlemek için bazı güvenlik önlemleri alınması tavsiye edilir.
