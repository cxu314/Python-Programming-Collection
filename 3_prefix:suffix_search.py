class WordDic:
    """A reusable dictionary of all matching words in a given list of words
       for a specific prefix or suffix.

    Attributes:
        words: A given list of words.
        p_map: A dictionary of all matching words for a specific prefix.
        s_map: A dictionary of all matching words for a specific suffix.

        :type words: List[str]
              p_map: Dict
              s_map: Dict
    """

    def __init__(self, words):
        """
        Inits WordDic with words, p_map and s_map.
        """
        self.words = words
        self.p_map = {}
        self.s_map = {}

        for idx, word in enumerate(words):
            for x in range(1, len(word) + 1):
                prefix = word[:x]
                suffix = word[x-1:]

                try:
                    self.p_map[prefix].append(idx)
                except KeyError:
                    self.p_map[prefix] = [idx]

                try:
                    self.s_map[suffix].append(idx)
                except KeyError:
                    self.s_map[suffix] = [idx]

    def get_p_words(self, prefix):
        """
        For a given prefix, return a list of all matching words.
        :type prefix: str
        :rtype: List[str]
        """
        idxs = self.p_map.get(prefix, -1)

        if idxs == -1:
            return None
        else:
            return [self.words[i] for i in idxs]

    def get_s_words(self, suffix):
        """
        For a given suffix, return a list of all matching words.
        :type suffix: str
        :rtype: List[str]
        """
        idxs = self.s_map.get(suffix, -1)

        if idxs == -1:
            return None
        else:
            return [self.words[i] for i in idxs]


def control(args, words):
    """Control for Constraints.
    Only one option at the time should be supported.
    Prefix or suffix must contain at least one character.
    Prefix or suffix only include letters from English ASCII character set
    in the range from DEC 65 to DEC 122.
    """
    if len(args.fix) == 0:
        return parser.print_help()

    letter_set = string.ascii_uppercase + string.ascii_lowercase
    if not set(args.fix).issubset(letter_set):
        return parser.print_help()

    if args.p and not args.s:
        return WordDic(words).get_p_words(args.fix)
    elif args.s and not args.p:
        return WordDic(words).get_s_words(args.fix)
    else:
        return parser.print_help()


if __name__ == "__main__":
    import argparse
    import sys
    import string

    # parsing
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''
        This is a prefix/suffix search program.
        Only one option at the time should be supported:
        p for prefix or s for suffix
        ''')
    parser.add_argument('fix', type=str, help='''
        prefix or suffix:
        It must contain at least one character.
        It can only include letters from English ASCII character set
        in the range from DEC 65 to DEC 122.
        ''')
    parser.add_argument('-p', '--prefix', action='store_true',
                        dest='p', default=False, help='prefix search')
    parser.add_argument('-s', '--suffix', action='store_true',
                        dest='s', default=False, help='suffix search')
    args = parser.parse_args(sys.argv[1:])
    args = parser.parse_args()

    words = [w.rstrip() for w in sys.stdin.readlines()]

    print(control(args, words))
