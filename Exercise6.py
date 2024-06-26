class Library:
    def __init__(self, n):
        self.books = n
        self.no_of_books = len(n)
    def intel_on_books(self):
        print(f'{self.no_of_books} number of books are present which are {self.books}')
# book=input([])
mylib = Library(['wonka', 'hp 1', 'hp 2', 'RichPoor'])
print('\n\n')
mylib.intel_on_books()
print('\n')
a=input('do you want to add a book yes or no (one at a time) = ',)

if(a=='no'):
    print('ok fine')
if(a=='yes'):
    b=input('enter ther name of the book you wanna add = ')
    mylib = Library(['wonka', 'hp 1', 'hp 2', 'RichPoor',b])
    print('Hence the updated list is =\n\n')
    mylib.intel_on_books()