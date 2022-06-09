from pex import *
from sys import *

engine = PexEngine()
engine.Build(argv[1], 10)
engine.Run(argv[1][:-2] + "pex")