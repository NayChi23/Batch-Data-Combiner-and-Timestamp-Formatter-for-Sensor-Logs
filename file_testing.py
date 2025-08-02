def change_format(number):
    s =[]
    s.append(int(number%100))
    s.append(int((number/100)%100))
    s.append(int((number/10000)%100))
    s.append(int(number/1000000))
    #print(s)
    if(s[0] == 59):
        s[0] = 0
        if(s[1] == 59):
            s[1] = 0
            if(s[2] == 23):
                s[2] = 0
                if(s[3] == 30):
                    s[3] = 1
                else:
                    s[3] +=1
            else:
                s[2] +=1
        else:
            s[1] +=1
    else:
        s[0] +=1
   # print(s)
    data = str(s[0]+(s[1]*100)+(s[2]*10000)+(s[3]*1000000))
    #print("the data is ",data)
    if(len(data) == 7):
        string_res = '0'+ data
    else:
        string_res = data
    print(string_res)
    return string_res

def change_first_data(input_file,output_file,increment):
    with open(input_file,'r') as file:
        lines = file.readlines()
    
    with open(output_file,'w') as file:
        for line in lines:
            parts = line.strip().split(',')
            key, value = parts[0].split('=')
            new_value = change_format(increment) #we can change the number here for furture usage
            increment = int(new_value)
            print("increment value is ",increment)
            parts[0] = f'{key}={new_value}'
            new_line = ','.join(parts)+'\n'

            file.write(new_line)

input_file = 'C:/Users/mcc/Desktop/Internship/file_combine_test/combined_output_md1.txt'
output_file = 'C:/Users/mcc/Desktop/Internship/file_combine_test/modified_data_md1.txt'
increment = int(input("Please enter the time we start........"))

change_first_data(input_file,output_file,increment)