class Armstrong:

    def __init__(self, num):
        self.num = num

    def check_armstrong(self):
        temp_res = self.num
        sum_ = 0

        while temp_res > 0:
            digits = temp_res % 10
            cube = digits * digits * digits
            sum_ = sum_ + cube
            temp_res = int(temp_res / 10)

        if sum_ == self.num:
            print("Armstrong")
        else:
            print("Not Armstrong")


value = int(input("Enter the number to check Armstrong : \n"))
obj_ = Armstrong(value)
obj_.check_armstrong()
