def encode(message):
    encoded_message =""
    i = 0
    while (i <=len(message)-1):
        count = 1
        char = message[i]
        j = i
        while(j < len(message)-1):
            if (message[j]== message[j+1]):
                count=count+1
                j = j+1
            else:
                break
        i = j+1
    encoded_message = encoded_message+char+str(count)

    return encoded_message

encoded_message = encode("AAAAABBBBB")
print(encoded_message)
