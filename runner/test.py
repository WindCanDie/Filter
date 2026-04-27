import gzip
import pickle

def load_gzip_pickle(filepath):
    with gzip.open(filepath, 'rb') as f:
        obj = pickle.load(f)
    return obj

# 示例
# data = load_gzip_pickle('release_data/mmcif_bioassembly/3ny2.pkl.gz')
data = load_gzip_pickle('release_data/mmcif_bioassembly/8gop.pkl.gz')
for key, value in data.items():
    print(f"{key}: {value}")
