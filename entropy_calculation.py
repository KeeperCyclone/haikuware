"""
module name: haikuware_entropy
purpose: calculate the entropy of the generated passphrase
"""


import math
from pprint import pprint


def calculate_single_entropy(r: int) -> float:
    return math.log(r, 2)


def get_entropy_info(wordlists: dict) -> tuple[dict, float]:
    entropies = {  # in bits
            label: calculate_single_entropy(len(wordlists[label]))
            for label
            in wordlists.keys()
        }

    # with 6 nouns, 3 verbs, and 1 adverb:
    total_entropy = (
            (6 * entropies['nouns'])
            + (3 * entropies['verbs'])
            + (entropies['adverbs'])
        )
    return entropies, total_entropy


def report_entropy(wordlists: dict) -> None:
    entropies, total_entropy = get_entropy_info(wordlists)
    print("Individual word entropies:")
    pprint(entropies)
    print("-------------")
    print(f"Total entropy: {total_entropy}")



