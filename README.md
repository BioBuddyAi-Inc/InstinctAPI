# InstinctAPI

**InstinctAPI** is a Python-based API for snake species recognition developed by BioBuddyAi-Inc. Built on deep learning models, it provides a simple interface to identify snakes from image input.

---

## Features

- **Deep learning powered**: Employs a CNN model (e.g., stored in `snake_model.h5` and `snake_model.pth`) to classify snake species.
- **Python-first API**: Everything is accessible via `api.py`.
- **Test suite included**: Contains basic tests in `test_api.py`.
- **Shell script & containerization**: `build.sh` likely helps with setup or container build processes.
- **AGPL-3.0 licensed**: Free to use and modify under AGPL-3.0 terms. :contentReference[oaicite:0]{index=0}

---

## Contents
```yaml
.
├── api.py # Main API implementation
├── cnn_snake.py # CNN model architecture or inference logic
├── snake_model.h5 # Pretrained model weights (H5 format)
├── snake_model.pth # Pretrained model weights (PyTorch format)
├── snake_classes.txt # Mapping of class indices to snake species names
├── test_api.py # Test suite for the API
├── requirements.txt # Python dependencies
├── build.sh # Build/bootstrap script
├── render.yaml # (Possibly CI/container orchestration config)
└── LICENSE # AGPL-3.0 license text

```


---

## Usage

1. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```
Run the API server:

```bash
python api.py
```
Test the API:

```bash
python test_api.py
```
Build or containerize (if applicable):

```bash
./build.sh
```
