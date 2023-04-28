import pygame, sys, os, json
        
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):     
        global look,pspeed,wall_rect,wall_rect_2,wall_rect_3,wall_rect_4,wall_rect_5,re,php,keylist,ending
        super().__init__()
        self.dsprites = []
        self.usprites = []
        self.rsprites = []
        self.lsprites = []
        self.ursprites = []
        self.ulsprites = []
        self.dlsprites = []
        self.drsprites = []
        self.deadsprites = []
    
        self.usprites.append(pygame.image.load('up1.png'))
        self.usprites.append(pygame.image.load('up2.png'))
        self.usprites.append(pygame.image.load('up3.png'))
        self.usprites.append(pygame.image.load('up4.png'))
        self.usprites.append(pygame.image.load('up5.png'))
        
        self.dsprites.append(pygame.image.load('newattack2.png'))
        self.dsprites.append(pygame.image.load('down2.png'))
        self.dsprites.append(pygame.image.load('down3.png'))
        self.dsprites.append(pygame.image.load('down4.png'))
        self.dsprites.append(pygame.image.load('down5.png'))
        
        self.lsprites.append(pygame.image.load('newleft1.png'))
        self.lsprites.append(pygame.image.load('left2.png'))
        self.lsprites.append(pygame.image.load('left3.png'))
        self.lsprites.append(pygame.image.load('left4.png'))
        self.lsprites.append(pygame.image.load('left5.png'))
        
        self.rsprites.append(pygame.image.load('newright1.png'))
        self.rsprites.append(pygame.image.load('newright2.png'))
        self.rsprites.append(pygame.image.load('newright3.png'))
        self.rsprites.append(pygame.image.load('newright4.png'))
        self.rsprites.append(pygame.image.load('newright5.png'))
        
        self.ulsprites.append(pygame.image.load('upleft1.png'))
        self.ulsprites.append(pygame.image.load('upleft2.png'))
        self.ulsprites.append(pygame.image.load('upleft3.png'))
        self.ulsprites.append(pygame.image.load('upleft4.png'))
        self.ulsprites.append(pygame.image.load('upleft5.png'))   
        
        self.ursprites.append(pygame.image.load('upright1.png'))
        self.ursprites.append(pygame.image.load('upright2.png'))
        self.ursprites.append(pygame.image.load('upright3.png'))
        self.ursprites.append(pygame.image.load('upright4.png'))
        self.ursprites.append(pygame.image.load('upright5.png'))
        
        self.dlsprites.append(pygame.image.load('newdownleft1.png'))
        self.dlsprites.append(pygame.image.load('downleft2.png'))
        self.dlsprites.append(pygame.image.load('downleft3.png'))
        self.dlsprites.append(pygame.image.load('downleft4.png'))
        self.dlsprites.append(pygame.image.load('downleft5.png'))
        
        self.drsprites.append(pygame.image.load('newdownright1.png'))
        self.drsprites.append(pygame.image.load('downright2.png'))
        self.drsprites.append(pygame.image.load('downright3.png'))
        self.drsprites.append(pygame.image.load('downright4.png'))
        self.drsprites.append(pygame.image.load('downright5.png'))
        
        self.deadsprites.append(pygame.image.load('dead2.png'))    
        self.deadsprites.append(pygame.image.load('dead3.png'))    
        self.deadsprites.append(pygame.image.load('dead4.png'))  
        
        self.porta= pygame.mixer.Sound("porta2.ogg")
        self.deadsound=[]
        self.deadsound.append(pygame.mixer.Sound("hit.ogg"))
        self.deadsound[0].set_volume(0.1)
        self.deadsound.append(pygame.mixer.Sound("blood.ogg"))
        self.deadsound[1].set_volume(0.1)
        
        wall_rect = []
        wall_rect_2 = []
        wall_rect_3 = []
        wall_rect_4 = []
        wall_rect_5 = []
        self.teleport=[]
        
        keylist=[False,False,False,False,False]
        ending=False
        wall_rect.append(pygame.Rect(200,316,78,28))
        wall_rect.append(pygame.Rect(399,316,179,28))
        wall_rect.append(pygame.Rect(700,316,180,28))
        wall_rect.append(pygame.Rect(1002,316,78,28))
        wall_rect.append(pygame.Rect(475,130,29,200))
        wall_rect.append(pygame.Rect(776,130,29,200))
        wall_rect.append(pygame.Rect(779,328,280,17))
        wall_rect.append(pygame.Rect(559,328,200,6))
        
        wall_rect_2.append(pygame.Rect(205,310,533,28))
        wall_rect_2.append(pygame.Rect(811,226,181,28))
        wall_rect_2.append(pygame.Rect(811,471,181,28))
        wall_rect_2.append(pygame.Rect(556,435,181,28))
        wall_rect_2.append(pygame.Rect(707,463,30,157))
        wall_rect_2.append(pygame.Rect(707,100,30,212))
        
        wall_rect_3.append(pygame.Rect(340,252,181,28))
        wall_rect_3.append(pygame.Rect(492,252,30,120))
        wall_rect_3.append(pygame.Rect(625,252,29,213))
        wall_rect_3.append(pygame.Rect(758,252,182,28))
        wall_rect_3.append(pygame.Rect(911,252,29,211))
        wall_rect_3.append(pygame.Rect(492,344,280,28))
        wall_rect_3.append(pygame.Rect(340,252,29,212))
        wall_rect_3.append(pygame.Rect(758,252,30,120))
        
        
        wall_rect_4.append(pygame.Rect(203,435,305,28))
        wall_rect_4.append(pygame.Rect(614,435,470,28))
        wall_rect_4.append(pygame.Rect(294,304,321,28))
        wall_rect_4.append(pygame.Rect(854,214,29,117))
        wall_rect_4.append(pygame.Rect(854,214,127,28))
        wall_rect_4.append(pygame.Rect(952,280,127,28))
        wall_rect_4.append(pygame.Rect(952,214,29,90))
        wall_rect_4.append(pygame.Rect(586,101,29,222))
        
        self.teleport.append(pygame.Rect(1060,460,50,48))
        self.teleport.append(pygame.Rect(200,430,10,88))
        self.teleport.append(pygame.Rect(857,95,88,10))
        self.teleport.append(pygame.Rect(857,614,88,10))
        self.teleport.append(pygame.Rect(857,614,88,10))
        self.teleport.append(pygame.Rect(857,95,88,10))
        self.teleport.append(pygame.Rect(1068,316,10,88))
        self.teleport.append(pygame.Rect(198,314,10,88))

        re=[False,False,False,False,False,False]
        self.current_sprite = 0
        self.tempim = self.dsprites[0]
        self.image = self.dsprites[0]
        self.rect = self.image.get_rect() 
        
        self.mainlevel=1
        self.rect.x = 320
        self.rect.y = 180
        
        self.help_x = 0
        self.help_y = 0
        
        self.x_speed = 0
        self.y_speed = 0
        
        self.d=0
        
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.a_pressed = False
        self.d_pressed = False
        self.w_pressed = False
        self.s_pressed = False
        self.opendoor=[False,False]
        look=0
        pspeed=True
        php=4
        
        self.image = pygame.Surface((40,40))
        self.image.fill((200,30,30))
        
        self.current_hp = 800
        self.target_hp = 800
        self.max_hp = 800
        self.hp_bar_length = 140
        self.hp_ratio = self.max_hp / self.hp_bar_length
        self.hp_change_speed = 5
    
    def get_damage(self,amount):
        if self.target_hp > 0:
            self.target_hp -= amount
        if self.target_hp < 0:
            self.target_amount = 0
    
    def get_hp(self,amount):
        if self.target_hp < self.max_hp:
            self.target_hp += amount
        if self.target_hp > self.max_hp:
            self.target_hp = self.max_hp
    
    def advanced_hp(self):
        transition_width = 0
        transition_color = (255,0,0)
        
        if self.current_hp < self.target_hp:
            self.current_hp += self.hp_change_speed
            transition_width = int((self.target_hp - self.current_hp) / self.hp_ratio)
            transition_color = (0,255,0)
        
        if self.current_hp > self.target_hp:
            self.current_hp -= self.hp_change_speed
            transition_width = int((self.target_hp - self.current_hp) / self.hp_ratio)
            transition_color = (255,255,0)
        
        hp_bar_width = int(self.current_hp / self.hp_ratio)
        hp_bar = pygame.Rect(10,30,hp_bar_width, 15)
        transition_bar = pygame.Rect(hp_bar.right,30, transition_width, 15)
        
        pygame.draw.rect(screen, (255,0,0), hp_bar)
        pygame.draw.rect(screen,transition_color,transition_bar)
        pygame.draw.rect(screen,(255,255,255), (10,30, self.hp_bar_length, 15), 3)
        
    def reset(self):
        if self.x_speed==0 and self.y_speed==0:
            self.image=self.tempim
            
    def movement(self):
        global px,py,level,player_rect,use,current_key,ending
        level=self.mainlevel
        
        self.a=0
        self.x_speed = 0
        self.y_speed = 0
        player_rect = pygame.Rect(self.rect.x + 5,self.rect.y +1,49,85)
        
        
        if php>0:
            if self.a_pressed and not self.d_pressed:
                self.x_speed = -2
            if self.d_pressed and not self.a_pressed:
                self.x_speed = 2
            if self.w_pressed and not self.s_pressed:
                self.y_speed = -2
            if self.s_pressed and not self.w_pressed:
                self.y_speed = 2
                
            if level==1:
                detect[1]=0
                detect[2]=0
                detect[3]=0
                detect[4]=0
                detect[5]=0
                for i in range(8):
     
                    if player_rect.colliderect(wall_rect[i]):
                      self.a=1
                if player_rect.colliderect(wall_rect[7]) and current_key==1:
                  wall_rect[7]=(pygame.Rect(-220,328,200,6))
                  current_key=-1
                  self.porta.play()
                  background_image[0]=pygame.image.load("1st level v3 no door.jpg").convert()
                if player_rect.colliderect(self.teleport[0]):
                    
                    self.mainlevel=2
                    self.rect.x=211
                    self.rect.y=436
                    re[0]=True
                    
                    
            elif level==2:
                detect[0]=0
                detect[2]=0
                detect[3]=0
                # detect[4]=0
                # detect[5]=0
                for i in range(6):
                    
                    if player_rect.colliderect(wall_rect_2[i]):
                        self.a=1
                  
                
                if player_rect.colliderect(self.teleport[1]):
                    detect[1]=0
                    self.mainlevel=1
                    self.rect.x=1000
                    self.rect.y=450
                    re[1]=True
                    
                
                if player_rect.colliderect(self.teleport[2]) and (current_key==0 or self.opendoor[0]==True):
                    detect[2]=0
                    # detect[4]=0
                    self.mainlevel=3
                    self.rect.x=857
                    self.rect.y=509
                    
                   
                    re[1]=True
                    if current_key==0:
                       current_key=-1
                    self.opendoor[0]=True
                    self.porta.play()
                    background_image[1]=pygame.image.load("2nd -red.jpg").convert()
                    
                if player_rect.colliderect(self.teleport[4]) and (current_key==2 or self.opendoor[1]==True):
                    detect[3]=0
                    # detect[5]=0
                    self.mainlevel=4
                    self.rect.x=865
                    self.rect.y=111
                    re[1]=True
                    # detect[level-1]=0
                    # detect[level+1]=0
                    
                    if current_key==2:
                       current_key=-1
                    self.opendoor[1]=True
                    self.porta.play()
                    background_image[1]=pygame.image.load("2nd -blue and red.jpg").convert()
                    
                if player_rect.colliderect(self.teleport[6]) and current_key==3:
                    ending=True
                    self.rect.x=217
                    self.rect.y=312
                    
                    current_key=-1
                    
            elif level==3: 
                detect[1]=0
                detect[0]=0
                detect[3]=0
                
                for i in range(8):
                    if player_rect.colliderect(wall_rect_3[i]):
                        self.a=1
                
                if player_rect.colliderect(self.teleport[3]):
                   self.mainlevel=2
                   self.rect.x=865
                   self.rect.y=111
                   re[2]=True
                   
            elif level==4:
                detect[1]=0
                detect[2]=0
                detect[0]=0
               
                if player_rect.colliderect(self.teleport[5]):
                    self.mainlevel=2
                    self.rect.x=865
                    self.rect.y=512
                    re[3]=True
                
                for i in range(8):
                    if player_rect.colliderect(wall_rect_4[i]):
                        self.a=1
                 
           
            
                    
            if self.rect.x >=203 and self.rect.x <=1020 and self.a==0:
                 self.help_x = self.rect.x  
                 self.rect.x += self.x_speed
                 
                 
            else:
                 self.x_speed=0
                 self.rect.x = self.help_x
                 
            if self.rect.y >=103 and self.rect.y <=534 and self.a==0 :
                 self.help_y = self.rect.y  
                 self.rect.y += self.y_speed
                 
            else:
                 self.y_speed=0
                 self.rect.y = self.help_y
            px=self.rect.x
            py=self.rect.y
           
    def update(self, speed):
        global look,pspeed
        
        if self.x_speed==0 and self.y_speed==0:
            pspeed=True
        else:
            pspeed=False
        
        if php>0:
            if self.x_speed==2 and self.y_speed==-2:
                self.current_sprite += speed
                if int(self.current_sprite) >= len(self.ursprites):
                    self.current_sprite = 1
                
                look=2
                self.tempim=self.ursprites[0]                     
                self.image = self.ursprites[int(self.current_sprite)]
                
            elif self.x_speed==-2 and self.y_speed==-2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.ulsprites):
                    self.current_sprite = 1
                    
                look=8   
                self.tempim=self.ulsprites[0]
                self.image = self.ulsprites[int(self.current_sprite)]
                
            elif self.x_speed==-2 and self.y_speed==2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.dlsprites):
                    self.current_sprite = 1
                    
                look=6
                self.tempim=self.dlsprites[0]       
                self.image = self.dlsprites[int(self.current_sprite)]
                
            elif self.x_speed==2 and self.y_speed==2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.drsprites):
                    self.current_sprite = 1
                    
                look=4
                self.tempim=self.drsprites[0]       
                self.image = self.drsprites[int(self.current_sprite)]
                
            elif self.y_speed==2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.dsprites):
                    self.current_sprite = 1
                
                look=5
                self.tempim=self.dsprites[0]        
                self.image = self.dsprites[int(self.current_sprite)]
                
            elif self.y_speed==-2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.usprites):
                    self.current_sprite = 1
                    
                look=1
                self.tempim=self.usprites[0]       
                self.image = self.usprites[int(self.current_sprite)]  
                
            elif self.x_speed==-2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.lsprites):
                    self.current_sprite = 1
                    
                look=7
                self.tempim=self.lsprites[0]       
                self.image = self.lsprites[int(self.current_sprite)] 
                
            elif self.x_speed==2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.rsprites):
                    self.current_sprite = 1
                    
                look=3
                self.tempim=self.rsprites[0] 
                self.image = self.rsprites[int(self.current_sprite)]
                
            if self.x_speed==0 and self.y_speed==0 and player.left_pressed==True and player.down_pressed==True   :
                self.tempim=self.dlsprites[0] 
                look=6
            elif self.x_speed==0 and self.y_speed==0 and player.left_pressed==True and player.up_pressed==True  :
                self.tempim=self.ulsprites[0] 
                look=8
            elif self.x_speed==0 and self.y_speed==0 and player.right_pressed==True and player.down_pressed==True   :
                self.tempim=self.drsprites[0] 
                look=4
            elif self.x_speed==0 and self.y_speed==0 and player.right_pressed==True and player.up_pressed==True   :
                self.tempim=self.ursprites[0] 
                look=2
            elif self.x_speed==0 and self.y_speed==0 and player.right_pressed==True:
                self.tempim=self.rsprites[0] 
                look=3
            elif self.x_speed==0 and self.y_speed==0 and player.left_pressed==True:
                self.tempim=self.lsprites[0] 
                look=7
            elif self.x_speed==0 and self.y_speed==0 and player.up_pressed==True:
                self.tempim=self.usprites[0] 
                look=1
            elif self.x_speed==0 and self.y_speed==0 and player.down_pressed==True:
                self.tempim=self.dsprites[0] 
                look=5
        else:  
            self.x_speed=0
            self.y_speed=0
          
            if int(self.d) < 2:
                if self.d==0:
                    self.deadsound[0].play()
                    self.deadsound[1].play()
                self.d += speed*3
                
                
                self.tempim = self.deadsprites[int(self.d)]
                self.image=self.tempim
        self.advanced_hp()
       
       
class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y):
        global ex,ey,ehp,enemylook,detect,enemybullet_list
        super().__init__()
        self.dsprites = []
        self.usprites = []
        self.rsprites = []
        self.lsprites = []
        self.ursprites = []
        self.ulsprites = []
        self.dlsprites = []
        self.drsprites = []
        self.deadsprites = []
        
        self.usprites.append(pygame.image.load('g_up1.png'))
        self.usprites.append(pygame.image.load('g_up2.png'))
        self.usprites.append(pygame.image.load('g_up3.png'))
        self.usprites.append(pygame.image.load('g_up4.png'))
        self.usprites.append(pygame.image.load('g_up5.png'))
        
        self.dsprites.append(pygame.image.load('g_attack3.png'))
        self.dsprites.append(pygame.image.load('g_down2.png'))
        self.dsprites.append(pygame.image.load('g_down3.png'))
        self.dsprites.append(pygame.image.load('g_down4.png'))
        self.dsprites.append(pygame.image.load('g_down5.png'))
        
        self.lsprites.append(pygame.image.load('g_left1.png'))
        self.lsprites.append(pygame.image.load('g_left2.png'))
        self.lsprites.append(pygame.image.load('g_left3.png'))
        self.lsprites.append(pygame.image.load('g_left4.png'))
        self.lsprites.append(pygame.image.load('g_left5.png'))
        
        self.rsprites.append(pygame.image.load('g_right1.png'))
        self.rsprites.append(pygame.image.load('g_right2.png'))
        self.rsprites.append(pygame.image.load('g_right3.png'))
        self.rsprites.append(pygame.image.load('g_right4.png'))
        self.rsprites.append(pygame.image.load('g_right5.png'))
        
        self.ulsprites.append(pygame.image.load('g_upleft1.png'))
        self.ulsprites.append(pygame.image.load('g_upleft2.png'))
        self.ulsprites.append(pygame.image.load('g_upleft3.png'))
        self.ulsprites.append(pygame.image.load('g_upleft4.png'))
        self.ulsprites.append(pygame.image.load('g_upleft5.png'))   
        
        self.ursprites.append(pygame.image.load('g_upright1.png'))
        self.ursprites.append(pygame.image.load('g_upright2.png'))
        self.ursprites.append(pygame.image.load('g_upright3.png'))
        self.ursprites.append(pygame.image.load('g_upright4.png'))
        self.ursprites.append(pygame.image.load('g_upright5.png'))
        
        self.dlsprites.append(pygame.image.load('g_downleft1.png'))
        self.dlsprites.append(pygame.image.load('g_downleft2.png'))
        self.dlsprites.append(pygame.image.load('g_downleft3.png'))
        self.dlsprites.append(pygame.image.load('g_downleft4.png'))
        self.dlsprites.append(pygame.image.load('g_downleft5.png'))
        
        self.drsprites.append(pygame.image.load('g_downright1.png'))
        self.drsprites.append(pygame.image.load('g_downright2.png'))
        self.drsprites.append(pygame.image.load('g_downright3.png'))
        self.drsprites.append(pygame.image.load('g_downright4.png'))
        self.drsprites.append(pygame.image.load('g_downright5.png'))
        
        self.deadsprites.append(pygame.image.load('g_dead1.png'))    
        self.deadsprites.append(pygame.image.load('g_dead2.png'))    
        self.deadsprites.append(pygame.image.load('g_dead3.png'))  
        
        self.attack=pygame.image.load('g_attack1.png')
        
        self.current_sprite = 0
        self.tempim = self.dsprites[0]
        self.image = self.dsprites[0]
        self.rect = self.image.get_rect() 
        
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        ex=self.rect.x
        ey=self.rect.y
        self.d=[0,0,0,0,0,0]
        
        self.help_x = 0
        self.help_y = 0
        
        self.x_speed = 0
        self.y_speed = 0
        
        enemylook=[7,7,7,7,7,7]
        
        enemybullet_list=[]
        self.direction=2
       
        self.location=[]
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.deadsound=[]
        self.deadsound.append(pygame.mixer.Sound("hit.ogg"))
        self.deadsound[0].set_volume(0.3)
        self.deadsound.append(pygame.mixer.Sound("blood.ogg"))
        self.deadsound[1].set_volume(0.1)
        self.egunshot= pygame.mixer.Sound("1911.ogg")
        

        
        
        self.mc=0
        
        detect=[0,0,0,0,0,0]
        self.pop=[0,0,0,0,0,0,0,0]
        self.dead=[False,False,False,False,False,False]     
        self.reposition=[False,False,False,False,False,False]
        ehp=[2,2,2,2,2,2,2]
        self.previous_time2 = 0
        self.escape=False
        
    def movement(self):
        global enemylook,detect
        
        self.player_rect = pygame.Rect(px + 31,py +43,2,2)
        self.location[0]=(pygame.Rect(ex-16,ey-313,80,297))
        self.location[1]=(pygame.Rect(ex+65,ey-126,95,110))
        self.location[2]=(pygame.Rect(ex+65,ey-16,282,85))
        self.location[3]=(pygame.Rect(ex+65,ey+69,95,110))
        self.location[4]=(pygame.Rect(ex-16,ey+69,80,290))
        self.location[5]=(pygame.Rect(ex-113,ey+69,95,110))
        self.location[6]=(pygame.Rect(ex-300,ey-16,282,85))
        self.location[7]=(pygame.Rect(ex-113,ey-126,95,110))
        
        if level==1:
            if self.reposition[0]==False:
                        detect[level-1]=0
                        self.rect.x=700
                        self.rect.y=420
                        self.direction=4
                        self.reposition[0]=True
                        
                        self.x_speed=0.01
                        self.y_speed=0.01
                        self.egunshot.stop()
                        
            self.y_speed=0
            self.reposition[1]=False
            if ehp[level-1]>0:
                re[level-1]=False
                if detect[level-1]==0:
                    if self.rect.x <= 1020 and self.direction==2:
                        self.x_speed=2
                        self.rect.x += self.x_speed
                    else:
                        self.direction=4
                        
                    if self.rect.x >=203 and self.direction==4:
                        self.x_speed=-2
                        self.rect.x += self.x_speed
                        
                    else:
                        self.direction=2
                        
                    if self.direction==4 and px>=self.rect.x-180 and px<=self.rect.x+20 and py>=self.rect.y-80 and py<=self.rect.y+80:
                        detect[level-1]=1
                        
                    elif self.direction==2 and px<=self.rect.x+180 and px>=self.rect.x-20 and py>=self.rect.y-80 and py<=self.rect.y+80:
                        detect[level-1]=1       
                
                    
            elif ehp[level-1]<=0:
                self.dead[level-1]=True
                self.egunshot.stop()
            if re[level-1]==True:
                if self.dead[level-1]==True:
                    self.rect.x=-190
                
        elif level==2:
            if self.reposition[1]==False:
                detect[level-1]=0      
                self.rect.x=750
                self.rect.y=200
                self.direction=3
                self.reposition[1]=True
                self.x_speed=0.01
                self.y_speed=0.01
                
                self.egunshot.stop()    
                        
            self.reposition[0]=False
            self.reposition[2]=False
            self.reposition[3]=False
            
              
            if ehp[level-1]>0:
                re[level-1]=False
                if detect[level-1]==0:
                   
                    if self.direction==3:
                        self.x_speed=0
                        self.y_speed=2
                        self.rect.y += self.y_speed
                        
                        if self.rect.y>520:
                            self.y_speed=0
                            self.direction=2
                        
                    if self.direction==2:
                        self.y_speed=0
                        self.x_speed=2
                        self.rect.x += self.x_speed
                        
                        if self.rect.x > 1000:
                            self.x_speed=0
                            self.direction=1
                            
                    if self.direction==1:
                        self.x_speed=0
                        self.y_speed=-2
                        self.rect.y += self.y_speed
                        if self.rect.y<103:
                            self.y_speed=0
                            self.direction=4
                        
                    if self.rect.x >=750 and self.direction==4:
                        self.y_speed=0
                        self.x_speed=-2
                        self.rect.x += self.x_speed
                        
                        if self.rect.x<750:
                            self.x_speed=0
                            self.direction=3
                    
                    if self.direction==3 and px>=self.rect.x-80 and px<=self.rect.x+80 and py<=self.rect.y+120 and py>=self.rect.y-90:
                        detect[level-1]=1
                    
                    elif self.direction==1 and px>=self.rect.x-80 and px<=self.rect.x+80 and py>=self.rect.y-120 and py<=self.rect.y+90:
                        detect[level-1]=1
                    
                    elif self.direction==2 and px>737 and py>500 and px>=self.rect.x-80:
                        detect[level-1]=1
                    
                    elif self.direction==4 and px>737 and py<146 and px<=self.rect.x+80:
                        detect[level-1]=1
            elif ehp[level-1]<=0:
                self.dead[level-1]=True
                self.egunshot.stop()
            if re[level-1]==True:
                if self.dead[level-1]==True:
                    self.rect.x=-190
                else:
                    re[level-1]==False
         
        elif level==3:
            if self.reposition[2]==False:
                detect[level-1]=0       
                self.rect.x=750
                self.rect.y=120
                self.direction=2
                self.reposition[2]=True
                self.x_speed=0.01
                self.y_speed=0.01
                
                self.egunshot.stop()
                        
            
            self.reposition[1]=False
            if ehp[level-1]>0:
                re[level-1]=False
                if detect[level-1]==0:
                   
                    if self.rect.x <= 1020 and self.direction==2:
                        self.x_speed=2
                        self.rect.x += self.x_speed
                    else:
                        self.direction=4
                        
                    if self.rect.x >=203 and self.direction==4:
                        self.x_speed=-2
                        self.rect.x += self.x_speed
                    else:
                        self.direction=2
                    
                    if self.direction==4 and px>=self.rect.x-180 and px<=self.rect.x+20 and py>=self.rect.y-80 and py<=self.rect.y+80:
                        detect[level-1]=1
                        
                    elif self.direction==2 and px<=self.rect.x+180 and px>=self.rect.x-20 and py>=self.rect.y-80 and py<=self.rect.y+80:
                        detect[level-1]=1  
            elif ehp[level-1]<=0:
                self.dead[level-1]=True
                self.egunshot.stop()
            if re[level-1]==True:
                if self.dead[level-1]==True:
                    self.rect.x=-190
                else:
                    re[level-1]==False
            
        elif level==4:
            if self.reposition[3]==False:
                detect[level-1]=0
                self.rect.x=641
                self.rect.y=112
                self.direction=2
                self.reposition[3]=True
                self.x_speed=0.01
                self.y_speed=0.01
                        
                        
            self.reposition[1]=False
            
            if ehp[level-1]>0:
                re[level-1]==False
                
                if detect[level-1]==0:
                    if self.rect.x <= 1020 and self.direction==2:
                        self.x_speed=2
                        self.rect.x += self.x_speed
                    else:
                        self.direction=4
                        
                    if self.rect.x >=610 and self.direction==4:
                        self.x_speed=-2
                        self.rect.x += self.x_speed
                    else:
                        self.direction=2
                    
                    if self.direction==4 and px>=self.rect.x-180 and px<=self.rect.x+20 and py>=self.rect.y-80 and py<=self.rect.y+80:
                        detect[level-1]=1
                        
                    elif self.direction==2 and px<=self.rect.x+180 and px>=self.rect.x-20 and py>=self.rect.y-80 and py<=self.rect.y+80:
                        detect[level-1]=1
            elif ehp[level-1]<=0:
                self.dead[level-1]=True
                self.egunshot.stop()
            if re[level-1]==True:
                if self.dead[level-1]==True:
                    self.rect.x=-190
              
        if detect[level-1]==1:
            for l in range(8):
                if self.player_rect.colliderect(self.location[l]):
                    self.pop[l]=1
                else:
                    self.pop[l]=0
            
            self.x_speed=0
            self.y_speed=0

            current_time2 = pygame.time.get_ticks()
            
            if self.pop!=[0,0,0,0,0,0,0,0]:
                if current_time2 - self.previous_time2 > 800:
                    
                   
                    self.previous_time2 = current_time2
                    enemybullet_list.append(EnemyBullet(level-1))
                    self.egunshot.play()
            
            if self.dead[level-1]==False:
                if self.player_rect.colliderect(self.location[0]) :
                    enemylook[level-1]=1
                    self.tempim=self.usprites[0]          
                
                if self.player_rect.colliderect(self.location[1]):
                    enemylook[level-1]=2
                    self.tempim=self.ursprites[0]
                    
                if self.player_rect.colliderect(self.location[2]):
                    enemylook[level-1]=3
                    self.tempim=self.rsprites[0]
                    
                if self.player_rect.colliderect(self.location[3]):
                    enemylook[level-1]=4
                    self.tempim=self.drsprites[0]
                    
                if self.player_rect.colliderect(self.location[4]) :
                    enemylook[level-1]=5
                    self.tempim=self.dsprites[0]
                    
                if self.player_rect.colliderect(self.location[5]):
                    enemylook[level-1]=6
                    self.tempim=self.dlsprites[0]
                    
                if self.player_rect.colliderect(self.location[6]) :
                    enemylook[level-1]=7
                    self.tempim=self.lsprites[0]
                    
                if self.player_rect.colliderect(self.location[7]) :
                    enemylook[level-1]=8
                    self.tempim=self.ulsprites[0]
                self.d[level-1]=0
            self.image=self.tempim
        
    def update(self, speed):
        global ey,ex
        if ehp[level-1]>0:   
            
            
            ex=self.rect.x
            ey=self.rect.y
            if self.x_speed==2 and self.y_speed==-2:
                self.current_sprite += speed
                if int(self.current_sprite) >= len(self.ursprites):
                    self.current_sprite = 1
               
                self.tempim=self.ursprites[0]                     
                self.image = self.ursprites[int(self.current_sprite)]
                
            elif self.x_speed==-2 and self.y_speed==-2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.ulsprites):
                    self.current_sprite = 1
               
                self.tempim=self.ulsprites[0]
                self.image = self.ulsprites[int(self.current_sprite)]
                
            elif self.x_speed==-2 and self.y_speed==2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.dlsprites):
                    self.current_sprite = 1
                
                self.tempim=self.dlsprites[0]       
                self.image = self.dlsprites[int(self.current_sprite)]
                
            elif self.x_speed==2 and self.y_speed==2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.drsprites):
                    self.current_sprite = 1
                
                self.tempim=self.drsprites[0]       
                self.image = self.drsprites[int(self.current_sprite)]
                
            elif self.y_speed==2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.dsprites):
                    self.current_sprite = 1
                
                self.tempim=self.dsprites[0]        
                self.image = self.dsprites[int(self.current_sprite)]
                
            elif self.y_speed==-2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.usprites):
                    self.current_sprite = 1
                    
                
                self.tempim=self.usprites[0]       
                self.image = self.usprites[int(self.current_sprite)]  
                
            elif self.x_speed==-2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.lsprites):
                    self.current_sprite = 1
                
                self.tempim=self.lsprites[0]       
                self.image = self.lsprites[int(self.current_sprite)] 
                
            elif self.x_speed==2:
                self.current_sprite += speed
                
                if int(self.current_sprite) >= len(self.rsprites):
                    self.current_sprite = 1
               
                self.tempim=self.rsprites[0] 
                self.image = self.rsprites[int(self.current_sprite)]
 
        else:
            
            self.x_speed=0
            
            
            if int(self.d[level-1]) < 2:
                if self.d[level-1]==0:
                    self.deadsound[0].play()
                    self.deadsound[1].play()
                self.d[level-1] += speed*3
                
                
                self.tempim = self.deadsprites[int(self.d[level-1])]
                self.image=self.tempim
                
class SecondEnemy(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y):
        global sex,sey,sehp,enemylook,detect,enemybullet_list
        super().__init__()
        self.dsprites = []
        self.usprites = []
        self.rsprites = []
        self.lsprites = []
        self.ursprites = []
        self.ulsprites = []
        self.dlsprites = []
        self.drsprites = []
        self.deadsprites = []
        
        self.usprites.append(pygame.image.load('g_up1.png'))
        self.usprites.append(pygame.image.load('g_up2.png'))
        self.usprites.append(pygame.image.load('g_up3.png'))
        self.usprites.append(pygame.image.load('g_up4.png'))
        self.usprites.append(pygame.image.load('g_up5.png'))
        
        self.dsprites.append(pygame.image.load('g_attack3.png'))
        self.dsprites.append(pygame.image.load('g_down2.png'))
        self.dsprites.append(pygame.image.load('g_down3.png'))
        self.dsprites.append(pygame.image.load('g_down4.png'))
        self.dsprites.append(pygame.image.load('g_down5.png'))
        
        self.lsprites.append(pygame.image.load('g_left1.png'))
        self.lsprites.append(pygame.image.load('g_left2.png'))
        self.lsprites.append(pygame.image.load('g_left3.png'))
        self.lsprites.append(pygame.image.load('g_left4.png'))
        self.lsprites.append(pygame.image.load('g_left5.png'))
        
        self.rsprites.append(pygame.image.load('g_right1.png'))
        self.rsprites.append(pygame.image.load('g_right2.png'))
        self.rsprites.append(pygame.image.load('g_right3.png'))
        self.rsprites.append(pygame.image.load('g_right4.png'))
        self.rsprites.append(pygame.image.load('g_right5.png'))
        
        self.ulsprites.append(pygame.image.load('g_upleft1.png'))
        self.ulsprites.append(pygame.image.load('g_upleft2.png'))
        self.ulsprites.append(pygame.image.load('g_upleft3.png'))
        self.ulsprites.append(pygame.image.load('g_upleft4.png'))
        self.ulsprites.append(pygame.image.load('g_upleft5.png'))   
        
        self.ursprites.append(pygame.image.load('g_upright1.png'))
        self.ursprites.append(pygame.image.load('g_upright2.png'))
        self.ursprites.append(pygame.image.load('g_upright3.png'))
        self.ursprites.append(pygame.image.load('g_upright4.png'))
        self.ursprites.append(pygame.image.load('g_upright5.png'))
        
        self.dlsprites.append(pygame.image.load('g_downleft1.png'))
        self.dlsprites.append(pygame.image.load('g_downleft2.png'))
        self.dlsprites.append(pygame.image.load('g_downleft3.png'))
        self.dlsprites.append(pygame.image.load('g_downleft4.png'))
        self.dlsprites.append(pygame.image.load('g_downleft5.png'))
        
        self.drsprites.append(pygame.image.load('g_downright1.png'))
        self.drsprites.append(pygame.image.load('g_downright2.png'))
        self.drsprites.append(pygame.image.load('g_downright3.png'))
        self.drsprites.append(pygame.image.load('g_downright4.png'))
        self.drsprites.append(pygame.image.load('g_downright5.png'))
        
        self.deadsprites.append(pygame.image.load('g_dead1.png'))    
        self.deadsprites.append(pygame.image.load('g_dead2.png'))    
        self.deadsprites.append(pygame.image.load('g_dead3.png'))  
        
        self.attack=pygame.image.load('g_attack1.png')
        
        self.current_sprite = 0
        self.tempim = self.dsprites[0]
        self.image = self.dsprites[0]
        self.rect = self.image.get_rect() 
        
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        sex=self.rect.x
        sey=self.rect.y
        self.d=[0,0,0,0,0,0,0]
        
        self.help_x = 0
        self.help_y = 0
        
        self.x_speed = 0
        self.y_speed = 0
        self.egunshot= pygame.mixer.Sound("1911.ogg")
        self.deadsound=[]
        self.deadsound.append(pygame.mixer.Sound("hit.ogg"))
        self.deadsound[0].set_volume(0.1)
        self.deadsound.append(pygame.mixer.Sound("blood.ogg"))
        self.deadsound[1].set_volume(0.1)
        
        self.pop=[0,0,0,0,0,0,0,0]
        
        self.direction=2
        
        self.location=[]
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        self.location.append(pygame.Rect(0,0,0,0)) 
        
       
        
        self.mc=0
        
        self.dead=[False,False,False,False,False,False,False]     
        self.reposition=[False,False,False,False,False,False,False]
        
        self.previous_time = pygame.time.get_ticks()
        
    def movement(self):
        global enemylook,detect

        self.player_rect = pygame.Rect(px + 31,py +43,2,2)
        self.location[0]=(pygame.Rect(sex-16,sey-313,80,297))
        self.location[1]=(pygame.Rect(sex+65,sey-126,95,110))
        self.location[2]=(pygame.Rect(sex+65,sey-16,282,85))
        self.location[3]=(pygame.Rect(sex+65,sey+69,95,110))
        self.location[4]=(pygame.Rect(sex-16,sey+69,80,290))
        self.location[5]=(pygame.Rect(sex-113,sey+69,95,110))
        self.location[6]=(pygame.Rect(sex-300,sey-16,282,85))
        self.location[7]=(pygame.Rect(sex-113,sey-126,95,110))
            
        if level==3:
            
                if self.reposition[2]==False and self.dead[level+1]==False:
                    detect[level+1]=0    
                    self.rect.x=242
                    self.rect.y=506
                    self.direction=2
                    self.reposition[2]=True
                    self.x_speed=0.01
                    self.y_speed=0.01
                          
                self.reposition[3]=False
               
                if ehp[level+1]>0:
                    re[level+1]=False
                    if detect[level+1]==0:
                        
                        if self.rect.x <= 1020 and self.direction==2:
                            self.x_speed=2
                            self.rect.x += self.x_speed
                        else:
                            self.direction=4
                            
                        if self.rect.x >=203 and self.direction==4:
                            self.x_speed=-2
                            self.rect.x += self.x_speed
                        else:
                            self.direction=2
                            
                        if self.direction==4 and px>=self.rect.x-180 and px<=self.rect.x+20 and py>=self.rect.y-80 and py<=self.rect.y+80:
                            detect[level+1]=1
                            
                        elif self.direction==2 and px<=self.rect.x+180 and px>=self.rect.x-20 and py>=self.rect.y-80 and py<=self.rect.y+80:
                            detect[level+1]=1  
                elif ehp[level+1]<=0:
                    self.dead[level+1]=True
                    self.egunshot.stop()
                if re[level-1]==True:
                    if self.dead[level+1]==True:
                        self.rect.x=-190   
                    
        elif level==4:
            
                if self.reposition[3]==False and self.dead[level+1]==False:
                    detect[level+1]=0 
                    self.rect.x=211
                    self.rect.y=337
                    self.direction=2
                    self.reposition[3]=True
                    self.x_speed=0.01
                    self.y_speed=0.01
                             
                self.reposition[2]=False
                
                if ehp[level+1]>0:
                    re[level+1]=False
                    if detect[level+1]==0:
                        if self.rect.x <= 1020 and self.direction==2:
                            self.x_speed=2
                            self.rect.x += self.x_speed
                        else:
                            self.direction=4
                            
                        if self.rect.x >=203 and self.direction==4:
                            self.x_speed=-2
                            self.rect.x += self.x_speed
                        else:
                            self.direction=2
                        
                        if self.direction==4 and px>=self.rect.x-180 and px<=self.rect.x+20 and py>=self.rect.y-80 and py<=self.rect.y+80:
                            detect[level+1]=1
                            
                        elif self.direction==2 and px<=self.rect.x+180 and px>=self.rect.x-20 and py>=self.rect.y-80 and py<=self.rect.y+80:
                            detect[level+1]=1                  
                elif ehp[level+1]<=0:
                    self.dead[level+1]=True
                    self.egunshot.stop()
                if re[level+1]==True:
                    if self.dead[level+1]==True:
                        self.rect.x=-190   
                    else:
                        re[level+1]==False
                
            
        
        if detect[level+1]==1:
            for l in range(8):
                if self.player_rect.colliderect(self.location[l]):
                    self.pop[l]=1
                else:
                    self.pop[l]=0
            self.x_speed=0
            self.y_speed=0
            
            current_time = pygame.time.get_ticks()
            if self.pop!=[0,0,0,0,0,0,0,0]:
                if current_time - self.previous_time > 800:
                    
                    self.previous_time = current_time
                    enemybullet_list.append(EnemyBullet(level+1))
                    self.egunshot.play()
                    
            if self.dead[level+1]==False:
                if self.player_rect.colliderect(self.location[0]):
                    enemylook[level+1]=1
                    self.tempim=self.usprites[0]          
                
                if self.player_rect.colliderect(self.location[1]):
                    enemylook[level+1]=2
                    self.tempim=self.ursprites[0]
                    
                if self.player_rect.colliderect(self.location[2]):
                    enemylook[level+1]=3
                    self.tempim=self.rsprites[0]
                    
                if self.player_rect.colliderect(self.location[3]):
                    enemylook[level+1]=4
                    self.tempim=self.drsprites[0]
                    
                if self.player_rect.colliderect(self.location[4]):
                    enemylook[level+1]=5
                    self.tempim=self.dsprites[0]
                    
                if self.player_rect.colliderect(self.location[5]):
                    enemylook[level+1]=6
                    self.tempim=self.dlsprites[0]
                    
                if self.player_rect.colliderect(self.location[6]):
                    enemylook[level+1]=7
                    self.tempim=self.lsprites[0]
                    
                if self.player_rect.colliderect(self.location[7]):
                    enemylook[level+1]=8
                    self.tempim=self.ulsprites[0]
                self.d[level+1]=0
            self.image=self.tempim
        if level==1 or level==2:
                self.rect.x=-190 
                self.reposition[2]=False
                self.reposition[3]=False
    def update(self, speed):
        global sey,sex,ehp
        if level==3 or level==4:
            if ehp[level+1]>0:   
                sex=self.rect.x
                sey=self.rect.y
                
                if self.x_speed==2 and self.y_speed==-2:
                    self.current_sprite += speed
                    if int(self.current_sprite) >= len(self.ursprites):
                        self.current_sprite = 1
                   
                    self.tempim=self.ursprites[0]                     
                    self.image = self.ursprites[int(self.current_sprite)]
                    
                elif self.x_speed==-2 and self.y_speed==-2:
                    self.current_sprite += speed
                    
                    if int(self.current_sprite) >= len(self.ulsprites):
                        self.current_sprite = 1
                   
                    self.tempim=self.ulsprites[0]
                    self.image = self.ulsprites[int(self.current_sprite)]
                    
                elif self.x_speed==-2 and self.y_speed==2:
                    self.current_sprite += speed
                    
                    if int(self.current_sprite) >= len(self.dlsprites):
                        self.current_sprite = 1
                    
                    self.tempim=self.dlsprites[0]       
                    self.image = self.dlsprites[int(self.current_sprite)]
                    
                elif self.x_speed==2 and self.y_speed==2:
                    self.current_sprite += speed
                    
                    if int(self.current_sprite) >= len(self.drsprites):
                        self.current_sprite = 1
                    
                    self.tempim=self.drsprites[0]       
                    self.image = self.drsprites[int(self.current_sprite)]
                    
                elif self.y_speed==2:
                    self.current_sprite += speed
                    
                    if int(self.current_sprite) >= len(self.dsprites):
                        self.current_sprite = 1
                    
                    self.tempim=self.dsprites[0]        
                    self.image = self.dsprites[int(self.current_sprite)]
                    
                elif self.y_speed==-2:
                    self.current_sprite += speed
                    
                    if int(self.current_sprite) >= len(self.usprites):
                        self.current_sprite = 1
                        
                    
                    self.tempim=self.usprites[0]       
                    self.image = self.usprites[int(self.current_sprite)]  
                    
                elif self.x_speed==-2: 
                    self.current_sprite += speed
                    
                    if int(self.current_sprite) >= len(self.lsprites):
                        self.current_sprite = 1
                    
                    self.tempim=self.lsprites[0]       
                    self.image = self.lsprites[int(self.current_sprite)] 
                    
                elif self.x_speed==2:
                    self.current_sprite += speed
                    
                    if int(self.current_sprite) >= len(self.rsprites):
                        self.current_sprite = 1
                   
                    self.tempim=self.rsprites[0] 
                    self.image = self.rsprites[int(self.current_sprite)]
                    
            else:
                self.x_speed=0
                
                
                if int(self.d[level+1]) < 2:
                    if self.d[level+1]==0:
                        self.deadsound[0].play()
                        self.deadsound[1].play()
                    self.d[level+1] += 0.1*3
                    
                    
                    self.tempim = self.deadsprites[int(self.d[level+1])]
                    self.image=self.tempim                
                
            

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        global ehp,wall_rect,wall_rect_2
        super().__init__()
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect() 
        self.rect.x=0
        self.rect.y=0
        self.x_speed = 0
        self.y_speed = 0
        self.a=0
        self.end=0
        self.shoot=True
        
    def movement(self):
        global ehp,detect,enemylook
        self.a=0
        self.bullet_rect = pygame.Rect(self.rect.x,self.rect.y,2,2)
        if php>0:
            if self.end==0 and self.shoot and self.x_speed==0 and self.y_speed==0 and pspeed:           
                if look==7:
                    self.x_speed = -8
                    self.rect.x= px+8
                    self.rect.y= py+34
                    self.end=1
                elif look==6:
                    self.x_speed = -8
                    self.y_speed = 8
                    self.rect.x= px+16
                    self.rect.y= py+49
                    self.end=1
                elif look==3:
                    self.x_speed = 8
                    self.rect.x= px+54
                    self.rect.y= py+34
                    self.end=1
                elif look==1:
                    self.y_speed = -7
                    self.rect.x= px+28
                    self.rect.y= py-2
                    self.end=1
                elif look==5:
                    self.y_speed = 8
                    self.rect.x= px+27
                    self.rect.y= py+34
                    self.end=1
                elif look==4:
                    self.x_speed = 8
                    self.y_speed = 8
                    self.rect.x= px+48
                    self.rect.y= py+49
                    self.end=1
                elif look==8:
                    self.x_speed = -8
                    self.y_speed = -8
                    self.rect.x= px+18
                    self.rect.y= py+18
                    self.end=1
                elif look==2:
                    self.x_speed = 8
                    self.y_speed = -8
                    self.rect.x= px+43
                    self.rect.y= py+19
                    self.end=1
                
            elif self.rect.x>=1070:
                self.end=0
                self.rect.x=-10
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.rect.x<=203:
                self.end=0
                self.rect.x=-10
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.rect.y<=103:
                self.end=0
                self.rect.y=-10
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.rect.y>=620:
                self.end=0
                self.rect.y=-10
                self.x_speed=0
                self.y_speed=0
                self.kill()
            if level==1:
                for i in range(7):
                    if self.bullet_rect.colliderect(wall_rect[i]):
                      self.a=1    
            elif level==2:
                for i in range(6):
                    if self.bullet_rect.colliderect(wall_rect_2[i]):
                      self.a=1  
            elif level==3:
                for i in range(8):
                    if self.bullet_rect.colliderect(wall_rect_3[i]):
                      self.a=1  
            elif level==4:
                for i in range(8):
                    if self.bullet_rect.colliderect(wall_rect_4[i]):
                      self.a=1
            if self.rect.x<px-220 or self.rect.x>px+220 or self.rect.y<py-220 or self.rect.y>py+220:
                self.a=1
            if self.a==1:
                self.end=0
                self.rect.x=-10
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.rect.x>=ex and self.rect.x<=ex+62 and self.rect.y<=ey+87 and self.rect.y>=ey and ehp[level-1]>0:
                self.end=0
                self.rect.y=-10
                self.x_speed=0
                self.y_speed=0
                ehp[level-1]-=1
                detect[level-1]=1
                self.kill()
            if level==3 or level==4:
                
                if self.rect.x>=sex and self.rect.x<=sex+62 and self.rect.y<=sey+87 and self.rect.y>=sey and ehp[level+1]>0:
                    self.end=0
                    self.rect.y=-10
                    self.x_speed=0
                    self.y_speed=0
                    ehp[level+1]-=1
                    detect[level+1]=1  
                    self.kill()
        self.shoot=False
    
                
    def update(self, speed):
        self.rect.x+=self.x_speed
        self.rect.y+=self.y_speed
        
class Grenade(pygame.sprite.Sprite):
    def __init__(self):
        global ehp,wall_rect,wall_rect_2
        super().__init__()
        self.attack_animation = False
        self.gsprites = []
       
        self.gsprites.append(pygame.image.load('grenade1.png'))
        self.gsprites.append(pygame.image.load('grenade2.png'))
        self.gsprites.append(pygame.image.load('grenade3.png'))
        self.gsprites.append(pygame.image.load('grenade4.png'))
        self.gsprites.append(pygame.image.load('grenade5.png'))
        self.gsprites.append(pygame.image.load('grenade6.png'))
        self.gsprites.append(pygame.image.load('grenade7.png'))
        self.gsprites.append(pygame.image.load('grenade8.png'))
        self.gsprites.append(pygame.image.load('grenade9.png'))
        self.gsprites.append(pygame.image.load('grenade10.png'))
        self.gsprites.append(pygame.image.load('grenade11.png'))
        self.gsprites.append(pygame.image.load('grenade12.png'))
        
        self.current_sprite = 0
        self.image = self.gsprites[self.current_sprite]
        self.rect = self.image.get_rect()
        
        self.rect.x= 10
        self.rect.y=100
               
        self.x_speed = 0
        self.y_speed = 0
        
        self.a=0
        
        self.end=0
        
        self.shoot=True
        self.expl = False
        
        
    def movement(self):
        global ehp,detect,enemylook
        self.a=0
        self.grenade_rect = pygame.Rect(self.rect.x,self.rect.y,2,2)
        if php>0:
            if self.end==0 and self.shoot and self.x_speed==0 and self.y_speed==0 and pspeed:           
                if look==7:
                    self.x_speed = -8
                    self.rect.x= px+8
                    self.rect.y= py+34
                    self.end=1
                    self.attack_animation = True
                elif look==6:
                    self.x_speed = -8
                    self.y_speed = 8
                    self.rect.x= px+16
                    self.rect.y= py+49
                    self.end=1
                    self.attack_animation = True
                elif look==3:
                    self.x_speed = 8
                    self.rect.x= px+54
                    self.rect.y= py+34
                    self.end=1
                    self.attack_animation = True
                elif look==1:
                    self.y_speed = -7
                    self.rect.x= px+28
                    self.rect.y= py-2
                    self.end=1
                    self.attack_animation = True
                elif look==5:
                    self.y_speed = 8
                    self.rect.x= px+27
                    self.rect.y= py+34
                    self.end=1
                    self.attack_animation = True
                elif look==4:
                    self.x_speed = 8
                    self.y_speed = 8
                    self.rect.x= px+48
                    self.rect.y= py+49
                    self.end=1
                    self.attack_animation = True
                elif look==8:
                    self.x_speed = -8
                    self.y_speed = -8
                    self.rect.x= px+18
                    self.rect.y= py+18
                    self.end=1
                    self.attack_animation = True
                elif look==2:
                    self.x_speed = 8
                    self.y_speed = -8
                    self.rect.x= px+43
                    self.rect.y= py+19
                    self.end=1
                    self.attack_animation = True
                     
            elif self.rect.x>=1070:
                self.end=0
                self.rect.x=-20
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.rect.x<=203:
                self.end=0
                self.rect.x=-20
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.rect.y<=103:
                self.end=0
                self.rect.y=-20
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.rect.y>=620:
                self.end=0
                self.rect.y=-20
                self.x_speed=0
                self.y_speed=0
                self.kill()
            if level==1:
                for i in range(7):
                    if self.grenade_rect.colliderect(wall_rect[i]):
                      self.a=1    
            elif level==2:
                for i in range(6):
                    if self.grenade_rect.colliderect(wall_rect_2[i]):
                      self.a=1  
            elif level==3:
                for i in range(8):
                    if self.grenade_rect.colliderect(wall_rect_3[i]):
                      self.a=1  
            elif level==4:
                for i in range(8):
                    if self.grenade_rect.colliderect(wall_rect_4[i]):
                      self.a=1
            if self.rect.x<px-220 or self.rect.x>px+220 or self.rect.y<py-220 or self.rect.y>py+220:
                self.a=1
            if self.a==1:
                self.end=0
                self.x_speed=0
                self.y_speed=0
            elif self.rect.x>=ex and self.rect.x<=ex+62 and self.rect.y<=ey+87 and self.rect.y>=ey and ehp[level-1]>0:
                self.end=0
                self.rect.x=ex
                self.current_sprite = 6
                self.x_speed=0
                self.y_speed=0
                ehp[level-1]-=2
                detect[level-1]=1
                
            if level==3 or level==4:
                
                if self.rect.x>=sex and self.rect.x<=sex+62 and self.rect.y<=sey+87 and self.rect.y>=sey and ehp[level+1]>0:
                    self.end=0
                    self.rect.x=ex
                    self.current_sprite = 6
                    self.x_speed=0
                    self.y_speed=0
                    ehp[level+1]-=1
                    detect[level+1]=1  
        self.shoot=False
                
    def update(self, speed):
        if self.attack_animation == True:
                self.current_sprite += speed
        # if int(self.current_sprite) == 5:
                # self.current_sprite = 0
        if int(self.current_sprite) >= len(self.gsprites):
            self.current_sprite = 0
            self.rect.x = -20
            self.attack_animation = False 
            self.kill()
               
        self.image = self.gsprites[int(self.current_sprite)]
        
        if self.expl == False:
            self.rect.x+=self.x_speed
            self.rect.y+=self.y_speed
        
        
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self,num):
        global ehp,wall_rect,wall_rect_2
        super().__init__()
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect() 
        
        self.rect.x=-190
        self.rect.y=-190
               
        self.x_speed = 0
        self.y_speed = 0
        
        self.a=0
        self.n=num
        self.end=0
        
        self.shoot=True
        
        self.xpos=-190
        self.ypos=-190
        
    def movement(self):
        global ehp,php
        self.a=0
        
        
        if self.n<4:
            self.xpos=ex
            self.ypos=ey
            self.levelnow=level-1
        else:
            self.xpos=sex
            self.ypos=sey
            self.levelnow=level+1

        self.bullet_rect = pygame.Rect(self.rect.x,self.rect.y,2,2)
        if php>0 and ehp[self.levelnow]>0 and detect[self.levelnow]==1:
            
            if self.end==0 and self.shoot and self.x_speed==0 and self.y_speed==0:  
                
                
                if enemylook[self.levelnow]==7:
                    self.x_speed = -8
                    self.rect.x= self.xpos+8
                    self.rect.y= self.ypos+34
                    self.end=1
                elif enemylook[self.levelnow]==6:
                    self.x_speed = -8
                    self.y_speed = 8
                    self.rect.x= self.xpos+16
                    self.rect.y= self.ypos+49
                    self.end=1
                elif enemylook[self.levelnow]==3:
                    self.x_speed = 8
                    self.rect.x= self.xpos+54
                    self.rect.y= self.ypos+34
                    self.end=1
                elif enemylook[self.levelnow]==1:
                    self.y_speed = -7
                    self.rect.x= self.xpos+28
                    self.rect.y= self.ypos-2
                    self.end=1
                elif enemylook[self.levelnow]==5:
                    self.y_speed = 8
                    self.rect.x= self.xpos+27
                    self.rect.y= self.ypos+34
                    self.end=1
                elif enemylook[self.levelnow]==4:
                    self.x_speed = 8
                    self.y_speed = 8
                    self.rect.x= self.xpos+48
                    self.rect.y= self.ypos+49
                    self.end=1
                elif enemylook[self.levelnow]==8:
                    self.x_speed = -8
                    self.y_speed = -8
                    self.rect.x= self.xpos+18
                    self.rect.y= self.ypos+18
                    self.end=1
                elif enemylook[self.levelnow]==2:
                    self.x_speed = 8
                    self.y_speed = -8
                    self.rect.x= self.xpos+43
                    self.rect.y= self.ypos+19
                    self.end=1
                
            if level==1:
                for i in range(7):
                    if self.bullet_rect.colliderect(wall_rect[i]):
                      self.a=1    
            elif level==2:
                for i in range(6):
                    if self.bullet_rect.colliderect(wall_rect_2[i]):
                      self.a=1  
            elif level==3:
                for i in range(8):
                    if self.bullet_rect.colliderect(wall_rect_3[i]):
                      self.a=1  
            elif level==4:
                for i in range(8):
                    if self.bullet_rect.colliderect(wall_rect_4[i]):
                      self.a=1  
                      
            if self.rect.x<px-250 or self.rect.x>px+250 or self.rect.y<py-250 or self.rect.y>py+250:
                self.a=1
            if self.a==1:
                self.end=0
                self.rect.x=-10
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.bullet_rect.colliderect(player_rect):
                
                php-=1
                player.get_damage(200)
                self.rect.x=-10
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.rect.x>=1070:
                self.end=0
                self.rect.x=-10
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.rect.x<=203:
                self.end=0
                self.rect.x=-10
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.rect.y<=103:
                self.end=0
                self.rect.y=-10
                self.x_speed=0
                self.y_speed=0
                self.kill()
            elif self.rect.y>=620:
                self.end=0
                self.rect.y=-10
                self.x_speed=0
                self.y_speed=0
                self.kill()
        if ehp[self.levelnow]<=0:
            self.kill()
        self.shoot=False
            
                
    def update(self, speed):
        
        self.rect.x+=self.x_speed
        self.rect.y+=self.y_speed
        
class Chest(pygame.sprite.Sprite):
    def __init__(self):
        global opened,keylist,use,bulletcount, grenadecount
        super().__init__()
        self.chestsound= pygame.mixer.Sound("porta.ogg")
        self.cchestx=pygame.image.load('closedx.png')
        self.ochestx=pygame.image.load('openx.png')
        self.cchesty=pygame.image.load('closedy.png')
        self.ochesty=pygame.image.load('openy.png')
        
        self.image=self.cchestx
        self.rect = self.image.get_rect() 
        bulletcount=5
        grenadecount = 0
        opened=[False,False,False,False,False]
        self.c=0
        self.x=0
        use=False
        
        
    def update(self,speed):
        global php,keylist,current_key,bulletcount, grenadecount
        if opened[level-1]:
            self.image=self.ochestx
            
            font = pygame.font.SysFont("arial", 25)
            text = font.render("You got a key, bullets, a grenade and you healed up", True, (255, 255, 255))
            if self.x<60:
                self.x+=0.5
                screen.blit(text,(660 - text.get_width() // 2, 670 - text.get_height() // 2)) 
        else:
            self.image=self.cchestx
            
        if level==1:
            self.rect.x=620
            self.rect.y=102
        if level==2:
            self.rect.x=600
            self.rect.y=502
        if level==3:
            self.rect.x=523
            self.rect.y=307
        if level==4:
            self.rect.x=540
            self.rect.y=102
        if self.c==0:
           self.image=self.cchestx
           self.c=+1
        if py<=self.rect.y+120 and py>=self.rect.y-120 and px<=self.rect.x+120 and px>=self.rect.x-120 and use and opened[level-1]==False:
            opened[level-1]=True
            keylist[level-1]=True
            current_key=level-1
            bulletcount+=3
            grenadecount += 1
            if php < 4:
                php += 1
            player.get_hp(200)
            
            self.x=0
            self.chestsound.play()
            
class Key(pygame.sprite.Sprite):
    def __init__(self):
        global current_key
        super().__init__()
        self.keysprites=[]
        self.keysprites.append(pygame.image.load('red key.png'))
        self.keysprites.append(pygame.image.load('green key.png'))
        self.keysprites.append(pygame.image.load('new blue key.png'))
        self.keysprites.append(pygame.image.load('gold key.png'))
        current_key=-1
        self.image=self.keysprites[0]
        self.rect = self.image.get_rect()
        self.rect.x=30
        self.rect.y=120
    def update(self, speed):
        global current_key

        if current_key!=-1:
            self.rect.x=20
            self.rect.y=120
            self.image=self.keysprites[current_key]
        else:
            self.rect.x=-190
  
# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
player_list = pygame.sprite.Group()
# Game Screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Game")
background_image = []
background_image.append(pygame.image.load("1st level v4.jpg").convert())
background_image.append(pygame.image.load("2nd all.jpg").convert())
background_image.append(pygame.image.load("3rd level.jpg").convert())
background_image.append(pygame.image.load("4th level.jpg").convert())
background_image.append(pygame.image.load("5th level.jpg").convert())

game_over=pygame.image.load("Game Over.jpg").convert()
endscreen=pygame.image.load("ending.jpg").convert()

grenadesound= pygame.mixer.Sound("grenade.ogg")
grenadesound.set_volume(0.2)
gunshot= pygame.mixer.Sound("1911.ogg")
game_over_sound=pygame.mixer.Sound("game over.ogg")
game_over_sound.set_volume(0.2)
endsound=pygame.mixer.Sound("ending.ogg")
endsound.set_volume(0.1)
overworld=pygame.mixer.Sound("cave.ogg")
overworld.set_volume(0.1)

b_count = pygame.image.load('b_count.png')
bx = 15
by =70

# Creating the sprites and groups

moving_sprites = pygame.sprite.Group()
player = Player()
enemy = Enemy(900,420)
secenemy = SecondEnemy(900,420)

chest=Chest()
key=Key()
moving_sprites.add(chest)
moving_sprites.add(enemy)
moving_sprites.add(secenemy)
moving_sprites.add(player)
moving_sprites.add(key)

bullet_list=[]
grenade_list=[]
previous_time = pygame.time.get_ticks()
once=0
flag=0
with open(os.path.join("ps4_buttons.json"), 'r+') as file:
    button_keys = json.load(file)

analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1 }
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()
    
font = pygame.font.Font('freesansbold.ttf', 12)
b_cx = 45
b_cy = 73
g_cx = 105
g_cy = 73

def Bullet_Counter(x,y):
    bulletcounter = font.render(":"+str(bulletcount), True, WHITE)
    screen.blit(bulletcounter, (x, y))
    if bulletcount == 0:
        b_counter = font.render(":"+str(bulletcount), True, RED)
        screen.blit(b_counter, (x, y))
        
def Grenade_Counter(x,y):
    grenadecounter = font.render(":"+str(grenadecount), True, WHITE)
    screen.blit(grenadecounter, (x, y))
    if grenadecount == 0:
        grenadecounter = font.render(":"+str(grenadecount), True, RED)
        screen.blit(grenadecounter, (x, y))
        
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.a_pressed = True
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_d:
                player.d_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_w:
                player.w_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_s:
                player.s_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
            if event.key == pygame.K_e:
                use = True
            if event.key == pygame.K_g and player.a_pressed == False and player.w_pressed == False and player.d_pressed == False and player.s_pressed == False :
                current_time = pygame.time.get_ticks()
                if grenadecount>0:
                    if current_time - previous_time > 500:
                        grenadesound.play()
                        previous_time = current_time
                        grenade_list.append(Grenade())
                        grenadecount -= 1
            if event.key == pygame.K_SPACE and player.a_pressed == False and player.w_pressed == False and player.d_pressed == False and player.s_pressed == False:
                current_time = pygame.time.get_ticks()
                if bulletcount>0:
                    if current_time - previous_time > 400:
                        gunshot.play()
                        previous_time = current_time
                        bullet_list.append(Bullet())
                        bulletcount-=1
                
         
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.a_pressed = False
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_d:
                player.d_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_w:
                player.w_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_s:
                player.s_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
            if event.key == pygame.K_e:
                use = False
        
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys['R1'] and player.a_pressed == False and player.w_pressed == False and player.d_pressed == False and player.s_pressed == False:
                current_time = pygame.time.get_ticks()  
                if bulletcount>0:
                    if current_time - previous_time > 500:
                        gunshot.play()
                        previous_time = current_time
                        bullet_list.append(Bullet())
                        bulletcount -= 1
                    
            if event.button == button_keys['L1'] and player.a_pressed == False and player.w_pressed == False and player.d_pressed == False and player.s_pressed == False:
                current_time = pygame.time.get_ticks()
                if grenadecount > 0:
                    if current_time - previous_time > 500:
                        grenadesound.play()
                        previous_time = current_time
                        grenade_list.append(Grenade())
                        grenadecount -= 1
                    
            if event.button == button_keys['triangle']:
                chest.use = True
            if event.button == button_keys['left_arrow']:
                player.a_pressed = True
            if event.button == button_keys['right_arrow']:
                player.d_pressed = True
            if event.button == button_keys['up_arrow']:
                player.w_pressed = True
            if event.button == button_keys['down_arrow']:
                player.s_pressed = True
                
        if event.type == pygame.JOYBUTTONUP:
            if event.button == button_keys['left_arrow']:
                player.a_pressed = False
            if event.button == button_keys['right_arrow']:
                player.d_pressed = False
            if event.button == button_keys['up_arrow']:
                player.w_pressed = False
            if event.button == button_keys['down_arrow']:
                player.s_pressed = False
            if event.button == button_keys['triangle']:
                chest.use = False
                player.sprite.get_damage(200)
                
        if event.type == pygame.JOYAXISMOTION:
            analog_keys[event.axis] = event.value
            
            # Horizontal Analog
            if abs(analog_keys[0]) > .4:
                if analog_keys[0] < -.7:
                    player.a_pressed = True
                else:
                    player.a_pressed = False
                if analog_keys[0] > .7:
                    player.d_pressed = True
                else:
                    player.d_pressed = False
            # Vertical Analog
            if abs(analog_keys[1]) > .4:
                if analog_keys[1] < -.7:
                    player.w_pressed = True
                else:
                    player.w_pressed = False
                if analog_keys[1] > .7:
                    player.s_pressed = True
                else:
                    player.s_pressed = False
                    
    # Drawing
    screen.fill((0,0,0))
    if ending==False:
        if php>0:
            if flag==0:
                overworld.play(-1)
                flag=1
            screen.blit(background_image[player.mainlevel-1], [0, 0])
            screen.blit(b_count, (bx, by))
        
            
                
            player.movement()
            enemy.movement() 
            secenemy.movement() 
            for bullet in bullet_list:
                moving_sprites.add(bullet)
                bullet.movement()
    
                bullet.update(0.1)
            
            for grenade in grenade_list:
                moving_sprites.add(grenade)
                grenade.movement()
    
                grenade.update(0.1)
                
            for enemybullet in enemybullet_list:
                moving_sprites.add(enemybullet)
                enemybullet.movement()
    
                enemybullet.update(0.1)
            
            moving_sprites.draw(screen)
            moving_sprites.update(0.1)
            player.reset()
    
            Grenade_Counter(g_cx, g_cy)
            Bullet_Counter(b_cx, b_cy)
        else:
            screen.blit(game_over,[0, 0])
            if once==0:
                overworld.stop()
                game_over_sound.play()
                once=1
    else:
        screen.blit(endscreen, [0, 0])
        if once==0:
                endsound.play()
                once=1
    pygame.display.flip()
    clock.tick(60)
    
# Close the window and quit.
pygame.quit()