import os
from huggingface_hub import HfApi

api = HfApi(token=os.environ["HF_TOKEN"])

spaces = [
    "prashant-gulati/kmeans_clustering",
    "prashant-gulati/nnfs",
]

for space in spaces:
    try:
        api.restart_space(space)
        print(f"✓ {space}")
    except Exception as e:
        print(f"✗ {space}: {e}")
