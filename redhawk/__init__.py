import os

__version__ = '1.1.5'
DB_NAME = '.redhawk_db'

def GetVersion():
  return __version__

def GetDBName():
  return DB_NAME
