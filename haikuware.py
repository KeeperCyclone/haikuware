"""
module name: haikuware
purpose: Implementation of Haikuware concept, which produces a 100-bit entropy passphrase in a unique 3+4+3-word structural form.
"""


import secrets
import entropy_calculation
import importlib.resources


haikuware_version = "1.1"


def get_data_resources() -> dict:
    datapkg = importlib.resources.files("data")
    resources = {}
    for rsrc in ("nouns", "verbs", "adverbs"):
        resources[rsrc] = datapkg / f"{rsrc}.txt"
    return resources


def resource_to_list(resource) -> list[str]:
    content = resource.read_text()
    lines = content.splitlines(keepends=False)
    return lines


def get_wordlists() -> dict[str, list]:
    resources = get_data_resources()
    wordlists = {
            category: resource_to_list(resource)
            for category, resource
            in resources.items()
        }
    return wordlists


SVO_TEMPLATE = "{s} {v} {o}"
SVOADV_TEMPLATE = "{s} {v} {o} {adv}"


def choose_noun(wordlists: dict) -> str:
    l = wordlists['nouns']
    return secrets.choice(l)


def choose_verb(wordlists: dict) -> str:
    l = wordlists['verbs']
    return secrets.choice(l)


def choose_adverb(wordlists: dict) -> str:
    l = wordlists['adverbs']
    return secrets.choice(l)


_s = choose_noun
_v = choose_verb
_o = choose_noun
_adv = choose_adverb


def make_svo_phrase(wordlists: dict) -> tuple[str, str, str]:
    return (_s(wordlists), _v(wordlists), _o(wordlists))


def make_svoadv_phrase(wordlists: dict) -> tuple[str, str, str, str]:
    return (_s(wordlists), _v(wordlists), _o(wordlists), _adv(wordlists))


def as_line(phrase: tuple) -> str:
    return " ".join(phrase).lower()


def make_haiku(wordlists: dict) -> str:
    line_1 = as_line(make_svo_phrase(wordlists))
    line_2 = as_line(make_svoadv_phrase(wordlists))
    line_3 = as_line(make_svo_phrase(wordlists))
    haiku = "\n".join((line_1, line_2, line_3))
    return haiku


def main():
    wordlists = get_wordlists()
    # validate_wordlists_uniqueness(wordlists)
    haiku = make_haiku(wordlists)
    _, total_entropy = entropy_calculation.get_entropy_info(wordlists)
    print(f"----- Haikuware {haikuware_version} -----")
    print(haiku)
    print(f"----- {round(total_entropy, 2)} bits -----")
    

if __name__ == "__main__":
    main()

