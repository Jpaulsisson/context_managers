# Let's learn how to build a class based context manager
from contextlib import contextmanager

class MyContextManager:
  def __init__(self) -> None:
    print('this init function runs')
    
  def __enter__(self):
    print('then this enter function runs')
    
  def __exit__(self, *exc):
    print('and finally I make it over')
    # note that *exc is just a way of skipping adding the required arguments in the __exit__ function call
    
# with MyContextManager() as MCM:
#   print('I do my thing right after __enter__')
  

# an example from Codecademy where we open a file for use

class PoemFiles:
  def __init__(self, poem_file, mode):
    print('Starting up a poem context manager')
    self.file = poem_file
    self.mode = mode
    
  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  # This is more in line with a real __exit__ 
  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type)
    print(exc_value)
    print(traceback)
    self.opened_poem_file.close()
    # We can also specify how to handle specific errors with isinstance and a conditional
    if isinstance(exc_value, AttributeError):
      print("you got a attribute error dawg.. prolly callin something this class ain't got")
      return True
    # returning True suppresses the error, returning False does nothing
    
# with PoemFiles('poem.txt', 'r') as file2:
#   print(file2.read())
#   print("---- Exception data below ----")
  
    
# with PoemFiles('poem.txt', 'r') as file2:
#   print(file2.errormaker())
  

# now let's use that import to do this same thing but prettier
@contextmanager
def pretty_poem_files(file, mode):
  open_file = open(file, mode)
  try:
    print('Pretty file opening')
    yield open_file
  finally:
    print('Closing pretty file')
    open_file.close()
    
    
with pretty_poem_files('poem.txt', 'r') as ppf:
  print(ppf.read())