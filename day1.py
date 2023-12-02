numbers =['one','two','three','four','five','six','seven','eight','nine']

total = 0

with open('input.txt','r') as f:
    line = f.readline()
    while line != '':

        word_index = len(line)  # start with value above range
        for index in range(9):
            found_index = line.find(numbers[index])
            if found_index != -1 and found_index < word_index:  #if number text is found

                word_index = found_index                        #note where it was found in text
                word_value = index                              #word_value = index in number[], one less than actual value
                # print(numbers[found_index])


        for char in range(len(line)-1):
            if line[char].isdigit():
                if word_index < char and word_index != len(line):  #did text or digit come first?
                    value = (word_value + 1) * 10
                else:
                    value = int(line[char]) * 10
                break

        word_index = -1
        for index in range(9):
            found_index = line.rfind(numbers[index])  #find first text word from end of input string
            # print(found_index)
            if found_index != -1 and found_index > word_index:
                word_index = found_index
                word_value = index
                # print(found_index)

        for char in range(len(line)-1, -1, -1):
            if line[char].isdigit():
                if word_index > char and word_index != -1:   #see if word or digit came first by checking index of first spotted
                    value += (word_value + 1)
                else:
                    value += int(line[char])
                break

        total += value
        print(f'{line}:{value}')

        line = f.readline()

print(f'Total = {total}')
