class Outputer:
  def __init__(self,filename=None):
    self.filename = filename
  def output(self,l,filename=None):
    if filename:
      self.filename = filename
    if not self.filename:
      print("Filename not provided")
      return
    with open(self.filename,"w") as file:
      for i in l:
        file.write(str(i)+"\n")