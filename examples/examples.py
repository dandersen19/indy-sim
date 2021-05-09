# IndySim Project
# Copyright (C) 2021 Drake Andersen
# Functions for simulating performances of indeterminate music for analysis

####################
####  EXAMPLES  ####
####################

# import a melody from an XML file
my_melody = import_part('/Users/User/sample_score.xml')

# import a second melody using optional args to specify part (1) and measure range (1-3)
my_melody2 = import_part('/Users/User/sample_score.xml', part=1, excerpt=True, first_bar=1, last_bar=3)

# import two staves from a score (parts 0 and 1) into a single part (for multistaff instruments like piano)
my_melody3 = import_multistaff('/Users/User/sample_score.xml', [0,1])

# you can also enter a melody directly as a list of MIDI note numbers
# melodies can contain single notes, chords, or both (chords are imported as sub-lists)
my_melody4 = [73, 71, 69, [52, 56, 59, 68], 76, [49, 52, 55, 58], 67]

# one virtual performance, length = 100, no leading silence
perf1 = one_perf(my_melody, 100, leading=False)

# simulate ten performances of melody, length = 100, with silences interspersed...
sim1 = build_sim(my_melody, 100, 10, between=True)

# ...and ten performances of another melody without interspersed silences
sim2 = build_sim(my_melody2, 100, 10, between=False)

# organize simulation results by unit time...
sim_by_time = sim_time(sim1)

# ...in order to examine pitch content over time
for elem in sim_by_time:
	print(set(elem))

# combine simulations to get verticalities between parts (sims must have same length/number of perfs)
combine_sims([sim1, sim2])

# see the most prevalent set class per unit time (over the first 100 time units)
for i in range(100):
   print("Time Unit:",i)
   max(set_frequency(event11[i]).items(), key=operator.itemgetter(1))[0]

# add example with get_lewins function

#####################
#####   NOTES   #####
#####################

'''
performance length should generally be at least one order of magnitude greater than sequence length
(sequence length = melody length plus any leading, trailing, or interspersed zeroes)
if the two values are too close it will take too long to get random values that don't duplicate
'''
