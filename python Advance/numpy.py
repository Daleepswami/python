

import numpy as np
x = np.array([1,2,3])
print(x,type(x))

     

sum = 0
a = 0
b = 1
count = 0

while count < 10:          # 10 terms
    print(a, end=" ")

    c = sum                # (aapka line)
    sum = a + b            # next number
    a = b                  # a ko b ki value de dete hain
    b = sum                # b ko next number de dete hain

    count += 1

     
numpy is a fundametal library for numerical computing :numpy is shorthand for numberical python

efficeint in multi dimensional array a large colletion of high level mathematical function


#creating an array with the help of list
import numpy as np
li = [1,2,3]
x =np.array(li)
print(type(x))


     

# create an array and insert 1 - 100
# created 1d array using the list comprehsion
li = [x for x in range(1, 101)]
b = np.array(li)
# for checking the dimension of the array we use (.ndim)
b.ndim
     

# [1,2,3] rows are this 
#[4,5,6]
#[7,8,9]

#colums are [1,4,7] ,[4,5,6] , [7,8,9]

# created 2d array using the 2nd list
#matrix -> (3,3) -> column 3
li = [[1,2,3],[4,5,6],[7,8,9]]
c =np.array(li)

# checkin the shape of the data (.shape)

print(c.shape)

# checking the dimension of the data (.ndim)
print(c.ndim)


# to check ki ktine elements hai (.size)  by mulitipy row * col

print("to check the size of the ",c.size)

     

# to create the matix of 5*5 shape,dimesion and size

li = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

a = np.array(li)
print(a.shape)
print(a.ndim)
print(c.size)

     

#this function is responsible for the creating an nd array of ones - means isme 1 is set to all elemet postion to the matrix
# in this we give row and colums .ones(row,col)

# for explicitly converting the data type of the matrix we use  dtype as an argumet -> dtype = int

np.ones((3,3), dtype= int)

     

# this function is responsible for intiablizing the values 0 to all the postion into the matrix
np.zeros((3,3), dtype = int)
     

# arange act as range function  used to give an range -> arange(start->inclusive,end->exclusive,steps -> to jump the values of the range)
a = np.arange(1,101,2)
print(a)
a.ndim

# to initalize the matrix or conver the matric (.reshape) is used to reshape the value the array into this we would pass the row number and columns number
# the rows and colums product {should be the total number of element} -> (.size)
r = a.reshape(5,10)
print(a.size)
print(r.size)

     

import numpy as np
x = np.linspace(10, 20, 6).reshape(3, 2)

# 10, 10 + 2.5
# (20 - 10) / (6 - 1) -> 10/5 -> 2.0
# max - min / (n-1) -> space
x = np.arange(1, 13).reshape(3, 4)

     

a = np.array([1,2,3,4,5])
a[0]

# accessing the elements using the indices of the array is known indexing
# isme zero (0) based indexing

# array_iname[index]
a[-1]
a[-2]
for i in range(1,len(a)+1):
    print(a[i*-1])
print()
print()
for i in range(1,len(a)+1):
    print(a[-i])
# slicing is used to find or extract the subarray from the goiven array and steps
# [start,end,steps]
# by default the starting index is  0 
# by default the ending len(array) - 1
# step by default  -> 1
print(a[::2])
print(a[1:4])
 
  
# generate an array  using the arange function 1,100 using 3 steps print all the elemts 
alpha = np.arange(1,101,3)
print(alpha)


# using slicig reversing the array

print(a[::-1])




     

matrix = np.arange(1,13).reshape(3,4)

print(matrix[0][0])
#matrix ->  [rows][elemts index]

# print all the elements of the matrix
for i in range(0,3):
    for j in range(0,4): 
        print(matrix[i][j] ,end ='  ')
    print()    

     

# study slicing on the matirces  and vecotrization

     

# what is matrix , why do we use matrix # matrix opertion 
# what is the use of matrix operation into the machine learning



     

# in matrix  slicing we use the slicing the extract the sub matrix
# matrix_name [slicing_row, slicing_col ]
matrix = np.arange(1,13).reshape(3,4)
print(matrix)
     

matrix[0, : 1]
# finding the first 2 col of the matrix
# matrix[:] -> it will access whole rows
# matrix[:,0:2] -> this will give the first two colums


matrix[:, 0 :2]

     

matrix[1: ,2:]
     

#how to generate random number
# un numpy the random module is used to generate the random numbers
# randint -> it generate an array in given range,into which we can give number of elements
# into this the start is inclusive
# end is exclusive
import numpy as np
###                   start, end,  kitne chiye
x = np.random.randint(1, 2000,3000)
print(x)
np.random.seed
     

np.random.seed(32)
np.random.randint(1,11,10)


     

#np.random.rand is used to genrate the values between 0 to 1
#into this function or mthod we pass the number or elements which we want to generate

np.random.rand(40)
     

# mean
# li = [1,2,3,4]

# sum(li)/len(li)  this conusme more time,memory 


s = np.array([1,2,3,4])
np.mean(s)

     

import numpy as np
x = np.random.randint(1, 10, 50)
np.median(x)


     

n = np.array([1,2,3,4,5,6])

np.median(n)
     

#flatten method is used to put all the elements in one array
m = np.random.randint(1,10,12).reshape(3,4)
print(m)
flatten_matrix = m.flatten()
print(flatten_matrix)
     

#generate a  matrix using the random module randint ,last colums
# 2d element -> mean -> flatten ->mean

new = np.random.randint(1,10,10).reshape(2,5)
print(new)
print(new[:,-2:])
m = new.flatten()
print(np.mean(m))
     

# diffenece between the flatten and ravel
# flatten creates a copy of the original matrix into the array
# whenever we change any value of the new flattend array it would not affect on the original
# ravel creates a view of original matrix and into the whenever we change into the new
# array ir will affect the original matrix
m = new.ravel()
m[0] = 100
print('the change done in oroginal array by ravel',new)
f = new.flatten()
f[0] = 200
print('flatten make a copy',f)
print('the orginal array does not affect',m)

     

# fancing indexing : it is a techincure in programming ,especially in numpy that allows you to select multiple elements from an array at once using a list
# or array of indices
#instemd of packing elemet one by one with simple indexing
#print(arr[0])
#print(arr[2])
import numpy as np
arr = np.arange(10)
indices = [1,4,7]
arr1 = []
for i in indices:
    arr1.append(arr[i])
     

np.array(arr1)

     

arr = np.arange(1,11)
view_arr = arr.view()

view_arr[0] = 100
#view is a method which copies the reference/memory address of the original arra/object so any changes in the view will affect the orginal array
#if we change anthing into the duplicate array it will reflect into the original array
# here we are changing the first element of the duplicated arry 
     

# this copy() method is used to copy the object and create actual same object 
# at different location 
# into this the original object is NOT affected when we change the copied/duplicated array 
import numpy as np
arr = np.arange(1,11)
view_arr = arr.view()

view_arr[0] = 100
copy_arr = arr.copy()
print(copy_arr)
copy_arr[1] = 20
print(copy_arr)
print(arr)
# copy() creates a true copy, changes in copy_arr do not affect arr
     


     

#np .where is function powerful tool for conditional selection and replacement of elements within numpy array.if identifies elements that meet a specifice
# condition and return either the indices of those elements or a new array 

np.where(arr > 5)
# np.where fucntion or method is used to find the indices on the second on the basis of 
# some condition
np. where(arr>5 , 'high','low')


     

# verical stacking is used to stack the array into the stack format
# vertically.
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([7,8,9])
np.vstack([arr1,arr2,arr3])

     

# take an array ranging between 10 and 35 with step 20, label values less than 18 as 'child' and greater or equal as 'adult'
arr = np.random.randint(10, 35, 20)
print(arr)
print(np.where(arr >= 18, 'adult', 'child'))

     

#horigonatal stacking
matrix = np.arange(1,13).reshape(3,4)
arr = np.array([1,2,3]).reshape(3,1)

print(matrix)
print(arr)

print(np.hstack([matrix,arr]))
     

# here we are performin the fancy indexing 
# we give the multiple indices of th
     

x = np.array([[1,2,3],[4,5,6]])
print(x,type(x))
     

x = np.array([[[1,2,3],[4,5,6]]])
print(type(x))
     

x.ndim
     

c = np.zeros((4,5))
# tuple(row, column)
print(c)
     

c.ndim
     

c = np.ones((5,6))
print(c)
     

x = np.ones((5,6), dtype = int) 
print(x)
     

np.eye(3,3)
     

x = np.arange(1,13)
print(x)
     

x.reshape(3,4)
     

#peromrm linespce
np.linspace(10, 20, 5)
     

st = 'False'
bool(st)
     

a = np.linspace(10,20,12).reshape(3,4)
print(a)
     

a = a+1
print(a)
     

c = np.array([1,2,3,4,5])
print(c**2)
     

a= np.array([1,2,3,4,5])
b = np.array([6,7,8,9,1])
c = a+b
print(c)
     

#20,100 matrix create shape 
a = np.arange(20,100)
a = a.reshape(40,2)
print(a)
     

import numpy as np
arr = np.array([1,2,3,4])

     

# this are scaller opeation it can be /*-+
print(arr + 4)
print(arr * 4)


     

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
new_arr = arr1+ arr2
print(new_arr)
     

matrix = np.arange(1,13).reshape(3,4)
matrix
     

matrix + 1
     

# how to add an array  in existing matrix
# addition is performing on basis of axix = 0, it means all the elements of the array is added with each row of the matrix


matrix + arr
     

arr.shape
     

arr1 = np.array([1,2,3])

matrix + arr1
     

# braoadcasting in numpy is a powefull mechanish that allows artiemetic oepration on array of differenct shapes and sizes
# isme dono matrix k ek dimension match honi chiye jese ki row colums me 
arr1 = arr1.reshape(3,1)
matrix + arr1
     

# according to the rule broadcasting the dimension of matrices must have the same dimension
mat1 = np.arange(1,10).reshape(3,3)
mat2 = np.arange(10,19).reshape(3,3)
print(mat1, mat2)
mat1 + mat2
     


     
