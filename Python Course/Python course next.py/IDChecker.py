def check_id_valid(id_number: str) -> bool:
    """This function checks if the ID given is valid, based apon the instructions I was given.
    The ID must have 9 digits, then for every number that's located in a even index (1-9) we multiple that number by 2, as for the numbers in the odd indexs we keep them unchanged.
    after that we check for every number that's bigger than 9. If it's bigger than 9 we add its digits to create a new number that will replace it
    After all this we add all of the digits together and if we get a number that's divisible by 10, its a valid ID
    var: total_sum - stores the sum of all the final digits
    var: id_number - gets changed along the way, first we make sure its a string, then we make it a list with the neccery changes, as we don't convert numbers that are bigger than 9 here, we just do it when we about to sum them up
    r : returns a boolean experssion 
    """
    id_number = str(id_number)
    id_number = [int(id_number[index-1]) if index % 2 != 0 else int(
        id_number[index-1])*2 for index in range(1, len(id_number)+1)]  # creates a list with the needed changes
    total_sum = 0
    for number in id_number:
        if number > 9:
            number = sum(int(digit)
                         for digit in str(number))
            total_sum += number
        else:
            total_sum += number

    if total_sum % 10 == 0:
        return True
    return False


class IDIterator():
    """This class represents an iterator"""

    def __init__(self, id=100000000):
        self._id = id

    def __iter__(self):
        return self

    def __next__(self):
        self._id += 1
        if self._id == 999999999:
            raise StopIteration
        if check_id_valid(self._id):
            return self._id


def id_gen(id):
    while id != 999999999:
        id += 1
        if check_id_valid(id):
            yield id


def main():
    id = int(input("Enter ID "))
    engine = input("Generator or Iterator? (gen/it)? ").lower()
    count = 0
    # ----------------------------------------------------------------
    # The iterator version
    if engine == "it":
        id_iter = IDIterator(id)
        for id in id_iter:  # prints only 10 valid ID's after and not including the starting ID that the user gave, also it doesn't matter if the ID that the user gave is valid or not , as long as the number given is 9 digits
            if id == None:
                pass
            else:
                print(id)
                count += 1
            if count == 10:
                break
    # --------------
    # the generator version
    elif engine == 'gen':
        for ids in id_gen(id):
            if count == 10:
                break
            print(ids)
            count += 1
    else:
        print("invalid input")


def id_gen_check():  # to check if the id gen version works
    input_ID = int(input("Enter ID "))
    for id in id_gen(input_ID):
        print(id)


if __name__ == "__main__":
    main()
