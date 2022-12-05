#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    l = len(sentence)
    return (l, sentence[0])
