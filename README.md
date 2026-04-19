# Glauco

Complementary web app for the Riasco-Goyes 2025 preprint.

## Getting Started

To set up your local development environment, please use a fresh virtual environment with:

    conda env create --name glauco --file=environment-dev.yml

Then activate the environment with:

    conda activate glauco

To update this environment with your production dependencies, please run:

    conda env update --file=environment.yml

You can now access the CLI with `python -m glauco`.

If you want to deploy this project as a docker container, please ensure that [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/) are installed, then run

    docker-compose up

this will build the entire project with all dependencies inside a docker container. You may use the command line interface of the application now, e.g. by editing the `command` tag in the [`docker-compose.yml`](./docker-compose.yml).

### Testing

> [!WARNING]
>
> Not working right now. See [this GitHub issue](https://github.com/at-gmbh/at-python-template/issues/106).

We use `pytest` as the test framework. To run tests, use:


    pytest tests


To run tests with coverage reporting:


    pytest tests --cov=src --cov-report=html --cov-report=term


After running the tests, open the `htmlcov` directory in your browser to inspect coverage visually.


### Notebooks

You can use your module code (`src/`) in Jupyter notebooks (`notebooks/`) without running into import errors.


Make sure your conda environment is activated, then launch:

    jupyter notebook

or

    jupyter lab



To make your virtual environment available as a Jupyter kernel, run:

    conda install ipykernel
    python -m ipykernel install --user --name="glauco"

> 💡 This ensures that your notebook environment uses the same dependencies and paths as your project.

Note: We mainly use notebooks for experimentation, visualizations, and reporting. Any reusable logic should live in the `src/` module and be imported into notebooks.

### Distribution Package

To build a distribution package (wheel), run:


    python setup.py sdist bdist_wheel



> 💡 If needed, install wheel via:

    conda install wheel


Build artifacts will be placed in the `dist/` directory.


### Contributions

Before contributing, please set up the pre-commit hooks to ensure consistent formatting and linting.


    pip install -U pre-commit
    pre-commit install


> This will automatically run checks like code formatting, import sorting, and linting before each commit.

To uninstall the hooks:


    pre-commit uninstall


## Contact

Luis M. Torres-Villegas (lmtorresv@eafit.edu.co)

## License

© Luis M. Torres-Villegas
