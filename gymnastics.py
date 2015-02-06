scores = range(1, 11)
tuple(scores)
print "The lowest possible score is %s. and the highest possible score is %s." % (scores[0], scores[-1])

for score in scores:
    if score == 1:
        print "A judge can give a gymnast %s point" % score
    else:
        print "A judge can give a gymnast %s points" % score

