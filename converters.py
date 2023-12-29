#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Converter(ABC):

    @abstractmethod
    def convert(self, text: str) -> str:
        pass

class DirectConverter(Converter):

    def __init__(self, conv_dict):
        self.conv_dict = conv_dict

    def convert(self, text: str) -> str:
        result: str = ""
        for ch in text: 
            if ch not in self.conv_dict:
                result += ch
                continue
            result += self.conv_dict[ch]
        return result

