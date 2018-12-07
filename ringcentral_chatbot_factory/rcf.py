
from .cmd import cmd
import argparse
import os
from os.path import dirname, realpath, join, isabs
import pydash as _

def main():
  cwd = os.getcwd()
  parser = argparse.ArgumentParser(
    description='''
Cli tool to create a RingCentral chatbot project.
Example: rcf my-chatbot-app
    '''
  )
  parser.add_argument(
    'path',
    metavar='p',
    help='Project folder name like my-chatbot-app'
  )

  try:
    args = parser.parse_args()
  except:
    return parser.print_help()

  if not _.predicates.is_string(
    _.get(args, 'path')
  ):
    parser.print_help()
  else:
    name = args.path
    p = name
    if not isabs(name):
      p = join(cwd, name)

    cmd(p, name)