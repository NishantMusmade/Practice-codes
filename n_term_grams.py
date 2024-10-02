# The term N-gram refers to all possible substrings of length N and formed using consecutive letters contained in a string. Given a string S and an integer N, 
# find the most frequent N-gram and the number of time appears in S. If there is more than one N-gram with the same frequency, print the first one that appears in

#sample input: banana 3
#output: ana 2

#sample input: isamohanaismohanamoh 3
#output: moh 3 

def frequent_n_gram(input_string,n_terms):
    n_grams = {}
    n = 3
    str_len = len(input_string)
    for i in range((str_len)-n+1):
        n_gram = input_string[i:n]
        if n_gram in n_grams:
            n_grams[n_gram] += 1
        else:
            n_grams[n_gram] = 1
        n = n+1
    max = 0
    n_gram = ''
    for key,value in n_grams.items():
        if value>max:
            max = value
            n_gram = key

    print(n_gram,max)






input_string = 'banana'

n = 3

frequent_n_gram(input_string,n)