#  Adding Linked list
import math


num_set_1 = [50,1,7]
num_set_2 = [7,1,5]
# expected answer will sum_set = [1,6,13] => [13,6,1]
sum_set =[]
total=0
in_hand_value=0
for i in range(len(num_set_1)) or range(len(num_set_2)) :
    if num_set_1[i] + num_set_2[i] > 9:
        if i == (len(num_set_1)-1):
            sum_set.append(((num_set_1[i]+ num_set_2[i])) + in_hand_value)
        else:
            if num_set_1[i] + num_set_2[i] + in_hand_value >9:
                sum_set.append(((num_set_1[i]+ num_set_2[i] + in_hand_value)%10))
                in_hand_value=math.floor((num_set_1[i]+ num_set_2[i] + in_hand_value)/10)
            else:
                sum_set.append(((num_set_1[i]+ num_set_2[i])%10) + in_hand_value)
                in_hand_value = math.floor((num_set_1[i]+ num_set_2[i])/10)

    else:
        if num_set_1[i] + num_set_2[i] + in_hand_value >9:
            sum_set.append(((num_set_1[i]+ num_set_2[i] + in_hand_value)%10))
            in_hand_value=math.floor((num_set_1[i]+ num_set_2[i] + in_hand_value)/10)
        else:
            sum_set.append(num_set_1[i] + num_set_2[i] + in_hand_value)
            in_hand_value=math.floor((num_set_1[i]+ num_set_2[i] + in_hand_value)/10)
            print('in_hand_value',in_hand_value)

    total = total + num_set_2[i] + num_set_1[i]
print(sum_set[::-1])
#  output [12,7,7] what was expected
print(total)

