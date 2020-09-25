from NotebookScripter import run_notebook
import sys
import json

notebook = sys.argv[1]
kwargs = {}
if len(sys.argv)>2:
   kwargs = dict([(t[0],t[1]) for t in [x.split('=') for x in sys.argv[2:]]]) 

#for f in sys.argv[1:]:
print('Running {} with args {}'.format(notebook, json.dumps(kwargs)))

run_notebook(notebook, **kwargs)