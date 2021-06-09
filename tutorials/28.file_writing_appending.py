# f = open("barinder.txt", "w")
# a = f.write("barinder bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("barinder2.txt", "a")
# a = f.write("barinder bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("barinder2.txt", "r+")
print(f.read())
f.write("thank you")
  
