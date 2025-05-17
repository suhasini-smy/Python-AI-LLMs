def outer_function():
   def inner_function():
       print('This is the inner function')
   return inner_function
function = outer_function()
function()
