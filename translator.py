from argparse import ArgumentParser


def islatin(sentence):
    return False


def ismorse(sentence):
    return False


def translator(sentence):
    if islatin(sentence):
        pass  # Check if is valid and run translation to morse code
    elif ismorse(sentence):
        pass  # Check if is valid and run translation to morse code

    raise ValueError(f'Sentence "{sentence}" is neither latin or morse.')


if __name__ == '__main__':
    parser = ArgumentParser(description='Translate morse code in both ways')
    parser.add_argument('sentence')
    args = parser.parse_args()

    translator(args.sentence)
