import time

print('Welcome To Foodstore')

time.sleep(1)


# def validation_error(error_message):
#     if len(error_message) != 0:
#         print(("*")*45+"\n*Error:\n*"+error_message+"\n"+("*")*45)
#         # print("*********************************************\n*Error:\n*"+error_message+"\n*********************************************")
#         return 1
#     return 0

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
        menu_item = " "+li_item_list[i]
        menu_price = str(li_price_list[i])+" "
        menu_number = " "+str(i+1)+"> "
        print(symbol+menu_number+menu_item+(" ")*(space - (len(symbol)*2 + len(menu_item) + len(menu_price) + len(menu_number)))+menu_price+symbol)
    print(symbol+(" ")*(space - ((len(symbol))*2))+symbol)
    print((symbol)*space)

def menu():
    li_item_list = ["salsa","samosa","pova","buttermilk"]
    li_price_list = [100,25,25,20]
    item_hdr = ' ITEMS'
    price_hdr = 'PRICES '
    menu_resize(40,'%',li_item_list,li_price_list,item_hdr,price_hdr)



# Restaurants  Menu
show_menu = input("Do You want to open the today Menu? (Y/N):-")
if show_menu == "Y" or show_menu =='y':
    menu()
