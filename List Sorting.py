# This will sort lists that are either integer or string

def sortDescending(intList):
    newSortedList = sorted(intList, key=int, reverse=True)
    return newSortedList
def sortAscending(intList):    
    newSortedList = sorted(intList, key=int, reverse=False)
    return newSortedList
def sortDescending(strList):
    newSortedList = sorted(strList, key=str, reverse=True)
    return newSortedList
def sortAscending(strList):    
    newSortedList = sorted(strList, key=str, reverse=False)
    return newSortedList
    
def main():
    typeOfList = input("Does your list have integers or strings? ")
    
    if typeOfList == 'integers':
        n = int(input("Enter the number of elements in your list: "))
    
        userList = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
        
        print("\nUser's List: ", userList)

        print(f'Your list sorted in descending order is: {sortDescending(userList)}')
        print(f'Your list sorted in ascending order is: {sortAscending(userList)}')
    
    if typeOfList == 'strings':
        userList = list(map(str,input("\nEnter the strings : ").split()))
    
        print("\nUser's List: ", userList)

        print(f'Your list sorted in descending order is: {sortDescending(userList)}')
        print(f'Your list sorted in ascending order is: {sortAscending(userList)}')

def testingStrings():
    assert sortDescending(['abc', 'cde', 'zef']) == ['zef', 'cde', 'abc'], "Should be ['zef', 'cde', 'abc']"
    assert sortAscending(['abc', 'cde', 'zef']) == ['abc', 'cde', 'zef'], "Should be ['abc', 'cde', 'zef']"
    assert sortDescending(['abc', 'abcd', 'abbc']) == ['abcd', 'abc', 'abbc'], "Should be ['abcd', 'abc', 'abbc']"
    assert sortAscending(['abc', 'abcd', 'abbc']) == ['abbc', 'abc', 'abcd'], "Should be ['abbc', 'abc', 'abcd']"
def testingIntegers():
    assert sortDescending([1, 1, 1]) == [1, 1, 1], "Should be [1, 1, 1]"
    assert sortAscending([1, 1, 1]) == [1, 1, 1], "Should be [1, 1, 1]"
    assert sortDescending([1, 0, 0]) == [1, 0, 0], "Should be [0, 0, 0]"
    assert sortAscending([1, 0, 0]) == [0, 0, 1], "Should be [0, 0, 1]"
    assert sortDescending([-1, 0, 10000000]) == [10000000, 0, -1], "Should be [10000000, 0, -1]"
    assert sortAscending([-1, 0, 10000000]) == [-1, 0, 10000000], "Should be [-1, 0, 10000000]"

#testingStrings()
#testingIntegers()
main()