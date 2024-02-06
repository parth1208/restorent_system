import time

print('Welcome To Foodstore')

time.sleep(1)


def validation_error(error_message):
    if len(error_message) != 0:
        print(("*")*45+"\n*Error:\n*"+error_message+"\n"+("*")*45)
        # print("*********************************************\n*Error:\n*"+error_message+"\n*********************************************")
        return 1
    return 0

# def validation(dat,blank,inputvalue):

#     error_message = ''
#     le_is_digit = False
#     le_is_blank = False
#     le_is_symbol = False
#     le_is_string = False

#     if dat == 'str':
#         # if (any(chr.isdigit() for chr in inputvalue)) == True:
#         # error_message='\n*Number and Special Char is not allow.'
#         # if blank == False: error_message = '\n*Number,Special Char and Space is not allow.'
#         for chr in inputvalue:
#             if blank == False and (chr == " " or chr == ""): le_is_blank = True
#             if chr.isdigit():le_is_digit = True              
#             if chr != " " and (chr.isalpha() == False and chr.isdigit() == False): le_is_symbol = True
#                 # error_message = "Please Enter Only String."+error_message
        

#         if le_is_digit == True or le_is_symbol == True or le_is_blank == True:
#             error_message = "Your input contains"
#             if le_is_blank == True: error_message += ' space,'
#             if le_is_digit == True : error_message += ' number,' 
#             if le_is_symbol == True: error_message += ' symbol'
#             if le_is_blank == True or le_is_digit == True and le_is_symbol == False: error_message = error_message[:-1]  
#             error_message += '. Please Enter Only String.'
        

#     if dat == 'num':
#         for chr in inputvalue:
#            if chr.isdigit() == False: le_is_string = True
#            if chr.isalpha() == False and chr.isdigit() == False: le_is_symbol = True

#         if le_is_string == True or le_is_symbol == True:
#            error_message = "Your input contains"
#            if le_is_string == True: error_message += ' strings,'
#            if le_is_symbol == True: error_message += ' symbol'
#            if le_is_string == True and le_is_symbol == False : error_message = error_message[:-1]
#            error_message += '. Please Enter Only Numbers.'

#     return validation_error(error_message)

# def input_with_validation(data_type,blank,required,ask_message):
#     condition = True
#     while condition == True:
#         user_input = input(ask_message)
#         if required == True:
#             if len(user_input) == 0 and user_input == " ":
#                 return validation_error("This Filled is Required.")
#         validation_return = validation(data_type,blank,user_input)
#         if validation_return == 0 :
#             return user_input




# #  User Input for the user details
# customer_firstname = input_with_validation('str',False,True,'\nPlease Enter your first name:- ')
# customer_lastname = input_with_validation('str',False,True,'\nPlease Enter your last name:- ')
# customer_street_number = input_with_validation('num',False,True,'\nPlease Enter  street Number:- ')
# customer_street_name = input_with_validation('str',True,True,'\nPlease Enter  street Name:- ')
# customer_city = input_with_validation('str',True,True,'\nPlease Enter Your city:- ')
# customer_province = input_with_validation('str',True,True,'\nPlease Enter Your province:- ')
# customer_post_code = input_with_validation('num',True,True,'\nPlease Enter Your postal code:- ')
# customer_delivery_ins = input_with_validation('str',True,True,'\nPlease Enter Delivery instruction:- ')
# customer_phone_number = input_with_validation('num',True,True,'\nPlease Enter Phone number:- ')


def menu_resize(space,symbol,li_item_list,li_price_list,item_hdr,price_hdr):
    ls_no_hdr = " No."
    print((symbol)*space)
    print(symbol+(" ")*(space - ((len(symbol))*2))+symbol)
    print(symbol +(ls_no_hdr)+(item_hdr) + (" ")*(space - (len(symbol)*2+(len(item_hdr))+(len(price_hdr))+len(ls_no_hdr))) +price_hdr+symbol)
    print(symbol+(" ")*(space - ((len(symbol))*2))+symbol)
    for i in range(0,len(li_item_list)):
        menu_item = " "+str(li_item_list[i])
        menu_price = str(li_price_list[i])+" "
        menu_number = " "+str(i+1)+"> "
        print(symbol+menu_number+menu_item+(" ")*(space - (len(symbol)*2 + len(menu_item) + len(menu_price) + len(menu_number)))+menu_price+symbol)
    print(symbol+(" ")*(space - ((len(symbol))*2))+symbol)
    print((symbol)*space)

li_item_lists = ["salsa","samosa","pova","buttermilk"]
li_price_lists = [100,25,25,20]

def menu():
    item_hdr = ' ITEMS'
    price_hdr = 'PRICES '
    menu_resize(40,'%',li_item_lists,li_price_lists,item_hdr,price_hdr)



# Restaurants  Menu
show_menu = input("Do You want to open the today Menu? (Y/N):-")
if show_menu == "Y" or show_menu =='y':
    menu()

li_selcted_item = 0
ll_item_qty = 0
ll_error = 0
condition = True
ll_selected_menu = []
ll_selected_menu_qty = []
while condition == True:
    li_selcted_item = int(input("Please enter the selected menu item no:-"))
    if li_selcted_item > len(li_item_lists) or li_selcted_item <= 0:
        ll_error = validation_error("Item NO " +str(li_selcted_item) + "not in the menu.")
    else:
        li_item_qty = int(input("Please enter the qty. of selected item:-"))
        if li_item_qty <= 0:
            ll_error = validation_error("Item Qty can't be "+str(li_item_qty)+".")

    if ll_error ==0: 
        ll_selected_menu.append(li_item_lists[li_selcted_item - 1])
        ll_selected_menu_qty.append(li_item_qty)

    if ll_error != 1:
        ls_ask = input("Do you want to anything else? (Y/N):- ")
        if ls_ask == 'Y' or ls_ask == 'y':
            condition = True
        elif ls_ask == 'N' or ls_ask == 'n':
            condition = False
    else:
        condition = False


ls_show_order = input("Do you want to see your order? (Y/N):- ")
if ls_show_order == "Y" or ls_show_order == "y":
    item_hdr = ' ITEMS'
    price_hdr = 'QTY '
    menu_resize(40,'%',ll_selected_menu,ll_selected_menu_qty,item_hdr,price_hdr)

ll_error = 0
condition = True
while condition == True:
    ls_delivery_type = int(input("\nThank you for your order. please choose your preferred option: \n1> Dine - in \n2> Takeaway \n3> Delivery \nPlease enter the corresponding number for your choice: "))

    if ls_delivery_type < 1 or ls_delivery_type > 3:
        ll_error = validation_error("I apologize, but it appears that the number you've entered is not among the provided options. Please select one of the options mentioned above by entering the corresponding number. Thank you!")
    else:
        ll_error = 0

    if ll_error == 1 :
        condition = True
    else:
        condition = False
    


print("\nThank you for your order! Please allow us 20 minutes to prepare your delicious meal.\n")

#billing code 
ls_show_bill = input("Do You want to checkout?:- (Y/N)")

if ls_show_bill == 'Y' or ls_show_bill == 'y':
    item_hdr = ' ITEMS'
    price_hdr = 'PRICES '
    menu_resize(40,'%',ll_selected_menu,ll_selected_menu_qty,item_hdr,price_hdr)

