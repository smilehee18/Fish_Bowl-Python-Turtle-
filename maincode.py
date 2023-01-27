# Title : Fish_Bowl for Python Turtle Grapic

import turtle                # 터틀 모듈 불러오기
import random                # 랜덤 모듈 불러오기
import winsound              # 사운드 모듈 불러오기
import time                  # 타임 모듈 불러오기
    
scn = turtle.Screen()        # Screen 화면 생성
t=turtle.Turtle()            # t변수에 Turtle 메소드 저장하여 객체 생성
turtle.colormode(255)        # RGB모드의 색상표현방식 지정

img1 = "shell1.gif"           
img2 = "fish1.gif"
img3 = "fish2.gif"
img4 = "water.gif"
img5 = "shell2.gif"

scn.addshape(img1)
scn.addshape(img2)
scn.addshape(img3)
scn.addshape(img4)
scn.addshape(img5)

colors_list = ["slategray","plum","orange","chocolate","goldenrod"] # 색상 리스트 생성


def goto_(x,y):             # 이동하는 함수
    t.up()
    t.goto(x,y)
    t.down()

def fill_circle(x,y,z):     # 도형 채우는 함수     
    t.begin_fill()
    t.circle(x,y,z)
    t.end_fill()

def starWrite() :            # 별 그리는 함수
    t.begin_fill()
    for star in range(1,6):  # 지정된 조건을 5번 반복      
        t.fd(30)
        t.left(72)
        t.fd(30)
        t.right(144)
    t.end_fill() 
        
def seaWeed1() :             # 지그재그 그리는 함수1
    for weed1 in range(1,7): # 지정된 조건을 6번 반복
        t.left(60)
        t.forward(30)
        t.right(60)
        t.forward(30)
        
def seaWeed2() :             # 지그재그 그리는 함수2
    for weed2 in range(1,8): # 지정된 조건을 7번 반복
        t.left(60)                 
        t.forward(25)              
        t.right(60)                
        t.forward(25)

def seaWeed3() :             # 지그재그 그리는 함수3
    for weed3 in range(1,5): # 지정된 조건을 4번 반복
        t.left(60)
        t.forward(35)
        t.right(60)
        t.forward(35)

def stamp_draw(img) :                 # 스탬프 찍는 함수
    for where in range(1,4) :         # 3번 찍기
        t.shape(img)
        t.up()
        t.goto(random.randint(-400,300),random.randint(-400,300)) # 랜덤으로 위치 선정
        t.stamp()
        t.down()

def water_draw(x,y):                 # 물방울 출력하는 이벤트 함수
    t.up()
    t.goto(x,y)
    t.stamp()
    winsound.PlaySound("SystemQuestion",winsound.SND_ALIAS)  # 사운드 출력
    t.down()

def player(img) :                    # 물고기가 이동하는 함수
    for i in range(5):
        t.penup()
        t.shape(img)
        t.goto(random.randint(-400,300),random.randint(-400,300)) # 랜덤으로 위치 선정
        t.pendown()

def back_color() :                  # 스크린 배경색 채우는 함수
        t.begin_fill()
        scn.bgcolor(random.choice(colors_list)) # 리스트중에서 랜덤으로 색깔 선정
        t.end_fill()
                           
t.shape("arrow")             # 커서의 모양을 화살표로 설정
t.width(3)                   # 펜두께의 크기를 3으로 설정
goto_(-500,400)              # 이동하는 함수 호출              
t.fillcolor("lightskyblue")  
t.begin_fill()               
for edge in range(2):        # 어항 테두리 그리기
    t.forward(1000)          
    t.right(90)              
    t.forward(800)           
    t.right(90)               
t.end_fill()

t.width(1)                  # 펜두께의 크기를 1로 설정
t.speed(0)                  # 속도를 최고로 설정
goto_(-100,-400)            # 어항 내부 그리기 시작                   
t.left(90)                  
t.fillcolor("sienna")
fill_circle(200,180,6)      # 육각형 그리기                          
goto_(-460,-350)                          
t.fillcolor("slategray")
fill_circle(50,360,5)       # 오각형 그리기                                      
goto_(-240,-260)                          
t.fillcolor("coral")        
starWrite()                 # 별 그리는 함수 호출                                 
goto_(-200,-360)                               
t.left(150)                 
t.fillcolor("mediumorchid")              
starWrite()                # 별 그리는 함수 호출                                
goto_(-80,-400)
t.fillcolor("mediumseagreen")
t.begin_fill()
seaWeed1()                     # 해초1함수 호출 
t.right(180)
seaWeed1()                     # 해초1함수 호출
t.end_fill()
goto_(-30,-400)                                  
t.left(180)                    
t.fillcolor("palegreen")
t.begin_fill()                  
seaWeed2()                     # 해초2함수 호출             
t.right(180)                   
seaWeed2()                     # 해초2함수 호출
t.end_fill()                                          
goto_(20,-400)                                      
t.right(180)                   
t.fillcolor("darkcyan")        
t.begin_fill()                 
seaWeed3()                     # 해초3함수 호출
t.right(180)                   
seaWeed3()                     # 해초3함수 호출
t.end_fill()                                         
goto_(50,-370)                 # 이동하는 함수 호출                    
t.fillcolor("darksalmon")
t.begin_fill()                 
t.circle(20)
t.end_fill()
goto_(80,-370)                 # 이동하는 함수 호출                             
t.fillcolor("lightpink")       
t.begin_fill()                
t.circle(20)                    
t.end_fill()                                          
goto_(110,-370)                # 이동하는 함수 호출                     
t.fillcolor("lightsteelblue")  
t.begin_fill()                 
t.circle(20)                   
t.end_fill()                                         
goto_(500,-400)                # 이동하는 함수 호출                                              
t.right(150)                   
t.fillcolor(random.randrange(256),random.randrange(256),random.randrange(256))
# 랜덤으로 색상을 택하여 칠하기
fill_circle(180,180,5)         # 오각형 그리기                                       
goto_(300,-240)                                     
t.fillcolor("yellow")          
t.begin_fill()                 
starWrite()                    # 별 그리는 함수 호출 
t.end_fill() 
goto_(370,-300)
t.shape(img1)                  # 조개 사진 넣기           
t.stamp()                      # 스탬프 찍기
goto_(290,-350)
t.shape(img5)                  # 소라 사진 넣기
t.stamp()                      # 스탬프 찍기
t.shape("arrow")               # 커서를 다시 화살표로 설정

goto_(-300,180)                # 동그라미 물고기 그리기                     
t.fillcolor("slateblue")       
t.begin_fill()                 
t.circle(120,180)              
t.end_fill()                   
t.fillcolor("darkviolet")        
t.begin_fill()                          
t.circle(120,180)              
t.end_fill()                   
goto_(-300,180)             
t.right(180)                   
t.fillcolor("violet")          
fill_circle(50,360,3)          # 도형 채우는 함수 호출
goto_(-90,200)               
t.fillcolor("black")          
t.begin_fill()                
t.circle(10)                   
t.end_fill()                  
goto_(-180,360)                
t.right(270)                  
t.fillcolor("orchid")         
fill_circle(50,360,3)          # 도형 채우는 함수 호출
goto_(-180,0)                
t.left(180)                    
t.fillcolor("orchid")          
fill_circle(50,360,3)          # 도형 채우는 함수 호출    
goto_(-40,200)                 
t.circle(15)                   
goto_(0,240)                    
t.circle(15)                  
goto_(130,140)                
t.right(90)                    
t.fillcolor("darkorange")      
fill_circle(150,360,3)         # 삼각형 물고기 그리기
goto_(355,140)              
t.fillcolor("darkgoldenrod")               
fill_circle(50,360,3)          # 도형 채우는 함수 호출
goto_(170,150)                 
t.fillcolor("black")           
t.begin_fill()              
t.circle(10)               
t.end_fill()                   
goto_(120,100)                
t.circle(15)                  
goto_(90,70)               
t.circle(15)                  
t.speed(5)

stamp_draw(img2)                     # 노란색 물고기 함수 호출
stamp_draw(img3)                     # 주황색 물고기 함수 호출
stamp_draw(img4)                     # 물방울 함수 호출

player(img2)                         # 움직이는 노란색 물고기 호출
player(img3)                         # 움직이는 주황색 물고기 호출

t.hideturtle()                       # 커서 숨기기
goto_(-750,400)                      # 화면 가장자리로 이동 
t.write("space바를 누르면 배경색이 랜덤으로 바뀝니다")
goto_(-490,380)                                            
t.write("마우스 왼쪽 버튼을 클릭하면 물방울을 출력합니다")
goto_(-490,350)
t.write(time.strftime("%Z-%z\n%c"))  # 현재 시간을 출력

t.shape(img4)                        # 물방울 이미지로 변경
t.showturtle()                       # 커서 보여주기 
scn.onscreenclick(water_draw)        # 물방울 출력하는 이벤트 함수 호출
scn.onkey(back_color,"space")        # 배경을 랜덤으로 바꾸는 이벤트 함수 호출

scn.listen()                         # 키보드 이벤트를 받기
scn.mainloop()                       # 이벤트 루프 시작
