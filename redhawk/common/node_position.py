""" Definition of the NodePosition class."""

class NodePosition:
  def __init__(self, file, line, column):
    self.file = file
    self.line = line
    self.column = column
    return

  def GetFile(self):
    return self.file

  def GetLine(self):
    return self.line

  def GetColumn(self):
    return self.column

  def __repr__(self):
    return "[%s:%4s:%3s]"%(self.file, self.line, self.column)
  
  def __str__(self):
    return self.__repr__()

