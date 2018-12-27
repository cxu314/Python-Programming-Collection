class HashTable:
    """A reusable library of a hash table implementation.

    Attributes:
        nbuckets: An integer number of buckets.
                  It should be a prime number to avoid collisions.
        buckets: A list of lists representing buckets.
    """

    def __init__(self, nbuckets):
        """Inits HashTable with nbuckets and buckets."""
        self.nbuckets = nbuckets
        self.buckets = [[] for i in range(nbuckets)]

    def buckets_str(self):
        """
        Return a string representing the various buckets of this table.
        The output looks like:
            0000->
            0001->
            0002->
            0003->parrt:99
            0004->
        where parrt:99 indicates an association of (parrt,99) in bucket 3.
        """
        s = [[] for i in range(self.nbuckets)]
        for i in range(self.nbuckets):
            for (k, v) in self.buckets[i]:
                s[i].append(str(k) + ':' + str(v))

        mystring = ''
        for i in range(len(self.buckets)):
            mystring += str(i).zfill(4) + '->' + ', '.join(s[i]) + '\n'

        return mystring

    def __str__(self):
        """
        Return a regular Python dict such as {parrt:99} with str(table).
        The order should be bucket order and insertion order in the bucket.
        """
        s = []
        for i in range(len(self.buckets)):
            for (k, v) in self.buckets[i]:
                s.append(str(k) + ':' + str(v))

        mystring = '{'
        mystring += ', '.join(s)
        mystring += '}'

        return mystring

    def get(self, key):
        """
        Return table[key].
        Find the appropriate bucket and look for the association with the key.
        Return the value (not the key and not the association!)
        Return None if key not found.
        """
        bucket, idx = self.bucket_indexof(key)

        if idx is None:
            return None
        else:
            return bucket[idx][1]

    def put(self, key, value):
        """
        Perform table[key] = value
        Find the appropriate bucket and then append a value to the bucket.
        If the bucket already has that key, then replace that value.
        Otherwise, add (key, value) associations to the buckets.
        """
        bucket, idx = self.bucket_indexof(key)

        if idx is None:
            bucket.append((key, value))
        else:
            bucket[idx] = (key, value)

    def bucket_indexof(self, key):
        """
        Return the element within a specific bucket.
        The bucket is table[key].
        The idx is the index of the element in that bucket.
        If there is no such element in that bucket, idx returns None.
        """
        bucket = self.buckets[self.hashcode(key) % self.nbuckets]

        for idx, (k, v) in enumerate(bucket):
            if k == key:
                return bucket, idx

        return bucket, None

    def hashcode(self, key):
        """
        Return a hashcode for strings and integers; all others return None.
        For integers, just return the integer value.
        For strings, perform h=h*31+ord(c) for all characters in the string.
        """
        if isinstance(key, int):
            return key
        elif isinstance(key, str):
            h = 0
            for c in list(key):
                h = h*31 + ord(c)
            return h
        else:
            return None
