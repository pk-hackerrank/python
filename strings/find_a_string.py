def count_substring(string, sub_string):
    # there are two ways of acheieving it, as usual one we will put in comments.
    # 1st method as suggested in concept of question
    count = 0
    #sub_string_len =len(sub_string) # Finding length of sub_string
    #for i in range(0, len(string)): # Looping through string from 0 to len of string.
        # Retrieve substring of from index (i) to len of sub string and comparing with actual sub_string 
    #    if string[i:i+sub_string_len] == sub_string: 
    #        count += 1
    # 2nd Method, this method is more efficient, since the number of loops will be less. Since the index is dynamic.
    index_of_sub_string =  string.find(sub_string) # Get the first index of substring
    while index_of_sub_string != -1: # Loop through until the substring is not found
        count +=1 
        index_of_sub_string = string.find(sub_string, index_of_sub_string+1) # increment the index
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)