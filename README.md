This is a simple Python project demonstrating the use of Continuous Integration (CI) with GitHub Actions. It includes a basic calculator script along with associated tests.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Continuous Integration (CI) is a practice where code changes are automatically tested and verified whenever they are pushed to the repository. This helps ensure code quality and detect issues early in the development process.

This project showcases how to set up CI for a Python project using GitHub Actions. It includes a simple Python script (`calculator.py`) defining a basic calculator, along with corresponding test cases (`test_calculator.py`). The GitHub Actions workflow (`ci.yml`) is configured to run the tests automatically whenever changes are pushed to the repository.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/sample-ci-project.git
    cd sample-ci-project
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run tests**:

    ```bash
    pytest
    ```

2. **Make changes**:

    You can make changes to the `src/calculator.py` file to modify the calculator functionality or add more test cases in `tests/test_calculator.py`.

3. **Push changes to GitHub**:

    ```bash
    git add .
    git commit -m "Add feature / Fix bug"
    git push origin main
    ```

4. **Check CI status on GitHub**:

    Visit your GitHub repository and navigate to the "Actions" tab to see the workflow running. You should see the tests being executed automatically. If all tests pass, the workflow will be marked as successful.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to open a pull request with your changes or submit an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
