import streamlit as st
import re
from collections import defaultdict

# --- Core Logic ---
class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)
        self.documents = {}

    def _preprocess(self, text):
        return re.findall(r'\w+', text.lower())

    def add_document(self, doc_id, text):
        self.documents[doc_id] = text
        tokens = self._preprocess(text)
        for token in tokens:
            self.index[token].add(doc_id)

    def search(self, query):
        query_tokens = self._preprocess(query)
        if not query_tokens:
            return []
        results = None
        for token in query_tokens:
            doc_ids = self.index.get(token, set())
            if results is None:
                results = doc_ids
            else:
                results = results.intersection(doc_ids)
        return list(results) if results else []

# --- Streamlit UI ---
st.set_page_config(page_title="Inverted Index App", layout="wide")

st.title("🔍 Inverted Index Engine")
st.write("Bangun corpus dan cari dokumen secara real-time.")

# Inisialisasi index di session state agar tidak hilang saat rerun
if 'my_index' not in st.session_state:
    st.session_state.my_index = InvertedIndex()
    # Contoh data awal
    initial_data = [
        "Belajar Python untuk data science.",
        "Inverted index adalah dasar search engine.",
        "Streamlit memudahkan pembuatan aplikasi web."
    ]
    for i, txt in enumerate(initial_data):
        st.session_state.my_index.add_document(i + 1, txt)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("➕ Tambah Dokumen")
    new_doc = st.text_area("Masukkan teks dokumen baru:", placeholder="Ketik sesuatu di sini...")
    if st.button("Simpan ke Corpus"):
        if new_doc:
            new_id = len(st.session_state.my_index.documents) + 1
            st.session_state.my_index.add_document(new_id, new_doc)
            st.success(f"Dokumen #{new_id} berhasil ditambahkan!")
        else:
            st.warning("Teks tidak boleh kosong.")

with col2:
    st.subheader("🔎 Pencarian")
    query = st.text_input("Masukkan kata kunci:", placeholder="Contoh: Python")
    
    if query:
        results = st.session_state.my_index.search(query)
        if results:
            st.write(f"Ditemukan **{len(results)}** dokumen:")
            for doc_id in results:
                with st.expander(f"Dokumen #{doc_id}"):
                    st.write(st.session_state.my_index.documents[doc_id])
        else:
            st.info("Tidak ada dokumen yang cocok.")

st.divider()
st.subheader("📊 Isi Corpus Saat Ini")
st.json(st.session_state.my_index.documents)