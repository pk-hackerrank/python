list_to_handle=[]
input_list=[]
def do_insert(given_list):
    global list_to_handle
    list_to_handle.insert(int(given_list[1]), int(given_list[2]))

def print_list(given_list):
    global list_to_handle
    print(list_to_handle)

def remove_element(given_list):
    global list_to_handle
    list_to_handle.remove(int(given_list[1]))

def append_element(given_list):
    global list_to_handle
    list_to_handle.append(int(given_list[1]))

def sort_the_list(given_list):
    global list_to_handle
    list_to_handle.sort()

def pop_element(given_list):
    global list_to_handle
    list_to_handle.pop()

def reverse_the_list(given_list):
    global list_to_handle
    list_to_handle.reverse()    

input_dictionary = {
    'insert': do_insert,
    'print': print_list,
    'remove': remove_element,
    'append': append_element,
    'sort': sort_the_list,
    'pop': pop_element,
    'reverse': reverse_the_list
}
if __name__ == '__main__':
    N = int(input())
    for i in range(0,N,1):
        given_input = input()
        input_str_to_list = given_input.split(" ")
        input_list.append(input_str_to_list)
    for i in range(0,N,1):
        input_dictionary[input_list[i][0]](input_list[i])
    