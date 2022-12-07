#!/usr/bin/python3
def multiple_returns(sentence):
    len_ = len(sentence)
    if len_ == 0:
        returnstring = "None"
    returnstring = sentence[0]
    return (len_, returnstring)
