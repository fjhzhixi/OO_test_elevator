import operator
# 检查时分运行逻辑和功能逻辑
# 由输入来构建出发地，目的地，当前所在楼层
ins = {}
outs = {}
nows = {}
# 定义乘客状态
status_person = {}
# 记录各个电梯的位置
a_floor = 1
b_floor = 1
c_floor = 1
floors = {'A': a_floor, 'B': b_floor, 'C': c_floor}
# 记录各个电梯的状态(是否已经开门）
a_open = False
b_open = False
c_open = False
status = {'A': a_open, 'B': b_open, 'C': c_open}
# 记录各个电梯可以到达的楼层
all_floors = range(-3, 21)
a_reachable_floors = [-3, -2, -1, 1, 15, 16, 17, 18, 19, 20]
b_reachable_floors = [-2, -1, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
c_reachable_floors = [1, 3, 5, 7, 9, 11, 13, 15]
reachable_floors = {'A': a_reachable_floors, 'B': b_reachable_floors, 'C': c_reachable_floors}
# 记录各个电梯的最大人数
a_max = 6
b_max = 8
c_max = 7
max_nums = {'A': a_max, 'B': b_max, 'C': c_max}
# 记录各个电梯的乘客
a_person = []
b_person = []
c_person = []
persons = {'A': a_person, 'B': b_person, 'C': c_person}
names = ["my"]

def check_arrive(floor, elevator):
    # print(floor)
    # print(floors[elevator])
    # print(elevator)
    # 一次只能运行一层
    if not ((floor == 1 and floors[elevator] == -1) or (floor == -1 and floors[elevator] == 1)):
        # print("not special")
        if abs(floor - floors[elevator]) != 1:
            return False
    # 当前电梯状态(如果开门了）
    if status[elevator]:
        return False
    # 如果指令合法
    floors[elevator] = floor
    # 电梯中人的当前楼层改变
    for id in persons[elevator]:
        nows[id] = floor
    return True


def check_open(floor, elevator):
    # 检查是否在当前楼层开门
    if floor != floors[elevator]:
        return False
    # 检查当前电梯状态是否正确
    if status[elevator]:
        return False
    # 检测当前楼层是否可以开门
    if floor not in reachable_floors[elevator]:
        return False
    # 如果指令合法
    status[elevator] = True
    return True


def check_close(floor, elevator):
    # 检查是否在当前楼层关门
    if floor != floors[elevator]:
        return False
    # 检查当前电梯状态是否正确
    if not status[elevator]:
        return False
    # 检测当前楼层是否可达
    if floor not in reachable_floors[elevator]:
        return False
    # 如果指令合法
    status[elevator] = False
    return True


def check_in(id, floor, elevator):
    # 检查是否是当前楼层
    if floor != floors[elevator]:
        # print(floors[elevator])
        print("1")
        return False
    # 检测电梯状态
    if not status[elevator]:
        print("2")
        return False
    # 检测当前楼层是否可达
    if floor not in reachable_floors[elevator]:
        print("3")
        return False
    # 检测电梯是否满员
    if len(persons[elevator]) >= max_nums[elevator]:
        print("4")
        return False
    # 检测该id是否在这一层
    if floor != nows[id]:
        print("5")
        return False
    # 检查该乘客状态
    if status_person[id] == "IN":
        print("6")
        return False
    # 如果指令合法
    # 乘客上车
    persons[elevator].append(id)
    status_person[id] = "IN"
    return True


def check_out(id, floor, elevator):
    # 检测是否在当前楼层
    if floor != floors[elevator]:
        # print("1")
        return False
    # 检测电梯状态
    if not status[elevator]:
        # print("2")
        return False
    # 检测当前楼层是否可达
    if floor not in reachable_floors[elevator]:
        # print("3")
        return False
    # 检测乘客是否在电梯中
    if id not in persons[elevator]:
        # print("4")
        return False
    # 检测该id是否在当前层
    if floor != nows[id]:
        # print("5")
        return False
    # 检测该乘客状态
    if status_person[id] == "OUT":
        # print("6")
        return False
    # 如果指令合法
    persons[elevator].remove(id)
    status_person[id] = "OUT"
    return True


# 解析input文件
def read_input(input_file_name):
    for line in open(input_file_name, "r"):
        # 去掉换行符
        line = line.strip('\n')
        start = line.find(']')
        str = line[start+1:]
        elem = str.split('-')
        # 当楼层中有负数时
        if len(elem) == 7:
            in_floor = int("-" + elem[3])
            out_floor = int("-" + elem[6])
        elif len(elem) == 6:
            if elem[2] == '':
                in_floor = int("-" + elem[3])
                out_floor = int(elem[5])
            else:
                in_floor = int(elem[2])
                out_floor = int("-" + elem[5])
        else:
            in_floor = int(elem[2])
            out_floor = int(elem[4])
        ins.update({elem[0]: in_floor})
        outs.update({elem[0]: out_floor})
    nows.update(ins)
    for key in nows:
        status_person.update({key: "OUT"})
    # print(ins)
    # print(outs)
    # print(nows)


def get_floor_1(order:str):
    elems = order.split('-')
    if len(elems) == 4:
        return int("-" + elems[2])
    else:
        return int(elems[1])


def get_floor_2(order:str):
    elems = order.split('-')
    if len(elems) == 5:
        return int("-" + elems[3])
    else:
        return int(elems[2])


def init_set():
    floors['A'] = 1
    floors['B'] = 1
    floors['C'] = 1
    status['A'] = False
    status['B'] = False
    status['C'] = False
    ins.clear()
    outs.clear()
    nows.clear()
    status_person.clear()
    a_person.clear()
    b_person.clear()
    c_person.clear()


def check(input_name:str, output_name:str):
    line_num = 0
    read_input(input_name)
    error = open("error.txt", "a+")
    last_line = ""
    for line in open(output_name, "r"):
        line_num += 1
        line = line.strip('\n')
        # print(line)
        strline = line[line.find(']') + 1:]
        # print(strline)
        elem = strline.split('-')
        kind = elem[0]
        # print(kind)
        if kind == "ARRIVE":
            floor = get_floor_1(strline)
            # print(floor)
            if floor < 0:
                elevator = elem[3]
            else:
                elevator = elem[2]
            if not check_arrive(floor, elevator):
                error.write("error " + kind + " in line " + str(line_num) + " in file " + output_name + '\n')
                print("error " + kind + " in line " + str(line_num) + " in file " + output_name)
                break
        elif kind == "OPEN":
            floor = get_floor_1(strline)
            # print(floor)
            if floor < 0:
                elevator = elem[3]
            else:
                elevator = elem[2]
            # print(elevator)
            if not check_open(floor, elevator):
                error.write("error " + kind + " in line " + str(line_num) + " in file " + output_name + '\n')
                print("error " + kind + " in line " + str(line_num) + " in file " + output_name)
                break
        elif kind == "CLOSE":
            floor = get_floor_1(strline)
            if floor < 0:
                elevator = elem[3]
            else:
                elevator = elem[2]
            if not check_close(floor, elevator):
                error.write("error " + kind + " in line " + str(line_num) + " in file " + output_name + '\n')
                print("error " + kind + " in line " + str(line_num) + " in file " + output_name)
                break
        elif kind == "IN":
            id = elem[1]
            # rint(id)
            floor = get_floor_2(strline)
            # print(floor)
            if floor < 0:
                elevator = elem[4]
            else:
                elevator = elem[3]
            # print(elevator)
            if not check_in(id, floor, elevator):
                error.write("error " + kind + " in line " + str(line_num) + " in file " + output_name + '\n')
                print("error " + kind + " in line " + str(line_num) + " in file " + output_name)
                # print(elevator + ":")
                # print(persons[elevator])
                break
        elif kind == "OUT":
            id = elem[1]
            # print(id)
            floor = get_floor_2(strline)
            # print(floor)
            if floor < 0:
                elevator = elem[4]
            else:
                elevator = elem[3]
            # print(elevator)
            if not check_out(id, floor, elevator):
                error.write("error " + kind + " in line " + str(line_num) + " in file " + output_name + '\n')
                print("error " + kind + " in line " + str(line_num) + " in file " + output_name)
                break
        else:
            error.write("error " + kind + " in line " + str(line_num) + " in file " + output_name + '\n')
            print("error " + kind + " in line " + str(line_num) + " in file " + output_name)
            break
        last_line = line
    # 运行完之后检测功能逻辑
    # print(nows)
    # print(outs)
    # 检查人员是否都送到
    if not operator.eq(nows, outs):
        print(nows)
        print(outs)
        error.write("error in logic in file " + output_name + "\n")
        print("error in logic in file " + output_name)
    # 检查电梯是否都关门
    for key in status:
        # print(status)
        if status[key]:
            error.write("error in logic in file " + output_name + "\n")
            print("error in logic in file " + output_name)
            break

    # 检查文件最后一行的时间信息：
    time = last_line[last_line.find('[')+1:last_line.find(']')]
    # print(time)
    if float(time) > 200.0:
        error.write("error in time in file " + output_name + "\n")
        print("error in time in file " + output_name)


if __name__ == '__main__':
    for name in names:
        for i in range(1, 51):
            input_name = "./input_data/" + str(i) + ".txt"
            output_name = "./" + name + "/out" + str(i) + ".txt"
            init_set()
            # print(floors)
            check(input_name, output_name)

