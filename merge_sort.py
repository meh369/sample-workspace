class MergeSort:
    '''Takes user args such as len of list and each of the elements to be sorted'''

    def __init__(self):
        self.l = []
        self.n = int(input("enter a number of elements in list: "))
        

    def feedback_call(self):
        '''Populate list with raw inputs'''
        
        for i in range(self.n):
            temp = int(input('Enter Element' + str(i + 1) + ': '))
            self.l += [temp]
        return self.l
    
    def merge_sort(self, user_input_list):
        '''Call our algo which takes a mid point to and partition them into two sep lists'''
        # mid-point = (length-1)/ 2
        mid = int( (len(user_input_list) - 1)/2 )
        # check if length is greater than (mid + 2), index starts with value zero 
        if len(user_input_list) > 2:
            # partition into two parts (a, right)
            left = self.merge_sort(user_input_list[0:mid])
            right = self.merge_sort(user_input_list[mid:len(user_input_list)])
        # else check if its only 2 element list
        elif len(user_input_list) == 2:
            left = [user_input_list[0]]
            right = [user_input_list[1]]
        else:
            return user_input_list

        # merge in a new list
        i = 0
        j = 0
        new = []
        # Simple checks 
        while (i!= len(left) or j != len(right)):

            if i < len(left) and j < len(right):           
                # Sort comprison and append plus init index counter 
                if left[i] < right[j]:
                    new += [left[i]]
                    i += 1
                else:
                    new +=[right[j]]
                    j += 1
            # if i counter reaches len of left and j doesnt then add jth element      
            elif i == len(left) and j != len(right):
                new += [right[j]]
                j += 1
            # if j counter reaches len of right and i doesnt then add ith element
            elif j == len(right) and i != len(left):
                new += [left[i]]
                i += 1

            else:
                break

        return new


if __name__ == "__main__":
    merge_sort = MergeSort()
    callback = merge_sort.feedback_call()
    print(merge_sort.merge_sort(callback))
