# Returning after a few days
# I am really tired
# let's get back to it!! Lists today :) (as far as I remember it was pretty easy)

# It's basically the same concept as an array on other languages. I think it is nice because lists can contain several
# different data types
sample_list = ['I am a string', 5, "QA", 7.9, '5.7']
print(sample_list)

print("The size of the above list is " + str(len(sample_list)))

sample_list.append("dog")
last_element_added = sample_list.pop()

print(last_element_added) # <- nice! it printed the last element added to the list without the need to specify

# If I wanted to specify the element to be removed of the list, I could use the method "remove()"
sample_list.remove(5)

print(sample_list)