# grimorios
Project for FastAPI application on AWS Lambda using Terraform. 

[![codecov](https://codecov.io/gh/esgaelramos/grimorios/graph/badge.svg?token=DTS5NKYAE6)](https://codecov.io/gh/esgaelramos/grimorios)

| [Installation](#installation) |
| [Development](#development) |
| [Infrastructure](#infrastructure) |
| [ExtraTools](#extratools) |

For the project, we are going to use the next tools:
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Terraform](https://www.terraform.io/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

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
pip install -r src/requirements-dev.txt
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


## Development

For follow and respect the code style, will be used the nexts tools:

### Linter

Used for check the code style and syntax errors. 
With the [pre-commit](https://pre-commit.com/) and 
[flake8](https://flake8.pycqa.org/en/latest/).

Execute the command for lint the code
```bash
pre-commit run --all-files
```

### Testing

The tests will be used for check the code logic and errors.
With [pytest](https://docs.pytest.org/) create the unit and 
integration features tests.

Execute the command for run the tests
```bash
pytest
```

## Infrastructure

For the infrastructure, we are going to use Terraform.
All the instructions are in the [INFRA.md](infra-lambda/INFRA.md) file.
But, in summary, we use AWS Lambda for host this FastAPI application.
And, for manage the state of the backend, we use an S3 bucket.

## ExtraTools
Tree of the fundamental project
```bash
tree -I "env|.git|.pytest_cache|__pycache__|.terraform" -la
```

### Not Now
- [ ] Add Gateway in Terraform with AWS
- [ ] Configure custom domain with the API Gateway
- [ ] Add Poetry for manage the dependencies
