# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


from click import open_file


def read_file_content(filename):
    #[assignment] Add your code here
 f = open(filename, "r")
 file = f.read
 return file


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    count = dict()
    words = str.split(text)

    for word in words:
        if word in count:
            count [words] += 1
        else:
            count[words] = 1
