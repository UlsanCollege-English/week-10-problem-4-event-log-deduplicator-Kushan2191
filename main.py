def hash_function(key, m):
    return sum(ord(c) for c in key) % m

def make_set(m):
    return {'buckets': [[] for _ in range(m)], 'size': 0}

def add(s, key):
    bucket_index = hash_function(key, len(s['buckets']))
    bucket = s['buckets'][bucket_index]
    if key in bucket:
        return False
    bucket.append(key)
    s['size'] += 1
    return True

def contains(s, key):
    bucket_index = hash_function(key, len(s['buckets']))
    bucket = s['buckets'][bucket_index]
    return key in bucket

def remove(s, key):
    bucket_index = hash_function(key, len(s['buckets']))
    bucket = s['buckets'][bucket_index]
    if key in bucket:
        bucket.remove(key)
        s['size'] -= 1
        return True
    return False

def size(s):
    return s['size']
