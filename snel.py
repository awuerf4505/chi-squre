import random

    
def counts(text):
    array = [0] * 127

    for c in text:
        n = ord(c)
        array[n] += 1

    array = array[32:127]
    return array
def generate_random_text(num_chars):
    text = ""

    for i in range(num_chars):
        r = random.randint(32, 126)
        text += chr(r)
    
    return text


def average(array):
    a = len(array)
    return sum(array)/a

    

def chi_square(array):
    a = average(array)
    X = 0
    
    for n in array:
        X += ((n-a)**2)/(a)
    return X


with open('new_file.txt', 'w') as f:
    f.write(generate_random_text(15000))
    
with open('new_file.txt', 'r') as f:
    contents = f.read()
    array = counts(contents)

print(chi_square(array))
#lowest = 77 highest = 127

with open('actual_words.txt', 'w') as f:
    f.write(generate_random_text(14000))
    f.write("This is random text.Attach a document in which you describe what you have accomplished on the character distributions assignment. You should be very specific. Describe functions you have written and results you have obtained. Include sample code to supplement your decisions. Change code to a monospace font such as Courier or Consolas to make your code easier to read.It is okay if you haven't completed all tasks on the assignment. If that is the case, then you should also describe in detail things that you have tried but don't work. Include sample code to supplement your decisions. Change code to a monospace font such as Courier or Consolas to make your code easier to read. Create a Python program that generates a text file consisting of 15000 random characters from the set of ASCII values from 32 to 126.")
            
with open('actual_words.txt', 'r') as f:
    contents = f.read()
    print(len(contents))
    second_array = counts(contents)
print(chi_square(second_array))

with open('all_words.txt', 'r') as f:
    contents = f.read()
    third_array = counts(contents)
print(chi_square(third_array))
