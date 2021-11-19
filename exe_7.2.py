# counting the average of a floating value  from mbox-short.txt file

fname = input("Enter the file name: ")

fopen = open(fname, "r")
count, number = 0, 0
for line in fopen:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        lis= line.split()
        number+= float(lis[1])
        count+= 1

avg = number/count
print("Average spam confidence: ",avg)