from collections import deque
# Трябва да махаме от поръчките първо от индекс 0, затова ползваме опашка
pizza_orders = deque([int(x) for x in input().split(", ") if 0 < int(x) < 11])
# Тук махаме от края, затова оставяме да е stack
employees = [int(x) for x in input().split(", ")]
# Борояч на издадените пици
total_counter = 0
# Булева, за да спрем двата цикъла, когато не са останали employees
is_orders = False
# Първи цикъл - докато има поръчки и employees да ги приемат
while pizza_orders and employees:
    # Втори цикъл, докато има неизпълнена поръчка на индекс 0 да се предава на свободните employees
    # Когато приключи, премахваме поръчката от индекс 0 и следващата поръчка става индекс 0, защото е опашка и не се
    # преиндексира списъка
    while pizza_orders[0] > employees[-1]:
        # Добавяме към брояча текущият employee, защото той носи бройката направени пици, когато поръчката не е
        # изпълнена изцяло
        total_counter += employees[-1]
        # От текущата поръчка изваждаме вече направените пици
        pizza_orders[0] = pizza_orders[0] - employees[-1]
        # Премахваме текущият employee
        employees.pop()
        # Правим проверка дали в списъка има останали employees. Ако няма променяме булевата на True и брейкваме
        if not employees:
            # Булевата ни е необходима, за да спрем и външният цикъл
            is_orders = True
            break
    # Правим проверка дали булевата е True и брейкваме външния цикъл.
    if is_orders:
        break
    # Ако сме излезли от вътрешния цикъл, означава, че текущата поръчка е изпълнена.
    # Добавяме останалото количество в поръчката към брояча
    total_counter += pizza_orders[0]
    # Премахваме поръчката на индекс 0
    pizza_orders.popleft()
    # Премахваме текущият employee
    employees.pop()

# Ако са останали поръчки:
if pizza_orders:
    # Принтираме че не са изпълнени всички поръчки
    print("Not all orders are completed.")
    # Принтираме останалите поръчки, които трябва да ги разопаковаме, като ги правим на str
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
else:
    # Принтираме, че са изпълнени
    print("All orders are successfully completed!")
    # Принтираме броя на направените пици
    print(f"Total pizzas made: {total_counter}")
    # Принтираме останалите employees като ги разопаковаме и правим на str
    print(f"Employees: {', '.join(str(x) for x in employees)}")

# def process_orders(pizza_orders, employees):
#     orders = list(map(int, pizza_orders.split(", ")))
#     employees = list(map(int, employees.split(", ")))
#
#     completed_orders = []
#     total_pizzas_made = 0
#
#     while orders:
#         order = orders[0]
#         employee = employees[-1]
#
#         if order <= 0:
#             orders.pop(0)
#             continue
#
#         if order <= employee:
#             employees.pop()
#             total_pizzas_made += order
#             completed_orders.append(order)
#             orders.pop(0)
#         else:
#             orders[0] -= employee
#             total_pizzas_made += employee
#             employees.pop()
#
#     if not orders:
#        return f"All orders are successfully completed!\nTotal pizzas made: {total_pizzas_made}\nEmployees: " \
               # f"{', '.join(map(str, employees))}"
#     else:
#         return f"Not all orders are completed.\nOrders left: {', '.join(map(str, orders))}"
#
# process_orders()
# # Примери
# pizza_orders = "11, 6, 8, 1"
# employees = "3, 1, 9, 10, 5, 9, 1"
# print(process_orders(pizza_orders, employees))
#
# pizza_orders = "10, 9, 8, 7, 5"
# employees = "5, 10, 9, 8, 7"
# print(process_orders(pizza_orders, employees))
#
# pizza_orders = "12, -3, 14, 3, 2, 0"
# employees = "10, 15, 4, 6, 3, 1, 22, 1"
# print(process_orders(pizza_orders, employees))