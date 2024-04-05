def licznik():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment
