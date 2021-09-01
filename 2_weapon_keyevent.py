'''
Project) 오락실 Pang 게임 만들기
[게임 조건]
1. 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
2. 스페이스를 누르면 무기를 쏘아 올림
3. 큰 공 1개가 나타나서 바운스
4. 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
5. 모든 공을 없애면 게임 종료(성공)
6. 캐릭터는 공에 닿으면 게임 종료 (실패)
7. 시간 제한 99초 초과 시 게임 종료 (실패)
8. FPS 는 30 으로 고정 (필요시 speed 값을 조정)

[게임 이미지]
1. 배경 : 640 * 480 (가로 세로) -background.png
2. 무대 : 640 * 50 -stage.png
3. 캐릭터 : 33 * 60 -character.png
4. 무기 : 20 * 430 -weapon.png
5. 공 : 160 * 160, 80 * 80, 40 * 40, 20 * 20 - balloon1.png ~ ballon4.png
'''
import pygame
import os
##############################################################################
# 기본 초기화 부분 (반드시 해야 하는 것들)

pygame.init()   #초기화 (반드시 필요)

# 화면 크기 설정

screen_width = 640  # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("PANG!") # 게임 이름


# FPS
clock = pygame.time.Clock()
##############################################################################



# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

current_path = os.path.dirname(__file__) # 현재 파일의 위치를 반환
image_path= os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기

background = pygame.image.load(os.path.join(image_path,"background.png"))


# 스테이지 만들기

stage = pygame.image.load(os.path.join(image_path,"stage.png"))

stage_size = stage.get_rect().size
stage_height=stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기

character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width= character_size[0]
character_height=character_size[1]
character_x_pos = (screen_width/2) - (character_width /2)
character_y_pos = screen_height- character_height-stage_height

# 캐릭터 이동 방향

character_to_x= 0

# 캐릭터 이동속도
character_speed = 5


# 무기 만들기

weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size= weapon.get_rect().size

weapon_width= weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능

weapons = []

# 무기 이동 속도
weapon_speed = 10

# 이벤트 루프

running = True # 게임이 진행중인가 ?


while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:      
            running = False    
    if event.type==pygame.KEYDOWN:
        if event.key ==pygame.K_LEFT:
            character_to_x -=character_speed
        elif event.key ==pygame.K_RIGHT:
            print("right")
            character_to_x += character_speed
        elif event.key ==pygame.K_UP:
            print("aaa")
            weapon_x_pos = character_x_pos+ (character_width/2)-(weapon_width/2)
            weapon_y_pos = character_y_pos
            weapons.append([weapon_x_pos,weapon_y_pos])
        
    if event.type ==pygame.KEYUP:
        if event.key ==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
            character_to_x=0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos+=character_to_x
    

    if character_x_pos <0:
        character_x_pos =0
    elif character_x_pos > screen_width- character_width:
        character_x_pos = screen_width-character_width

    # 무기 위치 조정
    # 100, 200 ->
    weapons = [ [w[0],w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로 오림

    # 천장에 닿은 무기 없애기
    weapons = [[w[0],w[1]] for w in weapons if w[1]>0]
    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기 계속 불러오기 pygame에선 반드시 해줘야하는 작업


# pygame 종료
pygame.quit()