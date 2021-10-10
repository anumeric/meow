import random
import string

class TestCases():
    def __init__(self):
        self.names = list(string.ascii_lowercase)[:8]
        self.heights = [random.randint(10, 100) for _ in range(8)]
        self.weights = [random.randint(100, 200) for _ in range(8)]

# type validation to prevent injection   
def isInputValid(search_criteria,paramater,symbol):
    valid_search_criteria = {"weight","height"}
    valid_symbol = {"<",">","="}
    if (search_criteria not in valid_search_criteria) or (symbol not in valid_symbol) or (type(paramater) is not int):
        return False
    return True

class Cat():
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
      
def searchCats(search_criteria,paramater,symbol):
    search_criteria = search_criteria.lower()
    res = []
    if isInputValid(search_criteria,paramater,symbol):
        for cat in cats:
            command = "if cat."+ search_criteria + symbol + str(paramater) + ": res.append(cat.name)"   
            exec(command)
    return res

if __name__ == "__main__":
    
    # Generate Test Cases 
    test_cases = TestCases()
    print(test_cases.names)
    print(test_cases.heights)
    print(test_cases.weights)

    cats = [Cat(test_cases.names[i],test_cases.heights[i],test_cases.weights[i]) for i in range(len(test_cases.names))]
    res = searchCats("WEIGHT",121,"<")
    print(res)


















