# FastAPI Clear Architecture Project

This is a FastAPI project that follows a clear and organized architecture. It is designed to demonstrate best practices for structuring a FastAPI application. It is also designed to demonstrate how to write tests for a FastAPI application. It emphasizes a clean and organized architecture that separates concerns and encourages maintainability and testability. This README provides an overview of the project's structure, how to run it, and how to write tests for it.

## Table of Contents

- [Project Structure](#project-structure)
- [Running the Application](#running-the-application)
- [Running the Tests](#running-the-tests)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project is organized into the following directories:

- `app`: This directory contains all the source code of your application.
- `app/domain`: This directory contains all the domain models of your application.
- `app/domain/repositories`: This directory contains all the repositories of your application.
- `app/domain/entities`: This directory contains all the entities of your application.
- `app/domain/usecases`: This directory contains all the use cases of your application.
- `app/data`: This directory contains all the data access objects of your application.
- `app/presentation`: This directory contains all the presentation logic of your application.
- `app/presentation/routers`: This directory contains all the routers of your application.
- `app/data/repositories`: This directory contains all the repositories of your application.
- `app/data/data_sources`: This directory contains all the data sources of your application.
- `app/data/models`: This directory contains all the models of your application.
- `tests`: This directory contains all the tests of your application.

## Running the Application

To run the application, you need to have Python 3.8 or higher installed on your machine. You also need to install the dependencies in the `requirements.txt` file. To do that, run the following command:

```bash
pip install -r requirements.txt
```

```bash

uvicorn app.main:app --reload
```

## Running the Tests

To run the tests, you need to install the dependencies in the `requirements.txt` file. To do that, run the following command:

```bash

pip install -r requirements.txt
```

Then, run the following command:

```bash
unittest discover -s tests -p '*_test.py' -v
```

## Contributing

If you want to contribute to this project, clone the repository and just start making pull requests. If you find any issue, please open an issue. If you have any questions, feel free to ask. If you want to contact me, you can reach me at `duresafeyisa2022@gmail.com`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

[FastAPI](https://fastapi.tiangolo.com/)
