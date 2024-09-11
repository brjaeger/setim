Pertanyaan
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
5. Mengapa model pada Django disebut sebagai ORM?

Jawaban
<!-- 1. Membuat Main : Saya mulai dengan membuat aplikasi dengan nama main dengan menjalankan sintaks di cmd "python manage.py startapp main"

- Membuat Model: mendefinisikan model produk di models.py, saya ,mendeklarasikan atribut yang dibutuhkan seperti name, price, dan description.

- Membuat Views: Di views.py, saya membuat fungsi product_list yang mengambil produk dari model dan mengirimkan data tersebut ke template melalui context.

- Menghubungkan URL: Pada urls.py, saya menambahkan routing agar request URL diarahkan ke product_list yang ada di views.py. -->

<!-- - Membuat Template: Saya membuat file HTML di folder templates/main (karena kalo saya buatnya di folder templates aja nanti error saya juga kurang tau kenapa). Menggunakan syntax Django Template Language (DTL) untuk looping data produk dan menampilkan detailnya. -->

2. "Client Request -> Django URLConf (urls.py) -> View (views.py) -> Model (models.py) -> Template (HTML) -> Response

- **urls.py**: Menerima request dan memetakan ke view yang sesuai.
- **views.py**: Mengambil data dari model dan mengembalikan response dengan template HTML.
- **models.py**: Mendefinisikan struktur data yang disimpan di database.
- **Template HTML**: Menampilkan data yang diambil dari view.

3.  Git adalah sistem kontrol versi yang digunakan untuk melacak perubahan dalam kode sumber selama pengembangan perangkat lunak. Git memungkinkan pengembang untuk bekerja secara kolaboratif, mengelola versi kode, dan mengembalikan perubahan jika diperlukan.

4. Django adalah framework yang lengkap dan memiliki banyak fitur bawaan yang memudahkan pengembangan aplikasi web. Django juga memiliki dokumentasi yang baik dan komunitas yang besar, sehingga cocok untuk pemula.

5. Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa perlu menulis query SQL secara langsung. ORM memetakan tabel database ke kelas Python dan kolom tabel ke atribut kelas.

