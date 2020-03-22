class PalindromeClass:

    def __init__(self, num):
        self.num = num

    def check_palindrome_number(self):
        temp = self.num
        reverse = 0

        while temp > 0:
            tail = temp % 10
            reverse = (reverse * 10) + tail
            temp = int(temp / 10)

        if reverse == self.num:
            print('palindrome')
        else:
            print('not palindrome')


palindrome_obj = PalindromeClass(123)
palindrome_obj.check_palindrome_number()
