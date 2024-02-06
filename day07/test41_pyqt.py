# date : 20240206
# file : test41_pyqt.py
# desc : PyQt5 이미지 뷰어

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        # 이미지 추가 .scaledToWidth(800) 큰 해상도를 w800으로 고정
        pixmap = QPixmap('./images/cat.jpg').scaledToWidth(800)
        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)

        lblSize = QLabel(self)
        lblSize.setFont(QFont('NanumGothicCoding', 20)) # 폰트와 폰트사이즈 변경
        lblSize.setStyleSheet('Color: orange;')
        lblSize.setText(f'{pixmap.width()} x {pixmap.height()}') # cat.jpg의 width x height
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # 가로중앙정렬 | 세로중앙정렬
        
        vbox = QVBoxLayout(self) # QtDesigner VerticalLayout 위젯 생성
        vbox.addWidget(lblImage) # VL에 위젯 추가
        vbox.addWidget(lblSize)
        self.setLayout(vbox) # Form에 VL 추가와 동일

        self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowTitle('이미지 뷰어')
        rect = QRect(300, 300, 300, 300) # x, y, w, h
        self.setGeometry(rect) # 같은 이름의 함수를 여러개 선언해놓고 입맛에 맞게 골라쓰는 BR(오버로딩)
        # self.setGeometry(300, 300, 300, 300)
        self.show() # showFullScreen() 모니터를 꽉 채워서 출력
        self.setCenter()

    def setCenter(self): ## 윈앱을 화면 정중앙에 위치
        gm = self.frameGeometry() # 윈앱 자신의 위치 값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    width, heigh = screen_rect.width(), screen_rect.height()
    print(width, 'x', heigh) # 활용도 높음
    ins = WinApp()
    ins.show() # showFullScreen() 모니터를 꽉 채워서 출력
    sys.exit(app.exec_()) # 종료시 리소스 반환등의 효율을 위해서 sys 사용

    
