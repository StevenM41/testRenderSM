# testRender
Essai déploiement

### Installation

```bash
 python3.13 -m venv .venv
 source .venv/bin/activate
 pip install -r requirements.txt
```

### Execution
```bash
  fastapi dev main.py
```

## DOCKER
### Build
```bash
docker build -tag render
```

```bash
  docker run -it --rm -p 8000:8000 -name renderinstance render
```