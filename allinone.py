
products = {} # creating a empty dictionary
customers = {}# creating a empty dictionary
sales = {}    # create a dictionary to keep track of sales records

def addproduct():
    
    while True: # keeping looping to add as many products as user wants

        try:    # try this block of code
            code = eval(input('Enter the product code '))   # ask for product id from the user
            if code < 1:                                    # if the product is less then 1
                raise Exception                             # raise exception  
        except:                                             # if try block doesnt execute, if there is some error
            print('Invalid Input! Product Code can only contain digits and should start from 1')  # tell the user that his input is invalid
            continue                                        # continue to first line of loop

        if code in products.keys():                         # if the code Entered by user is already user by some other product
            print('This Product has already been alotted to a Product, please use a different Product Code ') # tell the user to use some different product code
            continue                                        # continue to first line of code
        
        while True:                                         # keeping looping until user Enters correct name 
            product_name = input('Enter the product name ') # ask user for the product name
            if product_name.isalpha():                      # if name contains alphabets
                break                                       # break out of loop (we got the correct name)
            else:                                           # else if product name doesnt contain all alphabets 
                print('Invalid Input! Name can only contain alphabets') # tell the user that his input is invalid
        
        while True:                                         # keeping looping until user Enters correct price 
            try:                                            # try this block of code
                product_price = eval(input('Enter the products price '))    # ask user to Enter the product price
                if product_price < 1:                       # if price Entered by user is less than 15
                    raise Exception                         # raise exception (generate error)
                break                                       # break out of loop ( if correct name is Entered
            except:                                         # if try block doesnt execute, if there is some error
                print('Invalid Input! Price can only contain digits and should start from 1')
        
        while True:
            try:
                quantity = eval(input('Enter the products quantity '))
                if quantity < 1:
                    raise Exception
                break
            except:
                print('Invalid Input! Quantity can only contain digits and should start from 1')

        products[code] = [product_name, product_price, quantity]
        
        check = input('Press 1 to add more products. Press any other key stop adding products ')
        if check != '1':
            break


def viewproduct():
    
    if products:
        print('Product Code\t\t\tProduct Name\t\t\tPrice\t\t\tQuantity')
        for i in products.keys():
            lst = products[i]
            print(i,'\t\t\t', lst[0], '\t\t\t', lst[1], '\t\t\t', lst[2])
    else:
        print('No Products Record found')
   

def editproduct():
    
    if products:

        while True:
            try:
                ask = eval(input('Enter the product code you want to edit '))
                if ask < 1:
                    raise Exception
                break
            except:
                print('Invalid Input, Product Code can only contain digits and should start from 1')

        found = False
        lst = []
        
        for i in products.keys():
            if i == ask:
                lst = products[i]
                found = True
                break

        if found:
            
            while True:   
                
                print("Press 1 to edit name of product\nPress 2 to edit price of product\nPress 3 to edit quantity of product\nPress 4 to stop editing")
                edit = input("Enter corresponding number to edit ")

                if edit == '1':
                    while True:
                        new_name = input("Enter new name of product ")
                        if new_name.isalpha():
                            break
                        else:
                            print('Invalid Input! Name can only contain alphabets')
                    products[ask][0] = new_name
                    print('The Product name has been Changed to ', new_name)

                elif edit == '2':
                   while True:
                       try:
                           new_price = eval(input("Enter new price of product "))
                           if new_price < 1:
                                raise Exception
                           products[ask][1] = new_price
                           break
                       except:
                           print('Price can only contain digits and should start from 1')
                   print('The Price of Product ID : ', ask, ' has been Changed to ', new_price)

                elif edit == '3':
                   while True:
                       try:
                           new_quantity = eval(input("Enter new quantity of product "))
                           if new_quantity < 1:
                                raise Exception
                           products[ask][2] = new_quantity
                           break
                       except:
                           print('Quantity can only contain digits and should start from 1')
                   print('The Quantity of Product ID : ', ask, ' has been Changed to ', new_quantity)
                
                elif edit == '4':
                    break
                
                else:
                    print('Please Enter a Valid Choice')
        else:
            print('Product key not found')

    else:
        print('No products Record is there to be edited')

                   
            
#search
def searchproduct():
    
    if products:
        
        while True:
            try:
                ask = eval(input('Enter the product code you want to search for '))
                if ask < 1:
                    raise Exception
                break
            except:
                print('Invalid Invalid! Product Code can only contain digits and should start from 1')
                

        found = False
        lst = []

        for i in products.keys():
            if i == ask:
                lst = products[i]
                found = True
                break

        if found:
            print('Your Searched Product Code Found')
            print('Product Code\t\t\tProduct Name\t\t\tPrice\t\t\tQuantity')
            print(i,'\t\t\t', lst[0], '\t\t\t', lst[1], '\t\t\t', lst[2])
        
        else:
            print('Your searched code not found')
    
    else:
        print('No products Record is there to be searched for')
    


#delete
def deleteproduct():
    
    if products:
        deleted = False
        
        while True:
            try:
                ask = eval(input('Enter the product code you want to delete '))
                if ask < 1:
                    raise Exception
                break
            except:
                print('Invalid Input! Product Code can only contain digits and should start from 1')

        for i in products.keys():
            if i == ask:
                deleted = True
                del products[i]
                print('product that has key ', i, ' has been deleted')
                break

        if not deleted:
            print('The Code you Entered doesnt match any products')
            
    else:
        print('No products Record is there to be deleted')
 
 
def productmenu():
    
    while True:
        print('\t\tPRODUCT MENU')
        print('Press 1 to Add products \nPress 2 to View products \nPress 3 to Edit products \nPress 4 to Search products \nPress 5 to Delete products \nPress 6 to Exit') # display the available functions     ask = int(input('Enter Corresponding Number to Perform Desired Task ')) # ask user what function he wants to perform
        ask = input("Enter corresponding number to perform desired task ")
        
        if ask == '1':  # if user types 1 
            #record = True
            print('Add product') # tell the user that he is going to add product
            addproduct() # call add function
        
        elif ask == '2': # if user types 2

            print('View product') # tell the user that he is going to view product
            viewproduct()
        
        elif ask == '3': # if user types 3
            
            print('Edit product') # tell the user that he is going to use edit function
            editproduct()
        
        elif ask == '4': # if user types 4
            
            print('Search for product') # tell the user that he is going to use search function
            searchproduct()
        
        elif ask == '5': # if user types 5
            
            print('Delete Customer') # tell the user that he is going to use delete function
            deleteproduct()
        
        elif ask == '6': # if user types 6
            break # exit the program
        
        else: # if user types something that was not expected
            print('Please Enter a valid number') # tell the user that he has to Enter valid number




#-----------------------------------------------------------------------------------------------------------------------------------------------


def addcustomer():
    
    while True:
        try:
            customerid = eval(input('Enter the customer id '))
        except:
            print('Invalid Input! Customer ID can only contain digits and should start from 1')
            break

        if customerid in customers.keys():
            print('This key has already been alotted to a customer, please use a different key ')
            continue
        
        while True:
            try:
                customer_phoneno = int(input('Enter the customer phone_no '))
                break
            except:
                print('Phone Number can only contain digits and should start from 1')

        customer_name = input('Enter the customer name ')
        address = input('Enter the customers address ')
        customers[customerid] = [customer_name, customer_phoneno, address]
        
        check = input('Press 1 to add more customers ')
        if check != '1':
            break



def viewcustomer():
    
    if customers:
        print('customer id\t\tcustomer name\t\tcustomer_phone.no\t\taddress')
        for i in customers.keys():
            lst = customers[i]
            print(i,'\t\t', lst[0], '\t\t', lst[1], '\t\t', lst[2]) 
    else:
        print("record doesnot exist")
        
        
        
def editcustomer():
    
    if customers:
        
        while True:
            try:
                ask = eval(input('Enter the customer id you want to edit '))
                break
            except:
                print('Invalid Input! Customer ID can only contain digits and should start from 1')
        
        found = False
        lst = []
        
        for i in customers.keys():
            if i == ask:
                lst = customers[i]
                found = True
                break
        
        if found:
            while True:
                print("Enter 1 to edit name of customer\nEnter 2 to edit customer_phone.no of customer\nEnter 3 to edit address of customer\nAny other key to go back to main menu")
                edit=input("Enter corresponding number to edit ")
                
                if edit=='1':
                    new_name = input("Enter new name of customer ")
                    customers[ask][0] = new_name
                    print('The Product name has been Changed to ', new_name)
                
                elif edit=='2':
                    new_customer_phoneno=eval(input("Enter new customer_phone.no of customer "))
                    customers[ask][1] = new_customer_phoneno
                    print('The Product name has been Changed to ', new_customer_phoneno)

                elif edit=='3':
                    new_address=input("Enter new address of customer")
                    customers[ask][2] = new_address
                    print('The Product name has been Changed to ', new_address)
                
                else:
                    break
    
    
    else:
        print("Record Doesnot Exist")
        
        
    
        
           
            
#search
def searchcustomer():
    
    if customers:
        while True:
            try:
                ask = eval(input('Enter the customer id you want to search for '))
                break
            except:
                print('Invalid Input! Customer ID can only contain digits and should start from 1')
        
        found = False
        lst = []
        
        for i in customers.keys():
            if i == ask:
                lst = customers[i]
                found = True
                break
        
        if found:
            print('your searched id found')
            print('customer id\t\tcustomer name\t\tcustomer_phone.no\t\tcustomer address')
            print(i,'\t\t', lst[0], '\t\t', lst[1], '\t\t', lst[2])
        
        else:
            print('Your searched id not found')
    
    else:
        print("record does not exist")
        
        
        

#delete
def deletecustomer():
    
    if customers:
        while True:
            try:
                ask = eval(input('Enter the customer id you want to delete '))
                break
            except:
                print('Invalid Input! Customer ID can only contain digits and should start from 1')       
        
        deleted = False
        
        for i in customers.keys():
            if i == ask:
                deleted = True
                del customers[i]
                print('customer that has key ', i, ' has been deleted')
                break

        if not deleted:
            print('The id you Entered doesnt match any customers')
    
    else:
        print("record does not exist")
        
        
        
def customermenu():
    
    while True:
        print('\t\tCUSOMTER MENU')
        print('Press 1 to Add customers \nPress 2 to View customers \nPress 3 to Edit customers \nPress 4 to Search customers \nPress 5 to Delete customers \nPress 6 to Exit') # display the available functions     ask = int(input('Enter Corresponding Number to Perform Desired Task ')) # ask user what function he wants to perform
        ask = input("Enter corresponding number to perform desired task ")
        
        if ask == '1':  # if user types 1 
            #record = True
            print('Add customer') # tell the user that he is going to add customer
            addcustomer() # call add function
        
        elif ask == '2': # if user types 2
            #print(record) # print is the best debugger 
            #if record:
            print('View customer') # tell the user that he is going to view customer
            viewcustomer()
        
        elif ask == '3': # if user types 3
            print('Edit customer') # tell the user that he is going to use edit function
            editcustomer()
        
        elif ask == '4': # if user types 4
            print('Search for customer') # tell the user that he is going to use search function
            searchcustomer()
        
        elif ask == '5': # if user types 5
            print('Delete Customer') # tell the user that he is going to use delete function
            deletecustomer()
        
        elif ask == '6': # if user types 6
            break# exit the program
        
        else: # if user types something that was not expected
            print('Please Enter a valid number') # tell the user that he has to Enter valid number



#--------------------------------------------------------------------------------------------------------------------------------------------------



def addsale(): #defining the function
     
    while True: # keeping looping until user wants
        
        if customers and products: # if customer and product record exists
            total_bill = 0         # set totalbill to zero, total bill for every 
            productdict = {}       # making a dictionary to keep track of products bought by specific customer
            try:                   # try executing the following block of code
                customer_id = eval(input('Enter Customer ID of the customer you are selling product to ')) # asking the user for customer id
            except:                # if there is an error then except block will execute
                print('Invalid Input! Customer ID can only contain digits and should start from 1')            # tell the user that his input is invalid
                continue           # continue to the 1st line of loop

            if customer_id not in customers:        # if customer id Entered by user is not in the customer dictionary
                print('Customer not found, Please Add this Customer First \nPress 1 to Add other Sale Record \nPress any other key to go back to sales menu ') # tell the user that his customer id is not found
                ask = input('')    # ask user what he wants to do
                if ask == '1':     # if user types 1
                    continue       # go back to 1st line of loop (start adding another sales record for some other customer)
                
                else:              # else if user press any other key
                    break          # break out of the main loop
                          
            
            while True:            # loop for keep adding the sales value until it is correct
                try:               # try executing the following block of code
                    salesid = eval(input('Enter Sales Id '))  # ask for sales id
                    if salesid in sales.keys():   # if sales id is already in sales dictionary
                        print('This Sales ID has already been alloted, please add some different ID ')  # tell the user to use a different sales id
                    else:          # else if sales id in already in not in the dictionary
                        break      # break out of loop (stop adding sales id, correct sales id has been Entered)
                except:            # if try block shows an error ( input is not a number )
                    print('Invalid Input! Sales ID can only contain digits and should start from 1') # tell the user that his input is invalid
                


            while True:            # setting an infinite loop so user can keep adding products until he wants to break
                try:               # try executing following block of code
                    product_code= eval(input('Enter Product Code of Product you want to Sell '))        # ask the user for product code he wants to add in sale record
                except:            # if there is error in try block
                    print('Invalid Input! Product Code can only contain digits and should start from 1') # tell the user that his input is invalid
                    continue       # as input is invalid, there is no need to execute next lines of code, go back to first line again

                if product_code not in products:                            # if product is not available 
                    print('This Product is not available, Add this Product First\nPress 1 to add another product\nPress any other key to stop this customer sale') # display user that to this product is not available
                    ask = input('')# ask the user if he wants to add another product or stop this sale
                    if ask == '1': # if user types 1
                        continue   # go to first line of loop ( add product again)
                    
                    else:          # else if user presses any other key
                        salesmenu()# go to sales menu by calling sales menu() function 
                
                elif products[product_code][2] == 0:
                    print('This Product is out of stock \nPress 1 to add another product\nPress any other key to stop this customer sale') # display user that to this product is not available
                    ask = input('')# ask the user if he wants to add another product or stop this sale

                    if ask == '1': # if user types 1
                        continue   # go to first line of loop ( add product again)
                    
                    else:          # else if user presses any other key
                        salesmenu()# go to sales menu by calling sales menu() function                   
                
                while True:        # set loop True, mean keeping executing loop until user Enters valid quantity
                    isquantity = False # setting isquantity to False, so dont change quantity if user didnt buy anything
                    try:           # try executing following block of code
                        quantity = eval(input('Enter Quantity of Selling Product ')) # ask user for the quantity of product
                        leftquantity = products[product_code][2] - quantity          # calculate what quantity is left after user adds some quantity
                    
                        if leftquantity < 0: # if quantityleft of product goes in negative value
                            print('Sorry there are ', products[product_code][2], ' products left ') # tell user that there are not many products that he wants to buy
                            ask = input('Press 1 if you want to buy '+ str(products[product_code][2]) + ' or less of this product, press any other key to stop purchasing this product') # ask user if he wants to buy less or wants to purchase some other product
                            if ask != '1':   # if user presses any other key than 1
                                break        # break out to quantity loop to add some other product
                            
                        else:                # else if quantity of product is available
                            products[product_code][2] -= quantity # subtract the quantity bought by user from the orignal one
                            isquantity = True# set isquantity to True i.e some quantity has been bought successfully
                            break            # break out the quantity loop
                         
                    except:                  # if user Enters invalid input if there is an error in try block
                        print('Invalid Input! Quantity can only contain digits and should start from 1') # tell user that input is invalid 
                        
                if not isquantity:           # if user didnt add any quantity
                    continue                 # go to first line of product loop, add some other product, next lines of code wont execute
                # there lines will only execute if some quantity of product has been bought
                total_price = products[product_code][1] * quantity  # calculate total price according to quantity and unit price of product
                
                if product_code in productdict.keys():              # if that product has already been bought by user
                    productdict[product_code][2] += quantity        # then add more to quantity of product, instead of creating new record for it
                    productdict[product_code][3] += total_price     # increase the price according to increased quantity
                    total_bill += total_price                       # increase the total bill
      
                
                else:                        # else if the product is not bought by user already
                    productdict[product_code] = [products[product_code][0], products[product_code][1], quantity, total_price] # add product record to product dictionary
                    total_bill += total_price# add total price of that product to total bill
                
                ask = input('Press 1 to Sale another product to this customer. Press any other key to stop adding products to this sale ') # ask user if he wants to sale another product to this customer
                if ask != '1':               # if user presses any other key then 1
                    break                    # break out of adding product loop

            sales[salesid] = [customer_id, total_bill, productdict]  # if user has finished add products then add that record to sales record
            
            ask = input('Press 1 to add another Sale Record. Press any other key to stop adding Sales ')       # ask user he wants to add any other sales record
            if ask != '1':                   # if user types any other key than 1
                break                        # break out of adding sales loop


        elif not products and customers:     # if products and customers record doesnot exist 
            print('Add Customers and Products Record 1st')   # tell user to add products and customer records first
            break                            # break out of the adding sale loop
        
        elif not products:                   # else if products record doesnt exist
            print('Add Products Record First')               # tell user to add products records first
            break                            # break out of adding sale loop
        
        else:                                # else if customer record is not there
            print('Add Customers Record First')              # tell user to add customer records first
            break                            # break out of adding sale loop
        
        
def viewsale():
 #   print(sales)
    if sales:                               # if sales record exists
        for i in sales.keys():              # loop through all sales keys
            lst = sales[i]                  # store the sale record of a key in a list
            print()                         # print an empty line
            print()                         # print an empty line
            print('\t\t\t\tThe Central Perk Cash and Carry')                                   # display title of system
            print('Sales ID : ', i, '\t\t\t\t\t\t\t\t\t', 'Customer Id : ', lst[0])#9 \ts      # display sales id and customer id
            print('Customer Name : ', customers[lst[0]][0], '\t\t\t\t\t\t\t\t\t', 'Address : ',customers[lst[0]][2]) # display name and address of customer
            print()                         # print an empty space
            print()                         # print an empty space
            print('Product Name\t\t\tUnit Price\t\t\tQuantity\t\t\tTotal Price')               # display the sold product data in tabular way
            print()                         # print an empty space
            
            for j in lst[2].keys():         # loop through product dictionary that contains products bought by a customer
                lst2 = lst[2][j]            # store a product record in a dictionary
                print(lst2[0], '\t\t\t', lst2[1], '\t\t\t', lst2[2], '\t\t\t', lst2[3])        # display that product record
            
            print('TOTAL BILL : ' , lst[1]) # display total bill of that customer 
            print('----------------------------------------------------------------------------------------------')
           
    else:                                   # else if sales record doesnt exist
        print('No Sales Record Exist, Please add sales first ')      # tell the user that sales record doesnt exist 
        
        
        
def salesmenu():                            # defining the sales menu function
    
    while True:                             # infinite loop, keep displaying menu until user wants to break
        print('\t\tSALES MENU')             # display sales menu heading
        print('Press 1 to Add Sale\nPress 2 to View Sales\n3.Go back to main menu')  # tell user about available options
        user = input('What do you want to do ')                      # ask user what he wants to do
        
        if user == '1':                     # if user presses 1, if user wants to add sale record
            addsale()                       # call the addsale() funtion
            #print(sales)
        
        elif user == '2':                   # if user presses 2, if user wanst to view sale records
            viewsale()                      # call the viewsale() function
        
        elif user == '3':                   # else if user presses 3, if user wants to go back to main menu
            break                           # break out of this menu loop
        
        else:                               # else if user presses any other key
            print('Please Enter a Valid Input')                      # tell the user that his input/option is invalid
    
        







#-----------------------------------------------------------------------------------------------------------------------------------------------


print('\t\t\tTHE CENTRAL PERK CASH AND CARRY')                          # display the system heading
while True:                                # infinite loop, keeping looping until user wants to break

    print('1.Produts menu\n2.Customers menu\n3.Sales Menu\n4. Exit')    # display the available options
    user = input('What do you want to do ')                             # ask user what he wants to do
    
    if user == '1':                        # if user wants to go to product menu
        productmenu()                      # call the product menu() function
    
    elif user == '2':                      # if user wants to go to customer menu
        customermenu()                     # call the customer menu() function
    
    elif user == '3':                      # else if user wants to go to sales menu()
        salesmenu()                        # call the sales menu() function
    
    elif user == '4':                      # else if user wants to exit
        break                              # break out of the loop, exits the program
    
    else:                                  # else if user Enters any other choice
        print('Please Enter a Valid Number ') # tell user that his choice is invalid 











