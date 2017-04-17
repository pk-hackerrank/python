import textwrap
# textwrap.wrap() The wrap() function wraps a single paragraph in text (a string) 
# so that every line is width characters long at most. 

# The fill() function wraps a single paragraph in text and returns 
# a single string containing the wrapped paragraph.

def wrap(string, max_width):
    return textwrap.fill(string, max_width)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)