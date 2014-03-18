#!/usr/bin/python

import json
import urllib2

MOD_TAG = 'develop'

# overview
f = open('mod.md', 'w+')
f.write('''
# Part 3 - Mods
## 1. Overview
There are four categories of Mods:

    - Meta: internal mods specific to VisualOps
    - Common: portable mods across linux and windows
    - Linux: linux-specific mods
    - Windows: windows-specific mds

NOTE: the following document is based on the version **`https://github.com/MadeiraCloud/salt/tree/%s`**
''' % MOD_TAG)

# category
mod = json.loads(urllib2.urlopen('https://raw.github.com/MadeiraCloud/salt/%s/sources/module.json' % MOD_TAG).read())
del mod['tag']
del mod['windows']

for i, cat in enumerate(mod):
	d = '''
## %d. %s
''' % (i+1, cat)
	f.write(d)

	for ii, m in enumerate(mod[cat]):
		d = '''
### %d.%d - %s
%s
'''	% (
	i+1, ii+1, m if m != '#' else '&num;',
	mod[cat][m]['reference']['en'].replace('###', '####')
)
		f.write(d)

f.flush()
f.close()
