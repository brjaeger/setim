1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery diperlukan dalam pengimplementasian platform untuk memastikan bahwa data dapat berpindah antar komponen dan juga layanan dalam suatu sistem secara akurat, efisien, dan aman. 

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON lebih ringan dan terlihat lebih sederhana dibandingkan dengan XML, contohnya yaitu penggunaan tag pembuka dan juga tag penutup yang ada pada XML, dan juga lebih mudah dibaca, dan dipahami oleh manusia.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan validasi yang didefinisikan di model atau di form. Fungsi ini memvalidasi data pada:

- Validasi tipe data: Memastikan data yang diinput sesuai dengan tipe yang diharapkan (misalnya, angka, teks, tanggal).

- Validasi custom: Validasi tambahan yang bisa didefinisikan pengguna, seperti panjang minimal, pola, atau logika khusus lainnya.

Jika data valid, is_valid() akan mengembalikan True dan form akan menyimpan data yang sudah bersih (cleaned data) dalam atribut cleaned_data. Jika tidak valid, form akan mengembalikan kesalahan yang sesuai untuk diperbaiki.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token (Cross-Site Request Forgery token) digunakan untuk mencegah serangan CSRF, di mana penyerang dapat mencoba mengelabui pengguna untuk mengirimkan permintaan yang tidak diinginkan (misalnya, mengirimkan formulir atau melakukan transaksi) ke server aplikasi tanpa sepengetahuan pengguna.

Jika kita tidak menambahkan csrf_token pada form Django:

- Rentan terhadap serangan CSRF: Tanpa csrf_token, form di situs web kita bisa dieksploitasi oleh penyerang dengan cara mengarahkan pengguna untuk mengirimkan request berbahaya ke server kita melalui browser yang telah terotentikasi.

- Penyerang bisa memanfaatkan sesi pengguna: Penyerang dapat memanfaatkan sesi pengguna yang sudah masuk ke aplikasi, sehingga mereka dapat mengirim permintaan seperti penggantian kata sandi, pengiriman formulir, atau transaksi lain yang dilakukan tanpa izin pengguna.

Dengan csrf_token, setiap form yang dikirimkan oleh pengguna memiliki token unik yang hanya diketahui oleh server dan browser pengguna. Jika token tidak cocok atau hilang, server akan menolak permintaan tersebut.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jadi pertama-tama itu saya membuat template yang berisikan dengan base.html yang berfungsi sebagai template dasar yang digunakan untuk kerangka umum pada halaman website, selanjutnya menyesuaikan beberapa hal pada settings.py, lalu mengubah struktur pada main.html agar dapat menggunakan base.html sebagai kerangka utama. Setelah itu saya menambahkan uuid pada models.py, lalu saya membuat form yang berisi name,price, dan juga description yang ada pada forms.py. lalu saya mengubah pada berkas yang sama yaitu fungsi create_mood__entry yang berfungsi untuk menerima parameter request, lalu menyesuaikan yang berkas-berkas yang lain. Selanjutnya saya mencoba untuk mengembalikan data dalam bentuk XML, dan juga JSON dengan cara membuat return function untuk masing-masing XML, dan juga JSON, dan terakhir saya mencoba untuk mengembalikan data berdasarkan ID dalam bentuk XML, dan juga JSON.

XML
![Screenshot (134)](https://github.com/user-attachments/assets/dfc5e4e8-3d26-4bb5-904b-e4b117351c15)

JSON
![Screenshot (135)](https://github.com/user-attachments/assets/06ad5b47-66dc-423c-a22a-8489d85a5124)

XML by ID
![Screenshot (136)](https://github.com/user-attachments/assets/5e3d0e3f-ff21-4301-9bff-70e05cda8a7c)

JSON by ID
![Screenshot (137)](https://github.com/user-attachments/assets/a6aed757-6ef6-481c-89aa-71de3b87f589)


