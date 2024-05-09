#Uses string slicing to check if number is green
def is_green(num):
    squared = str(num * num)
    return squared.endswith(str(num))

#Find the nth green number via a generator
def green(n):
    #initialize some variables
    found = 0
    num = 1
    step = 10
    #Tracks seen numbers to avoid duplicates
    seen = set() 

    #loop until it finds the nth green number
    while found < n:
        #check if it is green to increase the number of found items
        if num not in seen and is_green(num):
            seen.add(num)
            found += 1
            yield num
            #reset step when green number found
            step = 10
        #increment num to look at the next number
        num += 1
        
        #Checks if the next 10 numbers are in the seen set to skip ahead
        while num in seen:
            num += step
            
        #If all numbers in next step range are seen, increase step size
        while all(num + i in seen for i in range(1, step)):
            step *= 10

#Tests if the two numbers are equal
def test_green(n1, n2):
    #expects n1 to be a value yielded by a generator
    *_, last = n1
    return last == n2

# Test cases
print(test_green(green(2), 5)) # Should print True
print(test_green(green(3), 6)) # Should print True
print(test_green(green(4), 25)) # Should print True
print(test_green(green(10), 36)) # Should print False
print(test_green(green(12), 2890625)) # Should print True
print(test_green(green(13), 7109376)) # Should print True
print(test_green(green(100), 6188999442576576769103890995893380022607743740081787109376)) # Should print True
print(test_green(green(110), 9580863811000557423423230896109004106619977392256259918212890625)) # Should print True
