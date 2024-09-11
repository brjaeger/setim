Pertanyaan
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

