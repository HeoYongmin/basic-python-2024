# date : 20240130
# desc : 복합자료형 list
# s1 = 80
# s2 = 90
# s3 = 100
# s4 = 50
# s5 = 60 # 학생 수 만큼 변수를 생성
# 총갯수 10(n) 면 인덱스의 마지막 값은 9(n-1)
#index = 0,  1,   2,  3,  4,  5,  6,  7,  8,  9
#index = -10, -9, -8, -7, -6, -5,-4, -3, -2, -1 
std = [80, 90, 100, 50, 60, 55, 77, 88, 99, 100]
# 리스트 요소 접근
print(std[5])

list_1 = [265, 3.5, '문자열', True, [1,2,3,4], (3,4), std]
print(list_1)
print(list_1[5])
list_1[6] = '바꾼값' # 원래 리스트가 문자열로 변경
print(list_1)

## 리스트 연산
print(list_1[2:3+1]) # 뒤의 수는 출력하고 싶은 인덱스 +1이 필수
## 마이너스 인덱스
print(list_1[-1])
## 이중 리스트
print(list_1[4][2]) # [1,2,3,4] 중 3만 가져오기

list_2 = [[1,2,3],[4,5,6],[7,8,9]] # 0부터 숫자 시작
print(list_2[1][2]) # 6

list_3 = [1,2,3]
list_4 = [7,8,9]
## 리스트 연산 +, * 만 사용가능
print(list_3 + list_4) # +는 리스트를 연결
print(list_4 * 2) # *는 리스틀 반복

## 리스트 길이 len()
print(len(list_3))

## append() 리스트 마지막에 하나 추가
## insert(index, val) 리스트의 index 이후에 val 추가
print(list_1)
list_1.append('Hello')

print(list_1)

list_1.insert(2, 100) # 2번째 인덱스에 값을 추가(원래 값을 뒤로 밀림)
print(list_1)

## extend() 기존 리스트 확장 +와 거의 유사
list_3.extend(list_4)
print(list_3)
print(list_4)

## 리스트 삭제
del list_3[3]
print(list_3)
del list_3 # 리스트 자체를 삭제
# print(list_3)

list_4.pop() # 마지막 값을 꺼내오기
print(std)
print(list_4)

print(std)
val =std.pop(2)
print(val)
print(std)

# clear()
list_4.clear() # del()은 완전삭제 print도 안됨, clear() 내용만 삭제
print(list_4)

# sort()
print(list_1)
# list_1.sort() # 문자열, 숫자, 불 섞여있는 리스트는 정렬안됨
std.sort() # 오름차순 정렬
print(std)
std.sort(reverse=True) # 내림차순 정렬
print(std)

# in, not in
print(99 in std) # True
print(98 in std) # False

# reverse(), copy(), count() ...
# -리스트 : 전개연산자 - 몰라도 됨
list_a = [1,3,5]
list_b = [2,4,8]
list_c = [*list_a, *list_b]
print(list_c) # [1,3,5,2,4,8]

list_d = [list_a, list_b]
print(list_d) # [[1,3,5],[2,4,8]]