import hashmap

states = hashmap.new()
print states

key = 'Oregon'

print hash(key)

print len(states)

print hash(key) % len(states)

key = hash(key) % len(states)

print key

print states[key]

bucket = states[key]

print enumerate(bucket)

for i,kv in enumerate(bucket):
    print 'ok'
    print i,kv

print "oookkk"
value = 'OR'
bucket.append((key,value))

for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            print i, k, v

print "KKKKKKKK"

for i in enumerate(bucket):
    print i
