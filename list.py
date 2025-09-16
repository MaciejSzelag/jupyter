from time import sleep
my_list = [1,2,3]

# print(f"Elemant 0 w my_list= = [1,2,3] to: {my_list[0]}")
# print(f"Elemant 1 w my_list= = [1,2,3] to: {my_list[1]}")
# print(f"Elemant 2 w my_list= = [1,2,3] to: {my_list[2]}")

# my_list = ["srtring", 2, 3, "p"] # The list has been overwritten what is natural for list
# length_my_list = len(my_list) # the len() function will tell you how many items are in the sequence of the list.

# #colon inform to display everthing up to....
# # 
# print(f"Use colon - : - to display everthong up to. In my_list - {my_list} if I use my_list[:2] - is displaying - {my_list[:2]}") 

# print("The length of the list is: ",length_my_list)


#We can also use + to concatenate lists, just like we did for strings.

# print(my_list + ["new item"])

# m_list_2 = my_list.pop()
# print("moja list 2 ",my_list , " - ", m_list_2)


my_list.append("Kuba")
# print(my_list)

# nesting 

l=[] # list jest pusta
# print(f"lista l - jest pusta : {l}")
l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

# print(f"list 1 : {l_1}")
# print(f"list 2 : {l_2}")
# print(f"list 3 : {l_3}")

l = [l_1, l_2, l_3] # teraz list l zawiera 3 listy l_1 l_2 and l_3

# print(f"lista l zawiera wszytkie 3 w/w listy: {l}")

# show_only_0 = [row[0] for row in l]


# print(f"pierwszy elemant z kazdej listy w liscie l to: {show_only_0}")
# for element in l:
#     # print(f"Wszystkie elementy w list l : \n {element}")
#     for el_in_el in element:
#         print(el_in_el," -  ",el_in_el + el_in_el*2)

sit_l = [sit[0] for sit in l]
sit_m = [sit[1] for sit in l]
sit_r = [sit[2] for sit in l]

# print("miejsca przy oknie to:", sit_l,"\n")
# print("miejsca srodkowe to:", sit_m,"\n")
# print("miejsca przy przejsciu to:", sit_r,"\n")





# active_time = 10


elements = []

value_el = 0




while len(elements) < 10:

    # elements.append(value_el)
    value_el += 1
    elements.append(value_el)
    print(value_el)
    print(elements)
