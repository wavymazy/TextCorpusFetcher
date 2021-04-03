# TextCorpusFetcher

Project to automate the fetching of text data for language modeling tasks. Currently working on Wikipedia as a source.
We can automate the text extraction, by looking at an article (with a theme) -> extracting text -> iterating on child articles referenced on the page.

## Getting Started

Instructions to run the project locally on your machine.

### Prerequisites

As prerequisite you need to have python3.

### Installing requirements

In order to install the requirements you can follow the steps below. First create a virtual environement and give it a name:

```
python3 -m venv envname
source envname/bin/activate
```

Upgrade pip and Install the requirements:

```
pip install -U pip
pip install -r requirements.txt
```

### Running

To run the fetcher (for now) simply :

```
python main.py
```

Parameters (such as theme or category of article you are looking for) are currently variables to be modified in the main.py script (will make them part of the CLI command in the future).

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details

## Contact

Mehdi - mazeismyname@gmail.com