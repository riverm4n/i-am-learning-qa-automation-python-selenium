# I was not remembering this but after one example I was able to learn again this concept (it is not a class, but is
# somewhat close (?) ok I get it this is not oop but yeah

dict_sample = {
    "first_name": "Mario",
    "restof_name": "Hirotoshi Sugai Junior",
    "age:": 25
}

wisl_leaders = {"manual": "Ana", "automation": "Fabi", "innovation": "Walter?"}

# Dictionaries are NOT sequenced, so indexing is not available. This is important to have in mind.
my_leader = wisl_leaders.get("manual")
print(my_leader)

# but if we use the method to get all of the values (dictionaire.values()) or all of the keys (dictionaire.keys()), they
# are iterable...

fav_each_album_from_the_national = {
    "self titled" : "a beautiful head",
    "sad songs for dirty lovers" : "cardinal song",
    "cherry tree ep" : "I don't mind",
    "alligator" : "mr. november", # but I love the whole album basically
    "boxer" : "gospel",
    "high violet" : "afraid of everyone",
    "trouble will find me" : "this is the last time",
    "sleep well beast" : "the system only dreams in total darkness",
    "i am easy to find" : "quiet light",
    "first two pages of frankenstein" : "???"
}

fav_from_SWB = fav_each_album_from_the_national["sleep well beast"]
fav_from_IAETF = fav_each_album_from_the_national.get("i am easy to find")

print(fav_from_SWB)
print(fav_from_IAETF)

# Get key that does not exist
# fav_from_saddads = fav_each_album_from_the_national["sad dads"] <--- this will return an error!
fav_from_saddads = fav_each_album_from_the_national.get("sad dads")
print(fav_from_saddads)
fav_from_notreleased = fav_each_album_from_the_national.get("radioheads", "This album was not released (yet) XD")
print(fav_from_notreleased)

# Using the older dict for addition example:
wisl_leaders["nelows"] = "Cinthia"

# Other method
wisl_leaders.update({"sponsor":"Ricardo"})

print(wisl_leaders)

###### ASSIGNMENTS
# Assignment 1: Add a value to a key that already exists and see what happens:
fav_each_album_from_the_national["boxer"] = "squalor victoria"
print(fav_each_album_from_the_national.get("boxer"))
# It has successfully updated the value for a given key. Clever!

# Assignment 2: Lookup what does the method "setdefault()" does?
# The setdefault() method returns the value of the item with the specified key.

# If the key does not exist, insert the key, with the specified value.