# Introduction

*PageRank adalah suatu sistem SCORING (antara 1 – 10) yang diciptakan oleh founder Google (Larry Page) untuk memberikan penilaian seberapa tinggi score dari sebuah halaman website. Semakin tinggi score halaman website tersebut, maka artinya semakin bagus KUALITAS halaman website tersebut di mata Google.*

Secara sederhana, sistem scoring dari PageRank dihitung berdasarkan LINK POPULARITY, yaitu semakin banyak link yang mengarah ke sebuah website, maka akan semakin tinggi PR dari website tersebut.[disini](<<http://www.klikseo.com/apa-itu-pagerank-dan-kaitannya-dengan-seo/>>)

## Step 1. Installing

![1559053631506](C:\Users\i-one\AppData\Roaming\Typora\typora-user-images\1559053631506.png)

Dalam tutorial ini semua proses akan dibangun menggunakan bahasa pemograman *Python*. Alasan mengapa *author* menggunakan bahasa pemograman ini karena *Python* merupakan bahasa pemograman yang populer akhir-akhir ini, selain itu *Python* menyediakan banyak *library*yang mudah digunakan dalam membangun suatu sistem. Adapun *library* yang digunakan akan dijelaskan pada setiap stepnya.

Panduan instalasi python dapat teman-teman baca[disini](<https://realpython.com/installing-python/>)

Panduan instalasi library atau package dapat teman-teman [disini](<https://datatofish.com/install-package-python-using-pip/>)

## Step 2. Crawling

### Apa itu *Web Crawler* ?

*Web Crawler* merupakan suatu program atau *Script* otomatis yang relatif simpel, menggunakan sebuah metode tertentu untuk melakukan *scan* atau *crawl* pada halaman internet untuk mendapatkan indek dari data yang dicari. Nama lain dari *Web Crawler* adalah *Web Spider*, *Web Robot*, *Bot*, *Crawl* dan *Automatic Indexer*. Umumnya *Web Crawler* dapat digunakan berkaitan dengan *Search Engine*, yakni mengumpulkan informasi mengenai apa yang ada pada halaman-halaman web publik.

### Bagaimana cara kerja *Web Crawler* ?

Ketika *Web Crawler* suatu *Search Engine* mengunjungi halaman web, *Web Crawler* akan membaca teks , *hyperlink* dan macam-macam tag konten yang digunakan dalam situs misalnya meta tag yang berisi banyak keyword. Data tersebut kemudian akan dimasukkan ke dalam database atau tempat penyimpanan.

### Apa yang akan dilakukan ?

#### Install library yang digunakan

```python
from bs4 import BeautifulSoup
import requests
```

`BeautifulSoup`digunakan untuk dapat mengakses data html dan xml, sedangkan requests digunakan untuk dapat mengakses halaman web.

#### Menentukan halaman web yang akan di *crawl*

Pada artikel ini halaman web yang akan di crawl datanya adalah 

<http://lintasperistiwa.com/>.

#### Menentukan informasi apa yang akan di simpan

Setelah menentukan halaman web yang akan di crawl, selanjutnya berdasarkan informasi yang ada di halaman web diatas, data artikel atau berita yang akan di simpan pada tutorial ini berupa `URL, judul dan isi berita`.

#### Proses Crawling

```
>> Membuat requests pada halaman web yang dituju
```

`req = requests.get('http://lintasperistiwa.com/')`

```
>> Menentukan berita yang akan diambil dari halaman web
```

![1559053721767](C:\Users\i-one\AppData\Roaming\Typora\typora-user-images\1559053721767.png)



Berita yang akan  diambil adalah yang terletak di panel tengah pada list berita terkini, berita ini merupakan berita yang diupload tiap hari.

![1559053809390](C:\Users\i-one\AppData\Roaming\Typora\typora-user-images\1559053809390.png)

Untuk dapat mengakses tag html dari list berita tersebut, dapat dilakukan dengan *inspect element*, yakni dengan cara :

1. klik kanan pada halaman web

2. pilih *inspect*

3. maka akan muncul panel *inspect* di jendela sebelah kanan

   ![1559053848520](C:\Users\i-one\AppData\Roaming\Typora\typora-user-images\1559053848520.png)

Selanjutnya pada panel *inspect*, cari tag html yang berisi link berita terkait pada tag html yang memuat tag <a 

![1559053904235](C:\Users\i-one\AppData\Roaming\Typora\typora-user-images\1559053904235.png)

```
news_links = soup.find_all('a',{'class':'mod-judul-post'}, href=True)e)
```

```
>>Mendapatkan judul dan alamat web dari isi artikel
```

Setelah tag html list berita telah diperoleh, selanjutnya adalah mencari tag html yang memuat judul dan link dari judul tersebut. Hal ini dilakukan agar menelusuri isi dari setiap list berita yang terdapat pada halaman tersebut. Biasanya tag html yang memuat link terdapat attribut `href`.

Sehingga untuk melakukan crawling pada artikel tersebut, diperoleh code seperti berikut :

```
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
 news_linkss = soups.find_all('a',{'class':'vrp-thumb-link'}, href=True)
```

#### Looping hingga melakukan *crawling* pada kedalaman tertentu

#### Full Code

```
import requests
from bs4 import BeautifulSoup

def getLinks(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    news_links = soup.find_all('a',{'class':'mod-judul-post'}, href=True)
    for link in news_links:
        listUrl.append(link['href'])
    n_depth = 3
    swap_depth = 0
    swap_list = 0
    while swap_depth < n_depth :
        listUrl.append("depth")
        next_depth = False
        while next_depth == False:
            if listUrl[swap_list] == "depth" :
                swap_list+=1
                next_depth = True
                break
            
            if listUrl[swap_list].isdigit() :
                swap_list+=1
                break
            
            listUrl.append(str(swap_list))
            
            urls = listUrl[swap_list]
            reqs = requests.get(urls)
            soups = BeautifulSoup(reqs.text, 'html.parser')
            news_linkss = soups.find_all('a',{'class':'vrp-thumb-link'}, href=True)
            for link in news_linkss:
                listUrl.append(link['href'])
            
            swap_list+=1
        swap_depth+=1
        
if __name__== "__main__":
    listUrl = []
    links = getLinks("http://lintasperistiwa.com/")
    print(listUrl)

```

Hasil :

![1559053969639](C:\Users\i-one\AppData\Roaming\Typora\typora-user-images\1559053969639.png)

## Step 2. Graph Processing

### Apa itu graph ?

**Graph atau Graf** adalah kumpulan noktah (simpul) di dalam bidang dua dimensi yang dihubungkan dengan sekumpulan garis (sisi). *Graph* dapat digunakan untuk merepresentasikan objek-objek diskrit dan hubungan antara objek-objek tersebut. Representasi visual dari*graph*adalah dengan menyatakan objek sebagai noktah, bulatan atau titik (Vertex), sedangkan hubungan antara objek dinyatakan dengan garis (Edge).

> G = (V, E)

Dimana :

G = Graph

V = Simpul atau Vertex, atau Node, atau Titik

E = Busur atau Edge, atau arc

V adalah himpunan verteks dan E adalah himpunan sisi yang terdefinisi antara pasangan-pasangan verteks. Sebuah sisi antara verteks x dan y ditulis {x,y}. Suatu graph H = (V1, E1) disebut subgraph dari graph G jika V1 adalah himpunan bagian dari V dan E1 himpunan bagian dari E.

Cara pendefinisian lain untuk graph adalah dengan menggunakan himpunan keterhubungan langsung Vx. Pada setiap verteks x terdefinisi Vx sebagai himpunan dari verteks-verteks yang adjacent dari x. Secara formal:

> Vx = {y | (x,y) -> E}

### Apa manfaat dari graph ?

Tiap-tiap diagram memuat sekumpulan obyek (kotak, titik, dan lain-lain) beserta garis-garis yang menghubungkan obyek-obyek tersebut. Garis bisa berarah ataupun tidak berarah.

- Garis yang berarah biasanya digunakan untuk menyatakan hubungan yang mementingkan urutan antar objek-objek. Urut-urutan objek akan mempunyai arti yang lain jika arah garis diubah. Sebagai contoh adalah garis komando yang menghubungkan titik-titik struktur sebuah organisasi.
- Sebaliknya, garis yang tidak berarah digunakan untuk menyatakan hubungan antar objek-objek yang tidak mementingkan urutan. Sebagai contoh adalah garis untuk menyatakan jarak hubung 2 kota pada Gambar 2. Jarak dari kota A ke kota B sejauh 200 km akan sama dengan jarak dari kota B ke kota A. Apabila jarak 2 tempat tidak sama jika dibalik (misalnya karena harus melalui jalan memutar), maka garis yang digunakan haruslah garis yang berarah.

### Apa yang akan dilakukan ?

#### Install library yang digunakan

```
import matplotlib.pyplot as plt
import networkx as nx
```

`matplotlib` digunakan untuk dapat memvisualisasikan *graph*, sedangkan `networkx` digunakan untuk dapat mengakses atau membangun *graph*.

#### Menentukan node dan edge

**Node** merupakan kumpulan dari *link* yang telah diperoleh dari hasil crawling, sedangkan **Edge**merupakan hubungan antar *link* atau *link* yang saling berkaitan. Oleh karena itu, saat melakukan crawling alangkah lebih baiknya jika menginisialisasi **Node** dan **Edge** secara bersamaan.

```
 urls = listUrl[swap_list]
            reqs = requests.get(urls)
            soups = BeautifulSoup(reqs.text, 'html.parser')
            news_linkss = soups.find_all('a',{'class':'vrp-thumb-link'}, href=True)
            for link in news_linkss:
                listUrl.append(link['href'])
                
                if link['href'] not in node :
                    node.append(link['href'])
                value = (str(node.index(urls)),str(node.index(link['href'])))
                edge.append(value)
```

Saat mengunjungi sebuah artikel, *link* dari artikel tersebut akan di tambahkan ke dalam list node `node.append(link['href'])`, setelah itu *link* dari artikel `(str(node.index(urls))` dan *link*terkait `str(node.index(link['href']))` di inisialisasi dan ditambakan pada list edge

```
 value = (str(node.index(urls)),str(node.index(link['href'])))
 edge.append(value)
```

Sehingga keseluruhan code untuk proses *crawling* dan inisialisasi **Node** dan **Edge** 

full code :

```
import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt

def getLinks(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    news_links = soup.find_all('a',{'class':'mod-judul-post'}, href=True)
    for link in news_links:
        listUrl.append(link['href'])
        node.append(link['href'])
        
    n_depth = 3
    swap_depth = 0
    swap_list = 0
    while swap_depth < n_depth :
        listUrl.append("depth")
        next_depth = False
        while next_depth == False:
            if listUrl[swap_list] == "depth" :
                swap_list+=1
                next_depth = True
                swap_depth+=1
                break
            try :
                urls = listUrl[swap_list]
                reqs = requests.get(urls)
                soups = BeautifulSoup(reqs.text, 'html.parser')
                news_linkss = soups.find_all('a',{'class':'vrp-thumb-link'}, href=True)
                for link in news_linkss:
                    listUrl.append(link['href'])
                
                    if link['href'] not in node :
                        node.append(link['href'])
                    value = (str(node.index(urls)),str(node.index(link['href'])))
                    edge.append(value)
                    
            except :
                pass
            swap_list+=1
        swap_depth+=1
        
if __name__== "__main__":
    listUrl = []
    node = []
    edge = []
 
    
    links = getLinks("http://lintasperistiwa.com/")
    #print(listUrl)
    G=nx.DiGraph()
    pages = []
    for i in range(0,len(node)):
        pages.append(str(i))
        
    G.add_nodes_from(pages)
    G.add_edges_from(edge)
    
    print(edge)
    print(type(edge))
    #print(type(edge[0]))
    #membuat graf
    image = nx.draw_circular(G,node_color='blue', with_labels = True)
    plt.savefig("grap.png", format="PNG")
    #mancari nilai pagerank
    PR = nx.pagerank(G)
    print(PR)
    value = max(PR, key=PR.get)
    print("node : " + max(PR,key=PR.get))
    print("link : " + node[int(value)])
    nx.draw(G)
    plt.show()
    print(node)
    

 

```

Hasil :

![1559054085167](C:\Users\i-one\AppData\Roaming\Typora\typora-user-images\1559054085167.png)

![1559054015527](C:\Users\i-one\AppData\Roaming\Typora\typora-user-images\1559054015527.png)

