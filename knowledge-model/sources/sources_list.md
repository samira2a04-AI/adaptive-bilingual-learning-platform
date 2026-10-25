# Sources & Multilingual Embedding Models (Week 6 Draft)

## 1. MLCC (Google Machine Learning Crash Course) Sources

The following MLCC modules form the foundational source for the pilot. Each module is mapped to relevant concepts in the concept list.

| Module ID | Module Title | Relevant Concepts | Language |
|---|---|---|---|
| MLCC-01 | Foundations | M01-M04, P01-P04, D01-D04 | EN |
| MLCC-02 | Regression | M19-M20, ML06-ML09 | EN |
| MLCC-03 | Classification | M19-M20, ML06-ML09 | EN |
| MLCC-04 | Clustering | D11-D12, ML12-ML13 | EN |
| MLCC-05 | Neural Networks | ML01-ML05, P13-P15 | EN |
| MLCC-06 | Decision Forests | ML01-ML05, ML10-ML11 | EN |
| MLCC-07 | Evaluating Models | ML03-ML09, NFR-02, NFR-03 | EN |
| MLCC-08 | Recommendation Systems | ML15, P09-P10, M09 | EN |
| MLCC-10 | Python Introduction | P01-P04, P19-P20 | EN |
| MLCC-11 | Advanced Python | P15-P18, P20 | EN |

## 2. Multilingual Embedding Models Shortlist

For bilingual (Arabic/English) concept matching and question translation. All models support 512+ dimensional vectors and are compatible with sentence-transformers.

| Model Name | Provider | Languages | Dims | Key Strength | Licensing |
|---|---|---|---|---|---|
| `all-MiniLM-L6-v2` | Hugging Face | 100+ including AR/EN | 384 | Fast, lightweight, good baseline | MIT |
| `paraphrase-multilingual-MiniLM-L12-v2` | Hugging Face | 100+ including AR/EN | 384 | Higher quality than base MiniLM | MIT |
| `bge-m3` | BGEM3 | 100+ including AR/EN | 768 | State-of-the-art multilingual retrieval | Apache 2.0 |
| `all-MPNet-base-v2` | Hugging Face | 100+ including AR/EN | 768 | Strong performance, slower than MiniLM | MIT |
| `nomic-embed-text` | NVIDIA | 100+ including AR/EN | 768 | Optimized for retrieval tasks | Apache 2.0 |

**Recommended:** `paraphrase-multilingual-MiniLM-L12-v2` as primary (balanced quality/speed), `bge-m3` as secondary (highest quality for evaluation).

## 3. Arabic Language Resources

| Resource Name | Type | Description | Link |
|---|---|---|---|
| AraVec | Word Embeddings | Pre-trained Arabic word vectors | https://github.com/aaraf/AraVec |
| AraBERT | Language Model | Arabic BERT model, multilingual capable | https://github/aub-mind/AraBERT |
| KhBERT | Language Model | Kuwait Arabic dialect BERT | https://github.com/kbp/KhBERT |
| Arabic Question Bank | Educational | Translated MCQ items for math/programming concepts | Pilot-generated |

## 4. Public Datasets for Offline Evaluation (per NFR-04, ML-01, ML-02)

| Dataset | Domain | Size | Link |
|---|---|---|---|
| ASSISTments 2009-2010 | Education (Math) | ~1M interactions | https://www.assistments.org/ |
| EdNet-KT1 | Education (All subjects) | ~4M interactions | https://ednet-data.org/ |
| Junyi-KT | Education (China) | ~500K interactions | https://junyi.ac/ |

## 5. Attribution & Licensing Notes

- MLCC content is owned by Google Inc. and used under educational fair-use for pilot demonstration.
- Hugging Face sentence-transformer models are MIT-licensed; safe for commercial and non-commercial use.
- ASSISTments and EdNet are open educational datasets; verify terms of use before exporting models or metrics.
- Any Arabic resource attribution must follow the original provider's citation requirements.
- Model manifests (per NFR-09) must include source hash, kg_version, and git commit for roll-backability.