import random
import string

def autogenerate_token(token_length):
  '''
  generates a password from alphanumenric  characters
  '''
  character_pool = string.ascii_letters + string.digits
  return "".join((random.choice(character_pool) for i in range(token_length)))
