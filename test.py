import subprocess
import time
import os

start = 0.0
max_time = 200.0
names = ["my"]

def time_init():
    global start
    start = time.clock()


def get_time():
    return (time.clock() - start)


def excute(index, list, strout, belonger):
    os.chdir(belonger)
    # 启动java程序
    obj = subprocess.Popen("java -Djava.ext.dirs=../lib Main",
                           bufsize=0, shell=True, cwd='./',
                           stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print(belonger + "'s elevator starts running...")
    time.sleep(0.3)
    time_init()
    # 定点投放命令
    for elm in list:
        while (get_time() < elm[0]) :
            pass
        obj.stdin.write(elm[1].encode("UTF-8"))
    # 输入结束
    obj.stdin.close()
    # 等待子进程运行至结束
    '''while (obj.poll() == None):
        if (get_time() > max_time):
            with open("error.txt", "a+") as error_file:
                error_file.write("Error at text file-" + str(index))
            print(belonger + " has error in text file-" + str(index))
            break'''
    # 获得输出
    cmd_byte = obj.stdout.read()
    # cmd_out = cmd_byte.decode("UTF-8")
    obj.stdout.close()
    fp = open(strout, "wb")
    fp.write(cmd_byte)
    # print(cmd_out)
    fp.close()
    print(belonger + "'s elevator exits")
    os.chdir("..")

def run(list, strout, belonger):
    os.chdir(belonger)
    # 启动java程序
    obj = subprocess.Popen("java -Djava.ext.dirs=../lib Main",
                           bufsize=0, shell=True, cwd='./',
                           stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print(belonger + "'s elevator starts running...")
    time.sleep(0.3)
    time_init()
    # 定点投放命令
    for elm in list:
        while (get_time() < elm[0]):
            pass
        obj.stdin.write(elm[1].encode("UTF-8"))
    # 输入结束
    obj.stdin.close()
    # 获得输出
    cmd_byte = obj.stdout.read()
    cmd_out = cmd_byte.decode("UTF-8")
    obj.stdout.close()
    fp = open(strout, "wb")
    fp.write(cmd_byte)
    print(cmd_out)
    fp.close()
    print(belonger + "'s elevator exits")
    os.chdir("..")


if __name__ == '__main__':
    # print("main")
     for i in range(1, 51):
        # print(i)
        list = []
        with open("./input_data/" + str(i) + ".txt") as input_file:
            for line in input_file:
                # print(line)
                start = line.find('[')
                end = line.find(']')
                elm = [float(line[start+1:end]), line[end+1:]]
                list.append(elm)
            # run(list, "out" + str(i) + ".txt", "my")
            # print(list)
            for name in names:
                excute(i, list, "out" + str(i) + ".txt", name)







