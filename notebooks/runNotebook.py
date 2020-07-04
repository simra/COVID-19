from NotebookScripter import run_notebook
import sys

for f in sys.argv[1:]:
    print('Running {}'.format(f))
    run_notebook(f)