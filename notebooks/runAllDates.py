from NotebookScripter import run_notebook
import sys
import json
import datetime
import os
import matplotlib.pyplot as plt
            
notebook = sys.argv[1]

numdays=90
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]
date_list.reverse()

check = ['1_countryshift.png','9_usstates.png']

#kwargs = {}
#if len(sys.argv)>2:
#   kwargs = dict([(t[0],t[1]) for t in [x.split('=') for x in sys.argv[2:]]]) 

#for f in sys.argv[1:]:
#print('Running {} with args {}'.format(notebook, json.dumps(kwargs)))
for d in date_list:
    p = d.strftime('%Y%m%d')
    for c in check:
        fn = os.path.join('data',p,c)
        if not os.path.exists(fn):
            print('running for {}'.format(fn))
            run_notebook(notebook, **{'endDate':d.strftime('%Y-%m-%d')})
            assert(os.path.exists(fn))
            plt.close("all")