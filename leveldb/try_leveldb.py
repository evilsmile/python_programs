#!/usr/bin/env python

import leveldb

db = leveldb.LevelDB('./db')
db.Put('hello', 'world')
print db.Get('hello')

db.Delete('hello')
# It's error
#db.Get('hello')

for i in xrange(10):
    db.Put(str(i), 'string_%s' % i)
print list(db.RangeIter(key_from = '2', key_to = '5'))

batch = leveldb.WriteBatch()
for i in xrange(1000):
    db.Put(str(i), 'iiiistringi_%s' % i)

db.Write(batch, sync = True)
print list(db.RangeIter(key_from = '2', key_to = '99'))
