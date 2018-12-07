from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import tempfile
import sys, os
from os.path import join
from requests_download import download
from zipfile import ZipFile
import pydash as _
import json
import re

tempDir = tempfile.gettempdir()

supportedLanguage = {
  'python': {
    'zip': 'https://github.com/zxdong262/ringcentral-chatbot-template-python/archive/master.zip',
    'folderName': 'ringcentral-chatbot-template-python-master'
  }
}

def validateName(input = ''):
  if input.strip() == '':
    return 'project name is required'
  elif len(input) > 50:
    return 'project name max length: 50'
  return True

def validateDesc(input = ''):
  if input.strip() == '':
    return 'project description is required'
  elif len(input) > 1000:
    return 'project description max length: 1000'
  return True

questions = [
  {
    'type': 'input',
    'name': 'name',
    'message': 'Project name, eg: my-great-app',
    'validate': validateName
  },
  {
    'name': 'description',
    'type': 'input',
    'message': 'Project description',
    'validate': validateDesc
  },
  {
    'name': 'version',
    'type': 'input',
    'message': 'Project version',
    'default': '0.0.1'
  },
  # {
  #   'name': 'language',
  #   'type': 'input',
  #   'message': 'What programming language do you use? Currently only support python',
  #   'default': 'python',
  #   validate: input => {
  #     if (!Object.keys(supportedLanguage).includes(input)) {
  #       return 'Currently only support python'
  #     }
  #     return true
  #   }
  # },
  {
    'type': 'confirm',
    'name': 'confirm',
    'message': 'Can you confirm?',
    'default': True
  }
]

def verifyResult(res):
  return len(res.keys()) == len(questions)

def untar(fname):
  with ZipFile(fname) as zf:
    zf.extractall(
      tempDir
    )
    zf.close()

def fetchZip(url, folderPath):
  print('fetching', url, '-->', tempDir)
  zipName = folderPath + '.zip'
  try:
    os.rmdir(folderPath)
  except:
    pass
  try:
    os.remove(folderPath + '.zip')
  except:
    pass
  download(url, zipName)
  untar(zipName)

def editFiles(fromPath, res):

  # package.json
  pkg = join(fromPath, 'package.json')
  with open(pkg, 'r+') as toOpenFile:
    pkgInfo = toOpenFile.read()
    pkgInfo = json.loads(pkgInfo)
    pkgObj = {
      'name': res['npmName'],
      'version': res['version'],
      'description': res['description'],
      'keywords': pkgInfo['keywords'],
      'devDependencies': pkgInfo['devDependencies']
    }
    f = json.dumps(pkgObj, indent=2)
    toOpenFile.seek(0)
    toOpenFile.write(f)
    toOpenFile.truncate()
    toOpenFile.close()

  # README
  readme = join(fromPath, 'README.md')
  with open(readme, 'r+') as toOpenFile:
    readmeStr = str(toOpenFile.read())
    arr = readmeStr.split('## Prerequisites')
    final = f'''
# {res['name']}

${res['description']}

## Prerequisites${arr[1]}
  '''
    toOpenFile.seek(0)
    toOpenFile.write(final)
    toOpenFile.truncate()
    toOpenFile.close()

def cmd(targetPath, name):
  questions[0]['default'] = name
  res = prompt(questions)
  if not verifyResult(res):
    return quit()

  res['confirm'] = None
  res['npmName'] = re.sub(r'\s+', '-', res['name'])

  print('''
    building...
  ''')
  language = 'python'
  obj = supportedLanguage[language]
  zip = obj['zip']
  folderName = obj['folderName']
  fromPath = join(tempDir, folderName)
  fetchZip(zip, fromPath)
  editFiles(fromPath, res)
  os.rename(fromPath, targetPath)
  print(
    f'''
    ================================
    Done! Now you can run "cd {name}" and follow {name}/README.md's instruction to dev/test/deploy the bot!
    ================================
  ''')

