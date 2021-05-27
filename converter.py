import pandas as pd
#판다스 모듈을 불러와서 pd라고 지정
# Taking NFA input from User

nfa = {}
n = int(input("Number of states : "))  # 총 상태의 수를 적으세요.
t = int(input("Number of transitions : "))  #  transitions/paths 의 total 수를 입력하세요 예: a,b 이면 input 2 이고 a,b,c는  input 3
for i in range(n): # states 의 수 만큼 반복
    state = input("상태의 이름 입력(상태의 이름을 입력 예: A, B, C, q1, q2 ) : ")  # 상태의 이름을 입력 예: A, B, C, q1, q2 ..등등
    nfa[state] = {}  # 중첩 딕셔너리를 생성한다.
    for j in range(t): # transition의 수만큼 반복을 한다.
        path = input("path : ")  #  path를 입력한다 예 : a or b in {a,b}    0 or 1 in {0,1}
        print("State {}에서 input symbol  {}을 통하여서 갈 수 있는 State를 입력하세요. : ".format(state, path )) #처음{}에는 state가 두번째 {}에는 path가 출력
        reaching_state = [x for x in input().split()]  # 해당 path로 도달할 수 있는 모든 end states 를 입력
        nfa[state][path] = reaching_state

print("\nNFA : \n")
print(nfa)  # NFA 를 출력한다.
print("\nNFA 테이블을 출력한다. :")
nfa_table = pd.DataFrame(nfa) #pandas 의 DataFrame을 이용하여 nfa 테이블을 매개변수로 하여 nfa_table을 테이블 형식으로 생성
print(nfa_table.transpose())  # nfa_table 의 행과 열을 전치 시켜준다.

print("NFA 에서의 final state 를 입력하여라 : ")
nfa_final_state = [x for x in input().split()]  # NFA의 최종 state/states를 입력해라


new_states_list = []  #  새롭게 생성된 상태들을 저장
dfa = {}
keys_list = list(
    list(nfa.keys())[0]) #nfa의 모든 상태와 dfa에서 생성 된 상태도 추가됩니다.

path_list = list(nfa[keys_list[0]].keys())  # 모든 path들에 대한 list


#DFA transition 테이블의 첫번째 행을 계산

dfa[keys_list[0]] = {}  # DFA 의 중첩 딕셔너리를 생성한다.
for y in range(t):#path 의 수만큼 반복
    var = "".join(nfa[keys_list[0]][
                      path_list[y]])  # DFA 표에서 상태를 할당하는 새로운 상태인 목록의 모든 요소에서 단일 문자열 생성
    dfa[keys_list[0]][path_list[y]] = var
    if var not in keys_list:  # 상태가 새롭게 생성되었다면
        new_states_list.append(var)  #그럼 new_states_list 추가를 한다.
        keys_list.append(var)  # 또한 모든 상태를 포함하는 keys_list 에 추가한다.

#  DFA transition 테이블에서 다른 행을 연산을 한다.

while len(new_states_list) != 0:  # new_states_list가 비어 있지 않은 경우에만 참
    dfa[new_states_list[0]] = {}  # new_states_list의 첫 번째 요소를 가져 와서 검사
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []  # 임시리스트를 만든다.
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]  #임시 리스트에 상태들을 추가
            s = "" #빈 문자열
            s = s.join(temp)  #  단일 문자열 (새 상태) 만들기
            if s not in keys_list:  # 상태가 새롭게 생성되었다면
                new_states_list.append(s)  #  그렇다면 new_states_list에 추가
                keys_list.append(s)  # 모든 상태를 포함하는 keys_list에도 추가
            dfa[new_states_list[0]][path_list[i]] = s  # DFA 테이블에 새 상태 할당

    new_states_list.remove(new_states_list[0])  # new_states_list에서 첫번째 원소를 제거한다.
print("\nDFA : \n")
print(dfa)  # 생성된 DFA를 출력
print("\n DFA table 출력 : ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break

print("\nDFA의 final state들을 출력한다. : ", dfa_final_states)  # DFA의 최종상태를 출력한다.

