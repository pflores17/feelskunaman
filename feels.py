
from argparse import Namespace
from typing import Type
from parsers.feelsparser import FeelsParser

import tasks.analyze as BigBrain

def main(args: Namespace):
    print('\nFeels Kuna Man - a tool to check on the homie\'s feels using the SpotifyAPI\n')
    BigBrain.execute(args)

if __name__ == '__main__':
    from parsers.feelsparser import FeelsParser
    import sys

    args = FeelsParser().parse_args(sys.argv[1:])
    main(args)