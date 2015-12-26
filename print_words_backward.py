a = "print all words backward"

print a
print a[::-1]
print ' '.join(a.split()[::-1])



def print_backward(a):
    b = a.split()[len(a):0:-1]
    b = ' '.join(b)
    print  b +" " + a.split()[0]
    

print "xrange"
print ''.join((a[i] for i in xrange(len(a)-1, -1, -1)))

print_backward(a)


