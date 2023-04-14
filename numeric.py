import random
'''
간단한 언덕 등반 알고리즘
Convex.txt 를 사용해서 계산
1. 파일을 읽어옴
2. 파일로 초기값을 생성함
3. Convex.txt 파일의 수식과 값을 이용해서 계산
'''
# "./data/Convex.txt"
def create_problem(filename):
    # 1-1 파일을 읽자
    ini_file = open(filename, 'r', encoding='UTF8')
    expression = ini_file.readline().strip()
    # 리스트
    var_names = []
    lows = []
    up = []
    for line in ini_file.readlines():
        # n,l,u = tuple(line.split(","))
        var_names.append(line.strip().split(",")[0])
        lows.append(float(line.split(",")[1]))
        up.append(line.split(",")[2])

    ini_file.close()
    domain = [var_names, lows, up]
    return (expression, domain)

def random_init(p):
    expression, domain = p
    init = []
    for i in range(1, len(domain[0])):
        # 랜덤 선택
        init.append(random.uniform(domain[1][i], domain[2][i])) # lows ~ up 사이 랜덤 정수
    return init

def evaluate(state, p):
    num_eval = 0
    expression = p[0] # 튜플이라고 가정하고
    var_name = p[1][0]

    for i in range(len(var_name)):
        assignment = var_name[i] + '=' + str(state[i])
        exec(assignment) # exec 문자열을 코드로 실행 

    return eval(expression)

print(create_problem("./data/Convex.txt"))
print(random)



# if __name__ == "__main__":
#     pass
    # print(create_problem("./data/Convex.txt"))
    # print(1)