def fibo(n, db):

    if n <= 1:
        db[n] = n
        # print(db)
        return n

    if db[n] != -1 :  # check if the value is computed and stored # if not -1 ==> means value is computed prior and stored already -->
        return db[n]     # don't again do function call and compute --> just return that value

    db[n] = fibo(n-2,db) + fibo(n-1,db) # first compute the subproblems and then store the value
    
    # print(db)

    return db[n] # return the value of the particular position



n = int(input("give the position: "))

db = [-1]*(n+1) # create an array of (n+1) (as index from 0) with values to be -1

# print(f"intial: {db}")
print(fibo(n, db))

