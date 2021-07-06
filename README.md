# Pattern Learning with Explainable AI

This project implements an application, that learns string patterns. It uses an algorithm introduced by Lange and Wiehagen.

This project is part of the master module "Lernende Systeme" at the FH Erfurt.

## Requirements

- Python 3.9 *or later*. See: <https://www.python.org>
- `pipenv` – a package manager that creates isolated environments  
  install by running: `python3 -m pip install pipenv`

### Installation

From the project's directory run:

```sh
pipenv install --dev
```

## Usage

This project is implemented as a desktop app. Start this projects application by running:

```sh
pipenv run python src
```

## Testing

In the folder `test/` are a bunch files, that test the functionality in the `src/` directory. To run all automatic tests simply run:

```sh
pipenv run python test
```

By default the test files will only print messages for failed tests to the console. To also print successful tests to the console simply add either `--verbose` or `-v` to the above command like this:

```sh
pipenv run python test --verbose
```

It is also possible to run just a single test file. Simply type:

```sh
pipenv run python <path-to-testfile>

# or with verbose flag:
pipenv run python <path-to-testfile> --verbose
```

## Building Standalone Executable

Executables can only be build for the operating system the machine currently has. So, `.exe` can only be compiled on a Windows machine, `.app` only on a mac and so on.

Executables are compiled with `PyInstaller`. Run the following command to build the app:

```sh
pipenv run pyinstaller -n pattern-learning-xai -w -F --clean src/__main__.py
```

The executable will be put into the `dist/` directory.
