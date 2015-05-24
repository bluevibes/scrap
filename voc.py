import sys
import argparse
import os
import json
import subprocess as sp

def loadjson(jpath):
  if os.path.isfile(jpath):
    try:
      jdata=json.loads(open(jpath).read())
    except ValueError:
      print "Invalid json :",jpath
    return jdata
  else:
    print "File not found :",jpath
    return False

def init():
  #implement this
  print "Implementation left."
  
def edit():
  print "Implementation left."
  
def revise():
  print "Implementation left."
  
def test():
  print "Implementation left."
  
def search():
  print "Implementation left."
  
def stats():
  print "Implementation left."
  
def export():
  print "Implementation left."

#main
parser=argparse.ArgumentParser()
parser.add_argument('-p','--path',help='full path of the json file',required=False)
parser.add_argument('-n','--new',help='initialise a new json file',action='store_true',default=False)
args=parser.parse_args()

if args.path :
  jpath=args.path
else :
  jpath=os.path.dirname(os.path.realpath(__file__))+'/vocab.json'

if args.new == True:
  if os.path.isfile(jpath):
    cmd='mv '+jpath+' '+jpath+'.bkp'
    code=os.system(cmd)
    if code == 0:
      print 'The original %s backed up.',jpath
      init()
    else :
      print "File %s already exists and could not be backed up.",jpath
      
jdata=loadjson(jpath)
if jdata == False:
  exit(1)

while True:
  trash=os.system('clear')
  choice=raw_input ("Enter the choice : \n(1) Edit \n(2) Revise \n(3) Test \n(4) Search \n(5) Stats \n(6) Export \n(0) Exit")
  if choice == 1:
    edit()
  elif choice == 2:
    revise()
  elif choice == 3:
    test()
  elif choice == 4:
    search()
  elif choice == 5:
    stats()
  elif choice == 6:
    export()
  elif choice == 0:
    exit(0)
