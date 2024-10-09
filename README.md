TUGAS 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
5. Mengapa model pada Django disebut sebagai ORM?

Jawaban
1. Membuat Main : Saya mulai dengan membuat aplikasi dengan nama main dengan menjalankan sintaks di cmd "python manage.py startapp main"

- Membuat Model: Pada tahap ini saya mengganti sesuai dengan ketentuan soal yaitu name, description, dan juga price yang akan dipakai pada views.py

- Membuat Views: Di views.py saya menambahkan atribut-atribut yang akan digunakan dalam main.html nanti

- Menghubungkan URL: Pada urls.py gunanya untuk menghubungkan atau melakukan routing dengan urls yang akan ditampilkan sesuai dengan nama pada project 

- Membuat Template: Pada template ini berisi main.html yang berisi project tentang apa yang telah kita buat yaitu e-commerce yang telah dihubungkan melalui urls, sehingga dapat dibuka. Pada template ini juga berisi tentang data-data yang telah dimasukkan sebelumnnya yaitu name, price, dan juga description

2. "Client Request -> Django URLConf (urls.py) -> View (views.py) -> Model (models.py) -> Template (HTML) -> Response

- **urls.py**: Menerima request dan memetakan ke view yang sesuai.
- **views.py**: Mengambil data dari model dan mengembalikan response dengan template HTML.
- **models.py**: Mendefinisikan struktur data yang disimpan di database.
- **Template HTML**: Menampilkan data yang diambil dari view.

3.  Git adalah sistem kontrol versi yang digunakan untuk melacak perubahan dalam kode sumber selama pengembangan perangkat lunak. Git memungkinkan pengembang untuk bekerja secara kolaboratif, mengelola versi kode, dan mengembalikan perubahan jika diperlukan.

4. Django adalah framework yang lengkap dan memiliki banyak fitur bawaan yang memudahkan pengembangan aplikasi web. Django juga memiliki dokumentasi yang baik dan komunitas yang besar, sehingga cocok untuk pemula.

5. Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa perlu menulis query SQL secara langsung. ORM memetakan tabel database ke kelas Python dan kolom tabel ke atribut kelas.


TUGAS 3
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

=======
XML
![Screenshot (134)](https://github.com/user-attachments/assets/dfc5e4e8-3d26-4bb5-904b-e4b117351c15)

JSON
![Screenshot (135)](https://github.com/user-attachments/assets/06ad5b47-66dc-423c-a22a-8489d85a5124)

XML by ID
![Screenshot (136)](https://github.com/user-attachments/assets/5e3d0e3f-ff21-4301-9bff-70e05cda8a7c)

JSON by ID
![Screenshot (137)](https://github.com/user-attachments/assets/a6aed757-6ef6-481c-89aa-71de3b87f589)


>>>>>>> c4ff8fd040b362e05da2d0e2709d946f40af1780

TUGAS 4
1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
HttpResponseRedirect() merupakan kelas yang mengembalikan HTTP response dengan kode status 302 (Redirect), sedangkan redirect() merupakan fungsi shortcut yang mengembalikan HttpResponseRedirect, tetapi lebih fleksibel, karena kita bisa memberikan URL sebagai string, nama view, ataupun objek model

2. Jelaskan cara kerja penghubungan model Product dengan User!
Untuk menghubungkan model Product dengan User, biasanya menggunakan ForeignKey. Dengan ForeignKey setiap product akan terhubung dengan satu pengguna saja. Jika pengguna dihapus, maka semua produk terkait akan dihapus juga menggunakan on_delete=models.CASCADE. Untuk menambahkan produk baru, kita cukup mengaitkan produk dengan pengguna yang sedang login.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
- Authentication: Proses untuk memverifikasi identitas pengguna. Ini memastikan bahwa pengguna adalah siapa mereka. Saat pengguna login dengan nama pengguna dan kata sandi, itu merupakan proses autentikasi.

- Authorization: Proses untuk menentukan apakah pengguna yang terautentikasi memiliki izin untuk melakukan tindakan tertentu atau mengakses sumber daya tertentu. Misalnya, seorang pengguna mungkin memiliki akses untuk melihat konten tetapi tidak untuk mengeditnya.

Implementasi di Django:
Django menggunakan sistem autentikasi built-in untuk mengelola login dan logout. Ketika pengguna login, Django akan memeriksa kredensial yang diberikan dan membuat sesi untuk pengguna yang terautentikasi.
Untuk otorisasi, Django memberikan kontrol akses berbasis izin dan grup. Kamu bisa menentukan izin yang berbeda untuk model dan menggunakan decorator seperti @login_required untuk melindungi tampilan tertentu.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django menggunakan session untuk mengingat pengguna yang telah login. Ketika pengguna login, Django akan membuat sesi untuk pengguna tersebut dan menyimpannya di database atau menggunakan cookie. Kegunaan lain dari cookies adalah untuk menyimpan informasi pengguna antara session, seperti preferensi atau data keranjang belanja.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Jadi langkah pertama yaitu kita menambahkan fungsi register di views.py untuk menampilkan dan menampilkan form registrasi pengguna, lalu membuat file template baru yaitu register.html untuk menampilkan form registrasi, dan menambahkan path baru di urls.py untuk halaman registrasi 
- Langkah kedua yaitu membuat impor authenticate, login, dan AuthenticationForm di views.py, lalu menambahkan fungsi login_user di views.py untuk melakukan autentikasi dan login pengguna, dan membuat file template yaitu login.html untuk menampilkan form login, dan menambahkan path baru di urls.py untuk login
- Langkah ketiga yaitu membuat impor logout pada views.py, lalu menambahkan fungsi logout_user di views.py untuk melakukan logout dan menghapus sesi pengguna, setelah itu kita membuat tombol logout di main.html, dan menambahkan path baru pada urls.py
- Langkah keempat yaitu melakukan impor login_required di views.py, dan menambahkan decorator @login_required di atas fungsi show_main agar pengguna diharuskan untuk melakukan login terlebih dahulu sebelum dapat mengakses ke halaman main 
- Langkah kelima yaitu melakukan impor HttpResponseRedirect, reverse, dan datetime di views.py, lalu menambahkan function untuk menyimpan cookie last_login saat login di login_user, dan menampilkan last_login di halaman main dengan menambahkannya di context, dan menambahkan response.delete_cookie('last_login') untuk menghapus cookie saat logout
- Langkah keenam yaitu melakukan impor user dari django.contrib.auth.models di models.py, lalu menambahkan field ForeignKey pada model untuk menghubungkan entri dengan pengguna, dan melakukan migrate untuk menerapkan perubahan pada models.py 

TUGAS 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan Prioritas Pengambilan CSS Selector: Ketika ada beberapa CSS selector yang diterapkan pada elemen HTML yang sama, browser menentukan prioritas berdasarkan spesifisitas dan urutan penerapan aturan CSS. Berikut urutan prioritasnya:
- Inline styles (ditulis langsung pada elemen HTML) memiliki prioritas tertinggi.
- ID selector (#id) memiliki prioritas lebih tinggi dibandingkan class, attribute, atau element selectors.
- Class selector (.class), attribute selector ([type="text"]), dan pseudo-classes (:hover, :focus) berada di level berikutnya.
- Element selector (div, p, h1) dan pseudo-elements (::before, ::after) memiliki prioritas paling rendah.
- Jika dua selector memiliki tingkat spesifisitas yang sama, aturan yang diterapkan terakhir di file CSS akan diambil.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design sangat penting karena pengguna saat ini mengakses web dari berbagai perangkat dengan ukuran layar yang berbeda, seperti smartphone, tablet, dan desktop. Responsive design memastikan tampilan dan fungsi aplikasi web tetap optimal di semua perangkat.
Contoh aplikasi yang menerapkan responsive design:
Sudah menerapkan: Twitter, Bootstrap, Airbnb.
Belum menerapkan: Situs-situs lama yang hanya dirancang untuk tampilan desktop, misalnya beberapa website institusi 
pendidikan atau pemerintahan yang belum diperbarui.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Perbedaan antara Margin, Border, dan Padding:
- Margin: Ruang di luar border, digunakan untuk menciptakan jarak antara elemen dan elemen lainnya. Margin tidak memengaruhi ukuran elemen itu sendiri.
- Border: Garis yang mengelilingi elemen di antara padding dan margin. Border bisa diberi warna, ketebalan, dan gaya (solid, dashed, dll.).
- Padding: Ruang di dalam border, antara konten elemen dan border elemen tersebut. Padding memperbesar area elemen, tetapi tidak mengubah ukuran konten.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flexbox: Flexbox adalah layout model satu dimensi yang digunakan untuk mengatur elemen secara fleksibel dalam satu arah, baik itu baris (row) atau kolom (column). Flexbox mempermudah pembuatan tata letak responsif tanpa menggunakan banyak float atau positioning.
Kegunaan:
- Menyusun elemen secara horizontal atau vertikal dengan mudah.
- Menyebar ruang kosong antar elemen atau menyusun elemen agar memiliki ukuran yang sama.
- Cocok untuk tata letak komponen-komponen kecil seperti navbar, tombol, atau card

- Grid Layout: Grid adalah layout model dua dimensi yang memungkinkan pengaturan elemen secara vertikal dan horizontal dalam kolom dan baris. Grid mempermudah pembuatan tata letak yang lebih kompleks seperti halaman web dengan beberapa kolom dan baris.
Kegunaan:
- Membuat tata letak halaman secara kompleks dan terstruktur.
- Mengontrol posisi dan ukuran elemen baik dalam arah horizontal maupun vertikal.
- Cocok untuk tata letak halaman utama, galeri, atau dashboard

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Jadi Langkah pertama yaitu membuat edit_product, dengan cara yaitu membuat sebuah fungsi baru bernama edit_product yang menerima parameter request, dan juga id, lalu buatlah berkas HTML baru dengan nama edit_mood.html pada main/templates. Setelah itu masukkan import di urls.pym dan juga path urlnya ke ulrpattern agar bisa terhubung.
- Langkah kedua yaitu membuat delete_product dengan cara yang agar mirip dengan langkah sebelumnya yaitu pertama-tama membuat fungsi di views.py lalu menambahkannya ke urls.py dan sambungkan ke urlpatterns
- Langkah ketiga yaitu memasukkan tombol edit dan juga delete ke dalam main.htm, dengan cara menambahkan referensi url main:edit_product, dan juga main:delete_product
- Langkah keempat yaitu menambahkan navigation bar pada aplikasi, pertama-tama buatlah berkas baru dengan nama navbar.html untuk memasukkan kode agar dapat membuat navigation bar tersebut, lalu agar muncul di setiap tampilan tambahkan {% include 'navbar.html' %} di halaman-halaman lainnya.
- Langkah selanjutnya yaitu menambahkan middleware WhiteNoise pada settings.py, agar file statis bisa diakses pada deployment user secara default, tanpa harus konfigurasi yang kompleks.
- Langkah selanjutnya yaitu menambahkan folder static pada root directory, yang berisi folder css, dan juga image, buatlah berkas global.css agar style CSS yang ditambahkan bisa digunakan dalam template Django.
- Langkah selanjutnya yaitu mengkonfigurasi kode semenarik mungkin untuk tampilan login, dan juga register yang ada pada main/templates.
- Langkah selanjutnya yaitu membuat card_info.html dan juga card_product.html pada main/templates untuk mengubah tampilan yang muncul pada main.html yang berkaitan dengan product.
- Langkah selanjutnya yaitu, menambahkan image, pada folder image yang ada pada static untuk menampilkan gambar ketika belum ada product yang ditambahkan oleh user.
- Langkah terakhir yaitu, agar fitur-fitur pada aplikasi menjadi responsive, kita menambahkan tombol-tombol pada navbar contohnya yaitu adanya tombol hamburger jika dilihat pada mobile, lalu ada tombol pada navbar yang muncul jika dilihat pada dengan versi desktop. Untuk menambahkan tombol hamburger, kita melakukannya dengan cara menambahkan elemen <button> untuk tombol hamburger yang diisi tiga elemen <span> sebagai garis-garisnya, lalu menu navigasi menggunakan elemen <ul> yang berisi beberapa <li> sebagai link navigasi.

TUGAS 6
1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web
- Interaktivitas: Menambah elemen interaktif dan dinamis di halaman.
- Manipulasi DOM: Memungkinkan perubahan konten dan gaya secara real-time tanpa reload.
- Validasi Form: Memvalidasi data di sisi klien untuk mengurangi beban server.
- AJAX: Mengambil data dari server tanpa memuat ulang halaman.
- Single Page Application (SPA): Membangun aplikasi yang sepenuhnya berjalan di sisi klien.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi Penggunaan await dengan fetch()
- Menunggu Hasil: await menunggu promise dari fetch() selesai sebelum melanjutkan, memastikan data tersedia.
- Tanpa await: Kode akan terus berjalan dan mungkin mencoba mengakses data yang belum diambil, menyebabkan kesalahan atau hasil yang tidak diinginkan.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Penggunaan Decorator csrf_exempt pada View untuk AJAX POST
- CSRF Token: Django memerlukan CSRF token untuk melindungi dari serangan CSRF pada permintaan POST.
- csrf_exempt: Menghindari pemeriksaan token pada view tertentu untuk mempermudah pengiriman AJAX, tetapi harus digunakan dengan hati-hati untuk menjaga keamanan aplikasi.

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data input pengguna di backend penting karena:
- Keamanan: Pengguna bisa memanipulasi validasi frontend. Backend memastikan data yang diterima aman.
- Integritas Data: Hanya backend yang dapat menjamin bahwa data yang masuk ke database valid.
- Konsistensi: Backend menjaga validasi untuk semua akses, termasuk API.
- Audit dan Logging: Pembersihan di backend memungkinkan pencatatan data untuk analisis dan audit.
Secara keseluruhan, meskipun validasi frontend membantu pengalaman pengguna, backend tetap perlu melakukan pembersihan untuk keamanan dan integritas aplikasi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Agar dapat menerima ajax pertama-tama harus menambahkan fungsi baru pada views.py 
- Lalu untuk mengaktifkannya, kita harus melakukan import di urls.py seperti biasanya ketika untuk menghubungkan sebuah fungsi
- Untuk menggunakan fetch() API ke data JSON secara asynchronus, kita harus memasukkan fungsi async di dalam script
- Lalu untuk me-refresh data secara asinkronus, kita harus menambahkan fungsi async lagi pada main.html, secara khususnya pada blok script.
- Setelah itu untuk menampilkan modal (Tailwind) pada aplikasi, kita juga harus menambahkan kode yang berupa konfigurasi modal, mulai dari header, body, hingga footer.
- Lalu agar modal benar-benar berfungsi kita harus menambahkan beberapa fungsi-fungsi javascript yang berupa showModal untuk memunculkan dan, hideModal untuk menghilangkan.
- Setelah itu kita sedikit perubahan pada button untuk menampilkan tombol baru yang sudah terkonfigurasi AJAX yang sudah bisa menambahkan product secara asinkronus tanpa harus melakukan refresh lagi pada page setelah menambahkan product baru.
- Agar bisa menggunakan modal dengan form yang telah kita buat sebelumnya, kita harus menambahkan fungsi javascript baru, yang berfungsi untuk menambahkan data mood.
- 