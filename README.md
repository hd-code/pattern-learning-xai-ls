# Pattern Learning with Explainable AI

This project implements an application, that learns string patterns. It uses an algorithm introduced by Lange and Wiehagen.

This project is part of the master module "Lernende Systeme" at the FH Erfurt.

## Installation

**Python 3.9** or later is required. Find out more at <https://www.python.org>.

This project uses `pipenv` to manage its dependencies. It can be installed by using `pip` which ships with python. To do that, run:

```sh
python3 -m pip install pipenv
```

To install all dependencies for this project, run the following command in this projects directory:

```sh
pipenv install
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


