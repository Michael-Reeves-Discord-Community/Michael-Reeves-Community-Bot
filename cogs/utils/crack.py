import json
import collections 
from collections import namedtuple
import functools # <= for future stuff  idk 

#i thought that named tuple was in functools lmfao
#looking at docs and working on stuff on my class 

def get(file):
    try:
        with open(file , encoding='utf-8') as data:
            return json.load(data, object_hook= lambda d: namedtuple('X', d.keys())(*d.values()))
		except AttributeError:
			raise AttributeError('unkown argument')
	except FileNotFoundError:
		raise FileNotFoundError("json wasent found dips shit ")


