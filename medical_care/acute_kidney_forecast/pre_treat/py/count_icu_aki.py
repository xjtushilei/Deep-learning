import  numpy

with open('../label.txt') as file:
    all_text = [ int(L.strip("\n").split(",")[1]) for L in file.readlines()]

print(all_text)
all_text = numpy.array(all_text)
print(all_text.sum())