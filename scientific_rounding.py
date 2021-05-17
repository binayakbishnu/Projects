def rounding(number, places = 0):
    number_ = str(number)
    # number_ = [i for i in number_]
    last_digit = int(number_[-1])
    
    dec_place = number_.index(".")
    to_be_removed = int(number_[dec_place+places+1])
    
    if to_be_removed < 5:
        new_number = number_[0:dec_place+places+1]
        print(new_number)
    elif to_be_removed > 5:
        new_number = number_[0:dec_place+places]
        new_number += str(int(number_[dec_place+places])+1)
        print(new_number)
    elif to_be_removed == 5:
        previous = int(number_[dec_place+places])
        if previous % 2 == 0:
            new_number = number_[0:dec_place+places+1]
            print(new_number)
        else:
            new_number = number_[0:dec_place+places]
            new_number += str(int(number_[dec_place+places])+1)
            print(new_number)



i=0
while(i<8):
    number, places = input("Enter number<space>places: ").split()
    rounding(float(number),int(places))
    i+=1
    