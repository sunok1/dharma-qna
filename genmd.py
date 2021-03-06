# -*- coding: utf_8 -*-

import sqlite3
import sys  

# sys.setdefaultencoding('utf_8')

c = sqlite3.connect('dharmaqna.db')

f = open('PROJECTS.md', 'w')
f.write('## Published\n\n');
f.write('| NO | TITLE         | XLS | PUBLISHED | EN | FR | DE |\n')
f.write('|----| ------------- |-----|-----------|----|----|----|\n')

for row in c.execute('SELECT v.vid,en.title,v.xlsfn,v.pubdate,en.fn,fr.fn,de.fn \
                        FROM video v \
                        LEFT OUTER JOIN en ON v.vid = en.vid \
                        LEFT OUTER JOIN fr ON v.vid = fr.vid \
                        LEFT OUTER JOIN de ON v.vid = de.vid \
                       WHERE status=\'published\' \
                       ORDER BY v.pubdate DESC \
                         ' ):
    vid     = row[0]
    title   = row[1].encode('utf8')
    xlsfn   = row[2]
    pubdate = row[3]
    fn_en   = row[4]
    fn_fr   = row[5]
    fn_de   = row[6]
    # titlelink = "[#%s %s](sub/%s)" % (vid, title, vid)
    nolink = "[%s](sub/%s)" % (vid,vid)
    xlslink = "[![](img/excel.png)](sub/%s/%s)" % (vid,xlsfn)
    enlink  = "[en](sub/%s/%s)" % (vid,fn_en) if fn_en is not None else ''
    frlink = "[fr](sub/%s/%s)" % (vid,fn_fr) if fn_fr is not None else ''
    delink = "[de](sub/%s/%s)" % (vid,fn_de) if fn_de is not None else ''
    f.write("| %s | %s | %s | %s | %s | %s | %s |\n" % ( nolink, title, xlslink, pubdate, enlink, frlink, delink ))
f.close()

