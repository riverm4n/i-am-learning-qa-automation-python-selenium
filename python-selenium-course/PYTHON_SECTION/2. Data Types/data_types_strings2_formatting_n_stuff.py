# Returning, on day 4!! It seems like I've accomplished 10% of the course. Wow bob wow!

# Strings - Formatting
# used very often! strings are modified with a given data, so, a string is basically a placeholder until that data is
# given. He says that the Python version matters here.

sample_var = "I love {} programming language".format("Java")
print(sample_var)

# this was a funny one. I don't actually love any programming language haha the teacher used Python as an example, and I
# said Java considering this is the closest to love for me. You (no one is actually reading this code, I bet) might be
# asking yourself then why I chose Python to do this course if you can use Java and Selenium as well.
# Well, I'll tell you:
#   1. Although Java still a pretty popular language nowadays, I thought that since Python is on fashion (for a few
# years now), it might be a good choice
#   2. I don't have all the time in the world to write all that code required in Java, so I thought it would be faster
# to learn with Python
#   3. >Until now< I believe I am a better Java developer than a Python developer. So it would be a very nice exercise
# to do this course

# Yes I will not comment code like that on a serious company but since I am working by myself here I thought it would be
# nice to comment a code as if it was a stream of consciousness.

sample_var2 = "{} is {} years old".format("Mario", 25)
print(sample_var2)
# everything means everything. data types on python, I did not have to specify any single thing above

name, age   = "Mario Hirotoshi", 25
sample_var3 = "{name} is {age} years old".format(name=name, age=age) # <- this looks like redundant code. I should
# delete line 28 and not waste memory resources for those variables. Anyway..
print(sample_var3)

sample_var4 = "{0} is {1} years old".format("Mario", 25) # <- this one is TERRIBLE, but works... I guess
print(sample_var4) # yes it does...

# Ok so this one below I found to be kind of weird in the syntax, but it actually seems to be very ok-ish(?)

programming_lang = "Java"
sample_var5      = f"I love {programming_lang} programming language"
print(sample_var5) # this one actually surprised me

sample_var5 = f"{name} is {age} years old." # reusing the same variable (yeah I just remembered that NOW)
print(sample_var5)

sample_var5 = f"There are {len(programming_lang)} letters in '{programming_lang}'"
print(sample_var5)

