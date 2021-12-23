# EMOJI Converter

em = input("Enter the Emoji code:- ")
print()
print("*******EMOJI Converter*******")
# if em == ":)":
#     print("\N{slightly smiling face}") # Smiling face
# elif em == ":(":
#     print("\N{winking face}")  # Sad face
# else:
#     print("Emoji Code",em,"does not exist in my library at the moment")

words = em.split(" ")
emojicon = {
    ":)" : "😊",
    ":(" : "🙁"
}
outp = ""
for word in words:
    outp = outp + emojicon.get(word,word) + " "
print("Emoji Code",em,"is", outp)