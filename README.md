# Morse code translator
## Goal
Based on modification codebase and adding classes and functions you should implement a morse code translator.

**You can read more [here](https://en.wikipedia.org/wiki/Morse_code).**

## What you should implement

* Stage 1: Write code for `islatin` and `ismorse` to fix tests.
* Stage 2: Create functions and test for them to translate sentences (or for one characters).
* Stage 3: Implement validator for latin and morse sentences. 
* Stage 4: Use your imagination (e.g. add some encryption, extend characters).

## Files
* `translator.py` Main code file, this is entry point of your program.
* `consts.py` Here you can get mapping for morse code characters.
* `tests/test_translator.py` Initial tests for program.

## Implementation
You should start by read what was implemented already. Translator should detect
which type of characters where provided. Try implement `islatin` and `ismorse` functions
to successful detect that. Then start thinking about translating functions and what cases
you should implement. 

Program execution is correct when you see translated text in terminal.

## How to run
1. Install [python](https://www.python.org/)
2. Install [pytest](https://docs.pytest.org/) or `pip install -r requirements.txt`
3. Run code: `python translator.py 'SENTENCE'` or `python translator.py '... . -. - . -. -.-. .'` 
4. Run tests: `python -m pytest`
