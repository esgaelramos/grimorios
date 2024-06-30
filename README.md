# grimorios
Project for FastAPI application on AWS Lambda using Terraform. 

| [Installation](#installation)
| [ExtraTools](#extratools) |

### In Local Environment

Create a virtual environment
```bash
python -m venv env
```

Activate the virtual environment
```bash
source env/bin/activate
```

Install the requirements
```bash
pip install -r src/requirements.txt
```

Run the application
```bash
python src/app.py
```

### In Docker (Compose) Environment

Build and Up the docker-compose (inside src folder)
```bash
docker-compose up --build
```

> __Note:__ We USE two Dockerfiles, one for production environment 
> and another for the local environment (Dockerfile.Local).
> The docker-compose.yml file uses the Dockerfile.Local file 
> to build the image.

## ExtraTools
Tree of the fundamental project
```bash
tree -I "env|.git|.pytest_cache|__pycache__|.terraform" -la
```
