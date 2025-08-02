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
            #key, value = parts[0].split('=')
            key1, value1 = parts[1].split('=')
            key2, value2 = parts[2].split('=')
            key3, value3 = parts[3].split('=')
            key4, value4 = parts[4].split('=')
            key5, value5 = parts[5].split('=')
            key6, value6 = parts[6].split('=')
            new_value = change_format(increment) #we can change the number here for furture usage
            increment = int(new_value)
            print("increment value is ",increment)
            string_format = new_value[0:2]+','+new_value[2:4]+':'+new_value[4:6]+':'+new_value[6:8]
            parts[0] = f'{string_format}'
            parts[1] = f'{value1}'
            parts[2] = f'{value2}'
            parts[3] = f'{value3}'
            parts[4] = f'{value4}'
            parts[5] = f'{value5}'
            parts[6] = f'{value6}'

            
            new_line = ','.join(parts)
            new_line = new_line.rstrip(',') + '\n'

            file.write(new_line)

input_file = 'C:/Users/mcc/Desktop/Internship/file_combine_test/combined_output_md13.txt'
output_file = 'C:/Users/mcc/Desktop/Internship/file_combine_test/modified_data_md13.txt'
increment = int(input("Please enter the time we start........"))

change_first_data(input_file,output_file,increment)