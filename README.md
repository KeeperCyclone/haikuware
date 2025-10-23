# haikuware

[Diceware](https://en.wikipedia.org/wiki/Diceware) is a pretty popular method for randomly choosing words for passphrases. I hate how ugly and nonsensical such phrases turn out to be, though, so I wrote a proof-of-concept for `haikuware`:

```bash
user@machine:~/haikuware$ python3 haikuware-1.1.pyz 
----- Haikuware 1.1 -----
broom eradicates trap
sun wines end playful
bust bulks prop
----- 99.12 bits -----
```

This uses Python's `secrets` module to crypto-randomly choose words from "nouns," "verbs," and "adverbs" word lists, generating a haiku-like verse with an *SVO // SVO+Adv // SVO* structure. It's only haiku-like in the sense that it is structured as three lines with 3+4+3 words.

I think this haiku-like format is a neat little grammatical package that helps smooth memorization along. I mean, it's pretty hard *not* to memorize "broom eradicates trap."

## Security & Wordlists

Unfortunately, the word lists only have 1,024 nouns, 1,145 verbs, and 398 adverbs as of v1.1, so each haiku's entropy caps out at 99.12 bits.

Also, the entropy could be lower than advertised since I hadn't deduplicated cross-category words, but I couldn't actually find any duplicates after a cursory inspection, so the effects of duplication should be minimal.

To be clear, I'm only relatively confident that the effects of cross-category duplication is minimal because of these conditions:

- all nouns are singular
- all verbs agree with singular nouns

This means that in phrases like "sun wines end playful," the word "wines" is strictly found in `verbs.txt`, because if it were in `nouns.txt`, it could only be "wine."

As for the wordlists, I had Gemini generate them, then I deduplicated each list with a quick `:sort u` in Neovim— *Don't look at me like that!* I'm aware of `nltk` and the EFF wordlists, but this is just a proof-of-concept. Why take 10 minutes to learn a new package when there's a perfectly serviceable, grammatically-aware slop generator that can do it in 30 seconds flat?


## Future Development

Assuming I get around to doing it:

- [ ] Sorting and filtering the EFF wordlists (and others?) should help me come up with 10,000 nouns, 10,000 verbs, and maybe 500 adverbs. `haikuware` will be able to generate 128-bit entropy passphrases this way.
- [ ] Handcrafting the wordlists so that the generated phrases feel more coherent, therefore making them more memorable.


## See Also

- [Correct Horse Battery Staple](https://xkcd.com/936/)
- [NIST recommends simple-but-long passphrases over complex-but-short passwords.](https://pages.nist.gov/800-63-3/sp800-63b.html#appA)
