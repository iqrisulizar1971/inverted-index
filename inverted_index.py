import re
from collections import defaultdict

class InvertedIndex:
    def __init__(self):
        # Dictionary dengan default value list: { 'kata': [doc_id1, doc_id2] }
        self.index = defaultdict(set)
        self.documents = {}

    def _preprocess(self, text):
        """Membersihkan teks dan melakukan tokenisasi sederhana."""
        # Kecilkan huruf dan ambil hanya karakter alfanumerik
        tokens = re.findall(r'\w+', text.lower())
        return tokens

    def add_document(self, doc_id, text):
        """Menambahkan dokumen ke dalam corpus dan mengindeks kata-katanya."""
        self.documents[doc_id] = text
        tokens = self._preprocess(text)
        
        for token in tokens:
            self.index[token].add(doc_id)

    def search(self, query):
        """Mencari dokumen yang mengandung kata kunci dalam query."""
        query_tokens = self._preprocess(query)
        if not query_tokens:
            return []

        # Mengambil hasil untuk setiap kata kunci (Intersection/Irisan)
        results = None
        for token in query_tokens:
            doc_ids = self.index.get(token, set())
            if results is None:
                results = doc_ids
            else:
                results = results.intersection(doc_ids)
        
        return list(results) if results else []

# --- Contoh Penggunaan ---

corpus = {
    1: "Belajar Python untuk analisis data sangat menyenangkan.",
    2: "Python adalah bahasa pemrograman yang populer untuk AI.",
    3: "Data science membutuhkan pemahaman statistik dan Python.",
    4: "Kopi adalah teman terbaik saat menulis kode program."
}

# Inisialisasi index
my_index = InvertedIndex()

# Masukkan dataset ke dalam index
for doc_id, text in corpus.items():
    my_index.add_document(doc_id, text)

# Uji Coba Pencarian
keyword = "Python Data"
found_docs = my_index.search(keyword)

print(f"Hasil pencarian untuk '{keyword}':")
for doc_id in found_docs:
    print(f"- [Doc {doc_id}]: {corpus[doc_id]}")