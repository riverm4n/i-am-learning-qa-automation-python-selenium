# returned after 1-day pause (had a birthday party yesterday. these pauses are going to be pretty regular. I'm not
# always at home at night (thankfully!)

# Starting of class 16. Reached 5% of the course!! Here goes sequence types (strings, lists, tuple,...)

#String samples
print("\n" + "==========================")
print("String samples: (btw, this is one as well):")
print("==========================")

string_sample1 = "This sentence is a string."
print("\n" + string_sample1 + " Do you doubt it? Let's check below. \n" + str(type(string_sample1)))

string_sample2 = '5'
print("'" + string_sample2 + "' is a string as well. Do you doubt it? Ok \n" + str(type(string_sample2)))

# Operations with strings (Slicing)
print("\n" + "==========================")
print("2. String operations/methods:")
print("==========================")
print("\n2.1 Slicing:")

# remember (you never forgot -- yeah i'm kind of funny today) that indexing starts to count from 0 if orientation is
# left -> right
most_generic_string_in_the_world_just_for_sample = "BUNNY IS A RIDER"

print("Whole string: " + most_generic_string_in_the_world_just_for_sample)
print("Sliced (from 0 to 5): " + most_generic_string_in_the_world_just_for_sample[0:5])
print("Just the 8th character: " + most_generic_string_in_the_world_just_for_sample[7])

print("==========================")
print("2.2 String's length:")
print("If you want to know the length of a string, use the function 'len(str)': " +
      str(len(most_generic_string_in_the_world_just_for_sample)))

print("==========================")
print("2.2 String manipulation:")

new_sample_string = "Charli XCX"
print("For these new examples, our string will be '" + new_sample_string + "'. Let's see a few manipulations on it: \n")

print("Make everyghing upper case: " + new_sample_string.upper())
print("Make everything lower case: " + new_sample_string.lower())
print("Split the sentence: " + str(new_sample_string.split()))
print("Count how many times the letter 'C' appears: " + str(new_sample_string.count('C')))


# Gotta confess. I am having fun but maybe it is because it is too easy. That's exactly why I am kind of bored. It is
# very basic and yeah, I thought I would really need everything but yeah, I haven't fully forgot how to program (yeah
# I know and hope it gets more complex hehe