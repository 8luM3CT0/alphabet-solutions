#You need to free the bunny workers before 
# Commander Lambda's space station explodes! 
# Unfortunately, the Commander was very careful 
# with the highest-value workers -- they all work 
# in separate, maximum-security work rooms. The 
# rooms are opened by putting keys into each console, 
# then pressing the open button on each console 
# simultaneously. When the open button is pressed, 
# each key opens its corresponding lock on the work 
# room. So, the union of the keys in all of the 
# consoles must be all of the keys. The scheme may 
# require multiple copies of one key given to 
# different minions.

#The consoles are far enough apart that a separate 
# minion is needed for each one. Fortunately, you 
# have already relieved some bunnies to aid you - 
# and even better, you were able to steal the keys 
# while you were working as Commander Lambda's 
# assistant. The problem is, you don't know which 
# keys to use at which consoles. The consoles are 
# programmed to know which keys each minion had, 
# to prevent someone from just stealing all of the 
# keys and using them blindly. There are signs by the 
# consoles saying how many minions had some keys 
# for the set of consoles. You suspect that Commander 
# Lambda has a systematic way to decide which keys 
# to give to each minion such that they could use the 
# consoles.

#You need to figure out the scheme that Commander 
# Lambda used to distribute the keys. You know how 
# many minions had keys, and how many consoles are 
# by each work room.  You know that Command 
# Lambda wouldn't issue more keys than necessary 
# (beyond what the key distribution scheme requires), 
# and that you need as many bunnies with keys as 
# there are consoles to open the work room.

#Given the number of bunnies available and the 
# number of locks required to open a work room, 
# write a function solution(num_buns, num_required) 
# which returns a specification of how to distribute 
# the keys such that any num_required bunnies can 
# open the locks, but no group of (num_required - 1) 
# bunnies can.

#Each lock is numbered starting from 0. The keys 
# are numbered the same as the lock they open 
# (so for a duplicate key, the number will repeat, 
# since it opens the same lock). For a given bunny, 
# the keys they get is represented as a sorted list of 
# the numbers for the keys. To cover all of the 
# bunnies, the final solution is represented by 
# a sorted list of each individual bunny's list of keys.  
# Find the lexicographically least such 
# key distribution - that is, the first bunny should have 
# keys sequentially starting from 0.

#num_buns will always be between 1 and 9, 
# and num_required will always be between 0 and 9 
# (both inclusive).  For example, if you had 3 bunnies 
# and required only 1 of them to open the cell, 
# you would give each bunny the same key such that 
# any of the 3 of them would be able to open it, like 
# so:
#[
#  [0],
#  [0],
#  [0],
#]
#If you had 2 bunnies and required both of them to 
# open the cell, they would receive different keys 
# (otherwise they wouldn't both actually be required), 
# and your solution would be as follows:
#[
#  [0],
#  [1],
#]
#Finally, if you had 3 bunnies and required 2 of them 
# to open the cell, then any 2 of the 3 bunnies should 
# have all of the keys necessary to open the cell, but 
# no single bunny would be able to do it.  Thus, the 
# solution would be:
#[
#  [0, 1],
#  [0, 2],
#  [1, 2],
#]





#will try multple solutions for this
#have to understand for explanation reasons

#SOLUTION #1

from itertools import combinations

def solution(num_buns, num_required):
    #Init the list of keys
    keyrings=[[] for num in range(num_buns)]
    #Calc the amount of copies required
    # per key 
    copies_per_key = num_buns - num_required + 1
    #Append keys to list keyrings
    for key, bunnies in enumerate(combinations(range(num_buns), copies_per_key)):
        for bunny in bunnies:
            keyrings[bunny].append(key)
    
    return keyrings

    #TESTING IF IT WORKS
    #Conclusion: did not work. Probably has errors
    #Connclusion no.2 : nvm, it worked

    #explanation:
    # If you have N bunnies, and M locks, distribute M distinct keys among the bunnies so that it will always require num_required bunnies 
    # to open the locks, and no bunny should have the same key twice.

    #Let us now consider this simple situation, let us say we have chosen num_required−1 bunnies at random, and we were to choose 1
    #more bunny to get the complete set of keys to open the prison door. We know that these num_required−1 bunnies cannot open 
    # the door by themselves and hence the remaining num_bunnies−num_required+1 bunnies must have a key that these
    # num_required−1  bunnies don’t. We have total (num_bunsnum_required−1) combination of each num_required−1 bunnies pair, so we have
    #also (num_bunsnum_required−1) distinct keys. And there should be num_buns−num_required+1 copies of each distinct key among the
    #bunnies

    #Note that (num_bunsnum_required−1)=(num_bunsnum_buns−num_required+1)

    #Thus, for the example of N = 5 and M = 3, there are (53−1) distinct keys (10 keys).

    #We must distribute 5−3+1 copies of all 10 keys amongst the bunnies in such a way that any 3 bunnies we pair together have, amongst them, 
    # at least one copy of every key.

    #we count number of distinct keys we have with formula (num_bunsnum_required−1).
    #Find the number of copies per key num_buns−num_required+1
    #Yield combinations of keyholders one at a time, and we give key to each keyholder


#personal answer
#based off on the code above

from itertools import combinations

def solution(num_buns, num_required):
    unlockers = [[] for n in range(num_buns)]
    multi_unlockers = num_buns - num_required + 1
    for unlocker, buns in enumerate(combinations(range(num_buns), multi_unlockers)):
        for bunny in buns:
            unlockers[bunny].append(unlocker)

    return unlockers