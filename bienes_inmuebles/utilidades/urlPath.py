from pathlib import Path


class UrlPath():
    @staticmethod
    def getPath(file, dir=0):
       path = Path(file)
       pathFinal = Path(path.parents[dir])
       return pathFinal

