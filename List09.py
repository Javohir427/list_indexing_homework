def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i = 0
    while i<len(list1):
        if list1[i]==list1[0]:
            x= True
        else :
            return False
        i+=1
    return x

print(main([0, 0, 0, 0, 0])) 

