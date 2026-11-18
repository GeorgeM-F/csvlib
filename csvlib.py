# Returns the raw content of the file "a" as a simple string.
def as_string(a):
    with open(a, 'r') as file: t=file.read()   # open argument file, define "t" as a string corresponding to its content, then close the file
    return t

# Returns the content of the file "a" as a 2-dimensional list where each list represents a row.
def as_rowlist(a):
    stringified=as_string(a)   # convert argument to string
    if not stringified[-1]=="\n":   # add final newline if not present (necessary to avoid missing rows)
        stringified=stringified+"\n"
    res=list()   # initialize result to return
    currow=list()   # initialize first row
    curval=str()   # initialize first value
    for i in stringified:
        if i==",":   # at any comma, add the finished value to the current row, then initialize a new one
            currow.append(curval)
            curval=str()
        elif i=="\n":   # at any newline, add the finished value to the current row, add the finished row, then initialize new ones of both
            currow.append(curval)
            res.append(currow)
            curval=str()
            currow=list()
        else:   # in any other case, add that character to the current value
            curval=curval+i
    return res

# Same as as_rowlist(), but without including the 1st row.
def as_topclipped_rowlist(a):
    return as_rowlist(a)[1:]

# Same as as_rowlist(), but without including the 1st column.
def as_sideclipped_rowlist(a):
    res=list()   # initialize result
    for i in as_rowlist(a):
        res.append(i[1:])
    return res

# Same as as_rowlist(a), but without including neither the 1st row nor the 1st column.
def as_biclipped_rowlist(a):
    res=list()
    for i in as_rowlist(a):
        res.append(i[1:])
    return res[1:]

# test trial code:
# print(as_biclipped_rowlist('test.csv'))

