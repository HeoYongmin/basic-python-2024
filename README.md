# 파이썬 기초 2024
부경대 2024 IoT 개발자과정 기초 프로그래밍 언어 - 파이썬

## 1일차
- 개발환경 구축
    - 코딩폰트 - 나눔고딕코딩
    - Notepad++ 설치
    - python 설치
    - visual studio code 설치
    - Git 설치
        - TortoiseGit 설치
        - Github 가입
        - Github Desktop 설치

- 파이썬 기초
    - 파이썬 개발자는 구도 반 로썸
    - 1990년대 귀도가 크리스마스 이브에 취미로 개발
    - 콘솔출력
    - 주석
    - 변수
    - 자료형
    - 연산자

    ```python
    # 이 부분은 주석입니다.
    var01 = 10 # 정수, 실수, 불, 문자열 모두 가능
    print(var01) # 10
    print(type(var01)) # <class of 'int'>
    
    print(5 + 4 /2) # 7.0
    print(5 == 4) # false
    ```

## 2일차
- 파이썬 기초
    - 흐름제어
        - if : 참과 거싯으로 조건을 분기
        - for : 반복문 기본 (다른언어 foreach)
        - while : 반복문 변형 (다른 언어 do~while)
    - 복합자료형 + 연산자(연산함수)
        - 리스트, 튜플, 딕셔너리
    - 출력 포맷, 입력 방법   
    - 구구단 + 디버깅

    ```python
    # debugging
    # F9(중단점 토글), F5(디버깅 시작), F10(한줄씩 실행), F11(함수안으로 진입)
    print('구구단 시작!')
    for x in range(2, 3+1): # 2부터 9까지 반복
    print(f'{x}단 ----->')
    for y in range(1, 9+1): # 1부터 9까지 반복
        print(f'{x} x {y} = {x*y:2d}',end = ' ') # end는 엔터 대신 공백으로 변경
    print() # 안쪽 for문이 끝나면 마지막 엔터를 하나 추가
    ```

## 3일차
- 파이썬 기초
    - 입력 방법
    - 별 찍기(피라미드 만들기)
    - 함수, 람다함수는 나중에...
    - 객체지향 OOP
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아둔 곳 : 클래스(class)
        - 클래스에서 하나씩 생성 : 객체(object)
        - 캡슐화(__plateNumber)
    - 패키지, 모듈    


## 4일차
- 파이썬 기초
    -패키지, 모듈 계속
    - pip 사용

        ```shell
        > pip --version # 버전 확인
        > pip list # 현재 설치된 라이브러리 목록 확인
        > pip install 패키지명 # 패키지를 내 컴퓨터에 설치
        > pip uninstall 패키지명 # 패키지를 삭제
        ```
    - 예외 처리 : 비정상적 프로그램 종료 막기

    ```python
    def divide(x, y):
        try:
            return x / y # ZeroDivisionError 발생
        except ZeroDivisionError as e:
            print('[오류!!] 제수는 0이 될수 없습니다. ')
            return 0
        ```
- 텍스트 파일 입출력

    ```python
    f = open('파일명', mode='r,w,a', encoding='cp949', 'utf-8')
    f.read()
    f.readline() # 읽기
    f.write('text') # 쓰기
    f.close() # 파일은 반드시 닫는다
    ```
- 파이썬 응용
    - 주피터 노트북
        - Ctrl + Shift + P (명령팔레트)로 시작
        - 사용방법 (test31_jupyternb.ipynb 참조)
    - folium 기본 사용
    ![folium 사용법](https://raw.githubusercontent.com/HeoYongmin/basic-python-2024/main/images/python_001.png)

## 5일차
- 파이썬 응용
    - 주피터 노트북 활용 - 구글 코랩(colab)
    - folium 계속
    - json 입출력
    - 응용예제 연습
        - IP주소 확인
        - QRCODE 만들기

## 6일차
- Python 라이브러리 경로 : C:\DEV\Langs\Python311\Lib\site-packages
- 파이썬 응용
    - Window App(PyQt) 만들기

    ```shell
    > pip install PyQt5
    > pip install PyQt5Designer
    ```

    - PyQt5 기본실행
    - QtDesinger 사용법
    - ☆☆☆ 쓰레드 학습 : UI쓰레드와 Background쓰레드 분리
        - GIL, 병렬프로세싱 더학습할것 
   
    ![쓰레드예제 사용법](https://raw.githubusercontent.com/HeoYongmin/basic-python-2024/main/images/python_003.gif)

    ```python
    # 스레드 클래스에서 시그널 선언
    class BackWorker(QThread): # pyQt에서 스레드 클래스 상속
        initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기 위한 변수 객체
        setSignal = pyqtSignal(int)
        #...

        def run(self) -> None: # 스레드 실행할 때는 항상 run 사용
        # 스레드로 동작할 내용
        maxVal = 100
        self.initSignal.emit(maxVal) # UI스레드로 보내기

        class qtwin_exam(QWidget): # UI 스레드
        # ....
        def btnStartClicked(self):
            th = BackWorker(self)
            th.start() # BackWorker 내의 self.run() 실행
            th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리
            # ...
        # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 슬롯함수
        @pyqtSlot(int) # self.initSignal.emit()이 동작해서 실행
        def initPgbTask(self, maxVal):
            self.pgbTask.setValue(0)
            self.pgbTask.setRange(0, maxVal-1)
        ```

## 7일차
- 파이썬 응용
    - 객체지향 정리
        - 상속, 오버라이딩(재정의), 오버로딩(같은이름의 함수를 마음대로 골라쓰자)
    - 가상환경 virtualenv
        - 다른 버전 파이썬도 설치해야 사용 가능
        - 현재 3.11에서 3.9 가상환경 만들려면 3.9 파이썬 설치
    - PyQt5와 응용예제 연습
        - 이미지 뷰어
        - 이미지 에디터

     ![PyQt 예제](https://raw.githubusercontent.com/HeoYongmin/basic-python-2024/main/images/test_001.jpg)

## 8일차
- 파이썬 응용
    - PyQt5 응용예제 계속

- 파이썬 기본 코딩테스트







    - 가상환경
    - 객체지향(나중에...)
        - 오버로딩, 오버라이딩(재정의)
        - 상속, 다중상속
        - 추상클래스, 인터페이스...